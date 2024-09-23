from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, quality

class Vinho(Base):
    __tablename__ = 'vinhos'
    
    id = Column(Integer, primary_key=True)
    name = Column("name", String(100))
    fixed_acidity = Column("fixed_acidity", Float)
    volatile_acidity = Column("volatile_acidity", Float)
    citric_acid = Column("citric_acid", Float)
    residual_sugar = Column("residual_sugar", Float)
    chlorides = Column("chlorides", Float)
    free_sulfur_dioxide = Column("free_sulfur_dioxide", Integer)
    total_sulfur_dioxide = Column("total_sulfur_dioxide", Integer)
    density = Column("density", Float)
    pH = Column("pH", Float)
    sulphates = Column("sulphates", Float)
    alcohol = Column("alcohol", Float)
    quality = Column("quality", Integer, nullable=True)
    image_url = Column("img_url", String(200), nullable=True)
    
    def __init__(self, image_url:str, name:str, fixed_acidity:float, volatile_acidity:float, citric_acid:float, 
                 residual_sugar:float, chlorides:float, free_sulfur_dioxide:int, 
                 total_sulfur_dioxide:int, density:float, pH:float, sulphates:float, alcohol:float, quality:int):

        self.image_url = image_url
        self.name=name
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol = alcohol
        self.quality = quality