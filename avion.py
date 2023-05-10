class Avion:
    #Atributos
    __codigo = 0
    __nombre = ""
    __peso = 0

    #Método Constructor --> Construye al objeto
    def __init__(self,codigo,nombre,peso):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__peso=peso

    #Método destructor

    #Método STR()
    def __str__(self):
        return "Código:{} - Nombre:{} - Peso:{}Tn".format(self.__codigo,self.__nombre,self.__peso)
    #Otros Métodos
    def despegar(self):
        print("El avión esta despegando :)")