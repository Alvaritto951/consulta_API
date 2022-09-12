""" Traerse todas las criptomonedas """
from config import apikey
# https://requests.readthedocs.io/en/latest/ --- Guía a seguir
import requests


class TodoCoinAPIio():
    def __init__(self): #Tienes que usar todas las apikeys
        self.criptos = [] #Criptomonedas
        self.no_criptos = [] #Monedas
    
    def trae(self, apikey): #Indicas cada vez la apikey
        r = requests.get("https://rest.coinapi.io/v1/assets?apikey={}".format(apikey)) #get es devolver
        if r.status_code != 200:  #Si es distinto a 200
            raise Exception("Error en consulta de assets: {}".format(r.status_code)) #Imprime el error indicando el número de r.status_code
        
        lista_candidatas = r.json() #Devuelve una lista de diccionarios que se puede procesar en Python
        for candidata in lista_candidatas: #Candidata es el diccionario de assets
            if candidata['type_is_crypto'] == 1: #bool(0) = False
                self.criptos.append(candidata['asset_id']) #asset_id es el identificador de moneda, solo nos interesan las criptos, es decir que el bool sea 1 (True)
            else:
                self.no_criptos.append(candidata['asset_id']) #Aquí incluye sólo las monedas, no las criptomonedas





"""
Ver qué cripto se elige

while cripto != '':
    if cripto in lista_definitiva:
        r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(cripto, apikey))
        resultado = r.json() #json() sirve para convertir un texto en un diccionario
"""