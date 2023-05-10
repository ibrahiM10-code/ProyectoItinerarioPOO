class Vuelo:
    __idVuelo=0
    __desc=""

    def __init__(self,idVuelo,desc):
        self.__idVuelo=idVuelo
        self.__desc=desc

    def __str__(self):
        return "Id Vuelo:{} - Descripción:{}".\
            format(self.__idVuelo,self.__desc)