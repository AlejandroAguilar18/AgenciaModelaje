class Portafolio:
    def __init__(self,fotos=[],objetivo="desconocido",anoCreacion="desconocido",numPortafolio="desconocido"):
        self.fotos=fotos
        self.objetivo= objetivo
        self.anoCreacion= anoCreacion
        self.numPortafolio= numPortafolio

    def getFotos(self):
        return self.fotos
    def setFotos(self,*fotos):
        for i in fotos:
            self.fotos.append(i)

    def getObjetivos(self):
        return self.objetivo
    def setObjetivos(self,objetivo):
        self.objetivo= objetivo

    def getCreacion(self):
        return self.anoCreacion
    def setCreacion(self,anoCreacion):
        self.anoCreacion=anoCreacion

    def getNumPortafolio(self):
        return self.numPortafolio
    def setNumPortafolio(self,numPortafolio):
        self.numPortafolio=numPortafolio

    def __str__(self):
        return f"las fotos del portafolio son: {self.fotos}\
            \nEl objetivo es: {self.objetivo}\
            \nFue creado el: {self.anoCreacion}\
            \nEl numero del portafolio es: {self.numPortafolio}"