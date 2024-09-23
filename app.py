from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from model.WineImageAPI import WineImageAPI
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
wine_tag = Tag(name="Vinho", description="Adição, visualização, remoção e predição da qualidade do vinho tito")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de listagem de vinhos
@app.get('/vinhos', tags=[wine_tag],
         responses={"200": VinhoViewSchema, "404": ErrorSchema})
def get_vinhos():
    """Lista todos os vinhos cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de vinhos cadastrados na base
    """
    logger.debug("Coletando dados físico-químicos sobre o vinho")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os vinhos
    vinhos = session.query(Vinho).all()
    
    if not vinhos:
        # Se não houver vinho
        return {"vinhos": []}, 200
    else:
        logger.debug(f"%d vinhos encontrados" % len(vinhos))
        print(vinhos)
        return apresenta_vinhos(vinhos), 200


# Rota de adição de vinhos
@app.post('/vinho', tags=[wine_tag],
          responses={"200": VinhoViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: VinhoSchema):
    """Adiciona um novo vinho à base de dados
    Retorna uma representação dos dados físico-químicos dos vinhos e sua qualidade.
    
    Args:
        name (str): nome do vinho
        fixed_acidity (float): Refere-se ao nível de ácidos não voláteis, como ácido tartárico, que não evaporam.
        volatile_acidity (float): Nível de ácidos voláteis, como ácido acético, que podem evaporar facilmente.
        citric_acid (float): Ácido encontrado em pequenas quantidades, que adiciona frescor ao vinho.
        residual_sugar (float): Quantidade de açúcar restante após a fermentação.
        chlorides (float): Refere-se ao sal no vinho, geralmente associado à água usada.
        free_sulfur_dioxide (int): Agente conservante livre, que protege o vinho contra oxidação.
        total_sulfur_dioxide (int): Soma do dióxido de enxofre livre e combinado no vinho.
        density (float): Medida da massa por volume do vinho.
        pH (float): Indica a acidez ou basicidade do vinho.
        sulphates (float): Compostos que contribuem para a preservação do vinho.
        alcohol (float): Percentual de álcool resultante da fermentação.
        
    Returns:
        dict: representação dos dados físico-químicos dos vinhos e sua qualidade.
    """

    ## API que retorna imagens de vinhos
    wine_img_api = WineImageAPI('https://api.sampleapis.com/wines/reds')
    retorno_img = wine_img_api.get_random_url()
       
    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    # Carregando modelo
    # model_path = r'./MachineLearning/pipelines/rf_redwine_pipeline.pkl'
    model_path = r'C:\Users\raque\OneDrive\Documentos\MVP4\Projeto\api\MachineLearning\pipelines\rf_redwine_pipeline.pkl'
    modelo = Pipeline.carrega_pipeline(model_path)
    # Realizando a predição
    quality = int(Model.realiza_predicao(modelo, X_input)[0])
    
    vinho = Vinho(
        image_url = retorno_img,
        name = form.name,
        fixed_acidity = form.fixed_acidity,
        volatile_acidity = form.volatile_acidity,
        citric_acid = form.citric_acid,
        residual_sugar = form.residual_sugar,
        chlorides = form.chlorides,
        free_sulfur_dioxide = form.free_sulfur_dioxide,
        total_sulfur_dioxide = form.total_sulfur_dioxide,
        density = form.density,
        pH = form.pH,
        sulphates = form.sulphates,
        alcohol = form.alcohol,
        quality= quality
    )
    logger.debug(f"Adicionando vinho de nome: '{vinho.name}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        if session.query(Vinho).filter(Vinho.name == form.name).first():
            error_msg = "Vinho já existente na base :/"
            logger.warning(f"Erro ao adicionar vinho '{vinho.name}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando vinho
        session.add(vinho)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado vinho de nome: '{vinho.name}'")
        return apresenta_vinho(vinho), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar vinho '{vinho.name}', {error_msg}")
        return {"message": error_msg}, 400
    
# Rota de busca de vinho por nome
@app.get('/vinho', tags=[wine_tag],
         responses={"200": VinhoViewSchema, "404": ErrorSchema})
def get_vinho(query: VinhoBuscaSchema):    
    """Faz a busca pelo vinho cadastrado na base a partir do nome

    Args:
        nome (str): nome do vinho
        
    Returns:
        dict: representação das características físico-químicas do vinho e sua qualidade
    """
    
    vinho_nome = query.name
    logger.debug(f"Coletando dados sobre produto #{vinho_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    vinho = session.query(Vinho).filter(Vinho.name == vinho_nome).first()
    
    if not vinho:
        # se o vinho não foi encontrado
        error_msg = f"Vinho {vinho_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{vinho_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Vinho encontrado: '{vinho.name}'")
        # retorna a representação das características físico-químicas do vinho e sua qualidade
        return apresenta_vinho(vinho), 200
   
    
# Rota de remoção do vinho por nome
@app.delete('/vinho', tags=[wine_tag],
            responses={"200": VinhoViewSchema, "404": ErrorSchema})
def delete_vinho(query: VinhoBuscaSchema):
    """Remove um vinho cadastrado na base a partir do nome

    Args:
        nome (str): nome do vinho
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    
    vinho_nome = unquote(query.name)
    logger.debug(f"Deletando dados sobre o vinho #{vinho_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    vinho = session.query(Vinho).filter(Vinho.name == vinho_nome).first()
    
    if not vinho:
        error_msg = "Vinho não encontrado na base :/"
        logger.warning(f"Erro ao deletar vinho '{vinho_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(vinho)
        session.commit()
        logger.debug(f"Deletado vinho #{vinho_nome}")
        return {"message": f"Vinho {vinho_nome} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)