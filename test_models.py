#15913 de 16132 (219)
from criptoexchange.models import TodoCoinAPIio
from config import apikey

def test_Todocoin():
    todas = TodoCoinAPIio() #todas es igual a la clase TodoCoinAPIio
    assert isinstance(todas, TodoCoinAPIio) #comprobamos que la variable es del tipo de la clase TodoCoinAPIio
    todas.trae(apikey) #Instancias la apikey
    assert len(todas.criptos) == 15913
    assert len(todas.no_criptos) == 219
