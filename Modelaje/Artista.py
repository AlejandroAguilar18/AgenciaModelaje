from Persona import Persona
class Artista(Persona):
    def __init__(self,nombre="desconocido",genero="desconocido",pertenece="desconocido"):
        Persona.__init__(self, nombre)
        self.genero= genero
        self.pertenece= pertenece
    
    def getGenero(self):
        return self.genero
    def setGenero(self,genero):
        self.genero = genero
    
    def getPertenece(self):
        return self.pertenece
    def setPertenece(self,pertenece):
        self.pertenece=pertenece
    
    def __str__(self):
        return f"{Persona.__str__(self)}\
        \n{self.nombre}\
        \nToca el genero: {self.genero}\
        \nPertenece a: {self.pertenece}\
        \n__________________________________"