import requests
import json
import random

class WineImageAPI:
    
    def __init__(self, url):
        self.__url = url

    def get_random_url(self):
        resultado = requests.get(self.__url)
        resultado = resultado.text

        lista_dicio = json.loads(resultado)

        lista_links = []
        for dicio in lista_dicio:
            lista_links.append(dicio['image'])

        random_image_url = random.choice(lista_links)
        return random_image_url
