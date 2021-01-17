import random
class Evento:
    def __init__(self,desfiles=[],codigo="desconocido",nombre="desconocido",fechaInicio="desconocido",fechaFin="desconocido"):
        self.desfiles= desfiles
        self.codigo= random.randint(0,1000000)
        self.nombre = nombre
        self.fechaInicio= fechaInicio
        self.fechaFin= fechaFin
    
    def getDesfiles(self):
        return self.desfiles
    def setDesfiles(self, *desfiles):
        for i in desfiles:
            self.desfiles.append(i)
    
    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getInicio(self):
        return self.fechaInicio
    def setInicio(self, fechaInicio):
            self.fechaInicio

    def getFin(self):
        return self.fechaFin
    def setFin(self, fechaFin):
            self.fechaFin

    def __str__(self):
        return f"El evento se llama: {self.nombre}\
            \nTiene el codigo {self.codigo}\
            \nLos desfiles son: {self.desfiles}\
            \nEmpieza el {self.fechaInicio}\
            \nTermina el {self.fechaFin}\
            \n_________________________________________"