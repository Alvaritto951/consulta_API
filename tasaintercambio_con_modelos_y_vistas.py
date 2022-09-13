from criptoexchange.models import Cambio, ModelError, TodoCoinAPIio
from criptoexchange.views import mostrarError, mostrarTipoCambio, pideCripto
from config import apikey

todas = TodoCoinAPIio() # 1º Controlador pide a modelo: todas
todas.trae(apikey) 

#print("{} de {}".format(len(todas.criptos), len(todas.criptos) + len(todas.no_criptos))) #{Todas las criptos} de {Todas las monedas, cripto y no cripto}

cripto = pideCripto() #2º Controlador pide a vista la cripto

while cripto != '': #3º Controlador le indica a modelo que calcule la tasa y a vista que imprima la tasa
    if cripto in todas.criptos:
        tipoCambio = Cambio(cripto) #Cada vez que queremos un tipo de cambio,se instancia con la Apikey
        try:
            tipoCambio.actualiza(apikey)
            mostrarTipoCambio(tipoCambio.tasa)
        except ModelError as mensaje:
            mostrarError(mensaje)
    
    cripto = pideCripto()
