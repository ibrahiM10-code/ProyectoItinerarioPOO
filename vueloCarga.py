from vuelo import Vuelo
class VueloCarga(Vuelo):
    __tipoCarga=""
    __pesoCarga=0

    def __init__(self,idVuelo,desc,tipoCarga,pesoCarga):
        super().__init__(idVuelo, desc)
        self.__tipoCarga=tipoCarga
        self.__pesoCarga=pesoCarga

    def __str__(self):
        res=super().__str__()+" - Tipo Carga:{} - Peso Carga:{} Kg".\
            format(self.__tipoCarga,self.__pesoCarga)
        return res
        #Al utilizar el super().__str__() no podemos retornarlo directamente y por eso lo guardamos en una variable
