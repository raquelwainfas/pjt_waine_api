# Projeto wAIne

### API Qualificador de Vinho Tinto

Esta API foi desenvolvida para facilitar a gestão de dados relacionados a vinhos tintos. Ela oferece endpoints que permitem a inclusão de novos registros, consulta e exclusão de vinhos. Além disso, a API possui funcionalidades para qualificar os vinhos com base nos dados físico-químicos fornecidos, ajudando os usuários a fazer escolhas mais informadas.

Video de apresentação aqui: [![Watch the video](https://img.youtube.com/vi/VIDEO_ID/hqdefault.jpg)](https://youtu.be/Ec8KdOR48CA)

### As principais tecnologias que serão utilizadas aqui serão:

- Flask
- SQLAlchemy
- OpenAPI3
- SQLite

### Machine Learning

- Scikit-learn

O modelo foi treinado utilizando o Google Colab. Para saber melhor o passo a passo do treinamento e sobre o modelo escolhido, acesso o notebook aqui: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raquelwainfas/MVP4-PUC-Rio/blob/main/ML_redwine.ipynb)

_Também há uma cópia neste repositório: MachineLearning > notebooks > ML_redwine.ipynb_

### Instalação

Para iniciar, é necessário instalar todas as bibliotecas Python listadas no arquivo `requirements.txt`. Após clonar o repositório, navegue até o diretório raiz usando o terminal para executar os comandos descritos abaixo.

Recomenda-se fortemente o uso de um ambiente virtual, como o `virtualenv`, para isolar as dependências do projeto.

1. **Instalando as Dependências**

   Execute o seguinte comando para instalar as bibliotecas necessárias:

   ```bash
   (env)$ pip install -r requirements.txt
   ```

    Este comando instalará todas as dependências especificadas no arquivo requirements.txt

2. **Executando o Servidor**

   Para iniciar a API, utilize o comando:
   
   ```bash
   (env)$ flask run --host 0.0.0.0 --port 5000
   ```

    Para o modo de desenvolvimento, é altamente recomendável adicionar o parâmetro `--reload`, que reiniciará automaticamente o servidor sempre que houver alterações no código-fonte:
   
   ```bash
   (env)$ flask run --host 0.0.0.0 --port 5000 --reload
   ```

3. **Acessando a API no Navegador**

   Após o servidor estar em execução, você pode verificar o status da API abrindo o seguinte endereço em seu navegador:

   ```bash
   http://localhost:5000
   ```
    Dessa forma, você poderá acompanhar a execução da API e verificar se está tudo funcionando corretamente.
