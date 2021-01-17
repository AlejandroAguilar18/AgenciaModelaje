from Artista import Artista
from Artista import Artista
class ArtistaContrato(Artista):
    def __init__(self,nombre="desconocido",genero="desconocido",pertenece="desconocido",pago=0,desfile="desconocido"):
        Artista.__init__(self,nombre,genero,pertenece)
        self.pago=pago
        self.desfile=desfile
    
    def getPago(self):
        return self.pago
    def setPago(self,pago):
        self.pago=pago

    def getDesfile(self):
        return self.desfile
    def setDesfile(self,desfile):
        self.desfile=desfile

    def __str__(self):
        return f"El artista: {self.nombre}\
            \nGenero: {self.genero}\
            \nPerfetence a: {self.pertenece}\
            \nSu paga es de: {self.pago}\
            \nSu desfile es: {self.desfile}\
            \n__________________________________"