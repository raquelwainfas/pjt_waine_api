import numpy as np
import pickle
import joblib
from model.preprocessador import PreProcessador
class Model:
    
    # TODO: Guardar model como atributo e o preditor receber as entradas.
    
    def carrega_modelo(path):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if path.endswith('.pkl'):
            with open(path, 'rb') as file:
                model = pickle.load(file)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model
    
    def realiza_predicao(model, X_input):
        """Realiza a predição do vinho com base no modelo treinado
        """
        diagnosis = model.predict(X_input)
        return diagnosis
