from Evento import Evento
class Desfile(Evento):
    def __init__(self,codigo="desconocido",modelos=[],fecha="desconocido",hora="desconocido",nomColeccion="desconocido"):
        Evento.__init__(self,codigo)
        self.modelos=modelos
        self.fecha= fecha
        self.hora= hora
        self.nomColeccion= nomColeccion

    def getModelos(self):
        return self.modelos
    def setModelos(self,*modelos):
        for i in modelos:
            self.modelos.append(i)

    def getFecha(self):
        return self.fecha
    def setFecha(self, fecha):
        self.fecha= fecha

    def getHora(self):
        return self.hora
    def setHora(self, hora):
        self.hora = hora

    def getColeccion(self):
        return self.nomColeccion
    def setColeccion(self,nomColeccion):
        self.nomColeccion= nomColeccion
    
    def __str__(self):
        return f"El codigo del evento es: {self.codigo}\
            \nLas modelos que participan son: {self.modelos}\
            \nLa fecha va a ser: {self.fecha} a las {self.hora}\
            \nEl nombre de la colecciona a exponer es: {self.nomColeccion}\
            \n_________________________________________________________________"