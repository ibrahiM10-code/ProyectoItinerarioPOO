from vuelo import Vuelo
class VueloPasajero(Vuelo):
    __cantPasajeros=0

    def __init__(self,idVuelo,desc,cantPasajeros):
        #El operador Super, permite invocar o llamar o acceder a los métodos y/o atributos del Padre
        super().__init__(idVuelo,desc)
        self.__cantPasajeros=cantPasajeros

    def __str__(self):
        res=super().__str__()+" - Cant. Pasajeros:{}".\
            format(self.__cantPasajeros)
        return res