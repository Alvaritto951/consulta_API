#15913 de 16132 (219)
import pytest
from criptoexchange.models import ModelError, TodoCoinAPIio, Cambio
from config import apikey

def test_Todocoin():
    todas = TodoCoinAPIio() #todas es igual a la clase TodoCoinAPIio
    assert isinstance(todas, TodoCoinAPIio) #comprobamos que la variable es del tipo de la clase TodoCoinAPIio
    todas.trae(apikey) #Instancias la apikey
    assert len(todas.criptos) == 15913
    assert len(todas.no_criptos) == 220


def test_Cambio():
    btcEur = Cambio("BTC") #Se comprueba, por ejemplo, el bitcoin dentro de la clase Cambio
    assert btcEur.tasa is None
    assert btcEur.horafecha is None
    btcEur.actualiza(apikey) #Se introduce la apikey en el método actualiza para la variable btcEur
    assert btcEur.tasa > 0 #Se comprueba que la tasa es superior a 0
    assert isinstance(btcEur.horafecha, str) #Se comprueba si la variable es del tipo cadena


def test_cambio_no_ok():
    noOK = Cambio("KKTUA")
    assert noOK.tasa is None
    assert noOK.horafecha is None

    #Hay que alzar el error con raise ModelError con pytest (importar pytest)
    
    with pytest.raises(ModelError) as exceptionInfo:
        noOK.actualiza(apikey) #De esta forma me tira fallo pero no sé qué tipo de fallo, está hecho de una forma general --- Es mejor este método
    assert "550" in str(exceptionInfo.value)
    
    """ Otra forma
    with pytest.raises(ModelError) as exceptionInfo: #ModelError viene importado de tasaintercambio_con_modelos
        noOK.actualiza(apikey) #Se introduce la apikey en el método actualiza para la variable btcEur
    assert str(exceptionInfo.value) == "550: You requested specific single item that we don't have at this moment."
    """