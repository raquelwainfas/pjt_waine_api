from pydantic import BaseModel
from typing import Optional, List
from model.vinho import Vinho
import json
import numpy as np

class VinhoSchema(BaseModel):
    """ Define como um novo vinho a ser inserido deve ser representado
    """
    name: str = "Vinho do Porto"
    fixed_acidity: float = 7.7
    volatile_acidity: float = 0.26
    citric_acid: float = 0.26
    residual_sugar: float = 2  
    chlorides: float = 0.052
    free_sulfur_dioxide: int = 19 
    total_sulfur_dioxide: int = 77 
    density: float = 0.9951
    pH: float = 3.15
    sulphates: float = 0.79
    alcohol: float = 10.9

class VinhoViewSchema(BaseModel):
    """Define como os dados físico-químicos do vinho será retornado
    """
    id: int = 1
    name:str = 'Vinho do Porto',
    fixed_acidity: float = 7.7 
    volatile_acidity: float = 0.26
    citric_acid: float = 0.26
    residual_sugar: float = 2  
    chlorides: float = 0.052
    free_sulfur_dioxide: int = 19 
    total_sulfur_dioxide: int = 77 
    density: float = 0.9951
    pH: float = 3.15
    sulphates: float = 0.79
    alcohol: float = 10.9
    quality: int = None
    
class VinhoBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do vinho.
    """
    name: str = "Vinho do Porto"

class ListaVinhosSchema(BaseModel):
    """Define como uma lista de vinhos será representada
    """
    vinhos: List[VinhoSchema]

    
class VinhoDelSchema(BaseModel):
    """Define como o vinho para deleção será representado
    """
    name: str = "Vinho do Porto"
    
# Apresenta apenas os dados de um vinho    
def apresenta_vinho(vinho: Vinho):
    """ Retorna uma representação do vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    return {
        "id": vinho.id,
        "name": vinho.name,
        "fixed_acidity": vinho.fixed_acidity,
        "volatile_acidity": vinho.volatile_acidity,
        "citric_acid": vinho.citric_acid,
        "residual_sugar": vinho.residual_sugar,
        "chlorides": vinho.chlorides,
        "free_sulfur_dioxide": vinho.free_sulfur_dioxide,
        "total_sulfur_dioxide": vinho.total_sulfur_dioxide,
        "density": vinho.density,
        "pH": vinho.pH,
        "sulphates": vinho.sulphates,
        "alcohol": vinho.alcohol,
        "quality": vinho.quality
    }
    
# Apresenta uma lista de vinhos
def apresenta_vinhos(vinhos: List[Vinho]):
    """ Retorna uma representação do vinho seguindo o schema definido em
        VinhoViewSchema.
    """
    result = []
    for vinho in vinhos:
        result.append({
            "id": vinho.id,
            "name": vinho.name,
            "fixed_acidity": vinho.fixed_acidity,
            "volatile_acidity": vinho.volatile_acidity,
            "citric_acid": vinho.citric_acid,
            "residual_sugar": vinho.residual_sugar,
            "chlorides": vinho.chlorides,
            "free_sulfur_dioxide": vinho.free_sulfur_dioxide,
            "total_sulfur_dioxide": vinho.total_sulfur_dioxide,
            "density": vinho.density,
            "pH": vinho.pH,
            "sulphates": vinho.sulphates,
            "alcohol": vinho.alcohol,
            "quality": vinho.quality
        })

    return {"vinhos": result}

