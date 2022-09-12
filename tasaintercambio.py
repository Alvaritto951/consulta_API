from config import apikey

# https://requests.readthedocs.io/en/latest/ --- Guía a seguir
import requests

cripto = input("Introduzca una cripto conocida: ")
while cripto != "": #Si existe el tipo de criptomoneda que introduzcas, entra en el bucle
    if cripto.isalpha():
        r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(cripto, apikey))
        resultado = r.json() #json() sirve para convertir un texto en un diccionario
        if r.status_code == 200:
            print("{:.2f} €".format(resultado["rate"])) #Imprime el resultado con 2 decimales
        else:
            print(resultado["error"])

    cripto = input("Introduzca una cripto conocida: ")

# print(r.status_code) #Para ver si contiene errores
# print(r.text) --- Imprime el propio texto que devuelve la API


#r.headers['content-type']
#'application/json; charset=utf8'
#r.encoding
#'utf-8'
#r.text
#'{"type":"User"...'
#r.json()
#{'private_gists': 419, 'total_private_repos': 77, ...}
