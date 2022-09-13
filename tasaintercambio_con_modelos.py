from criptoexchange.models import Cambio, ModelError, TodoCoinAPIio
from config import apikey

todas = TodoCoinAPIio() # 1º Controlador pide a modelo: todas
todas.trae(apikey) 

print("{} de {}".format(len(todas.criptos), len(todas.criptos) + len(todas.no_criptos))) #{Todas las criptos} de {Todas las monedas, cripto y no cripto}

cripto = input("Introduzca una cripto conocida: ").upper() #2º Controlador pide a vista la cripto
while cripto != '':
    if cripto in todas.criptos:

        tipoCambio = Cambio(cripto) #Cada vez que queremos un tipo de cambio,se instancia con la Apikey
        try:
            tipoCambio.actualiza(apikey)
            print("{:.2f} €".format(tipoCambio.tasa))
        except ModelError as mensaje:
            print("Se ha producido el error {}".format(mensaje))
    
    cripto = input("Introduzca una cripto conocida: ").upper()
