from avion import Avion
from  vueloPasajero import VueloPasajero
from vueloCarga import VueloCarga
from itinerario import Itinerario

#Creación de los objetos
avion1=Avion(2029, "Boeing 243", 4.1)
avion2=Avion(2030,"Boeing456",3.5)
print("**************************** Aviones ************************************")
print("Avión 1:\n",avion1)
avion1.despegar()
print("Avión 2:\n",avion2)

print("********************** Vuelos ***************************")
vueloP1=VueloPasajero(100,"Charter Privado",120)
vueloP2=VueloPasajero(200,"Comercial",250)

vueloC1=VueloCarga(800,"Vuelo Peligroso","Explosivos",2300)
vueloC2=VueloCarga(900,"Zoo","Elefantes",9800)

print("Vuelo Pasajeros 1:\n",vueloP1)
print("Vuelo Pasajeros 2:\n",vueloP2)
print("Vuelo Carga 1:\n",vueloC1)
print("Vuelo Carga 2:\n",vueloC2)

print("******************** Crear Itinerario ************************")
itinerario1=Itinerario(1200,"La Serena","Santiago","25/10/2022",avion1,vueloP1)
#Uso de los métodos de la clase Itinerario.
itinerario1.addVuelo(vueloP2)
itinerario1.addVuelo(vueloC1)
itinerario1.addVuelo(vueloC2)

print("Itinerario 1:\n",itinerario1)
print("Datos del Avión: \n")

itinerario1.mostrarAvion()

print("Vuelos Asociados:\n")
itinerario1.mostrarListaVuelos()
