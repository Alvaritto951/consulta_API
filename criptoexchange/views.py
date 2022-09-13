def pideCripto():
    cripto = input("Introduzca una cripto conocida: ").upper()
    return cripto

def mostrarTipoCambio(tasa): #Hace la conversión de la tasa
    print("{:.2f} €".format(tasa))

def mostrarError(mensaje):
    print("Se ha producido el error {}".format(mensaje))