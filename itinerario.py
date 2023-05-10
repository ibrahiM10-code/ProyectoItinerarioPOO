from avion import Avion
class Itinerario:
    __idItinerario = 0
    __origen = ""
    __destino = ""
    __fecha = ""
    __elAvion = Avion(0,"",0) #Creamos objeto en blanco.
    __listaVuelos = []

    def __init__(self, idItinerario, origen, destino, fecha, elAvion, vuelo):
        self.__idItinerario = idItinerario
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__elAvion = elAvion
        Itinerario.__listaVuelos.append(vuelo) #Añadimos los objetos de tipo vuelo a la lista

    def __str__(self):
        return "Id Itinerario:{}\n Origen:{}\n Destino:{}\n Fecha:{}".\
            format(self.__idItinerario,self.__origen,self.__destino,self.__fecha)

    def mostrarAvion(self):
        print(self.__elAvion)

    def mostrarListaVuelos(self):
        for vuelo in self.__listaVuelos:
            print(vuelo) #Muestra los vuelos que hay en la lista.

    def addVuelo(self,vuelo):
        self.__listaVuelos.append(vuelo) #Este metodo nos permite añadir más vuelos a la lista, ya que sin este
                                         #solo podemos añadir uno.
        print(self.__listaVuelos)