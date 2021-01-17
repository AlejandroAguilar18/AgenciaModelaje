import random
class Agencia:
    def __init__(self,nombre="desconocido",modelos=[],paisCede="desconocido",codigo="desconocido",anoCreacion="desconocido",
        correo="desconocido",dueno="desconocido"):
        self.nombre = nombre
        self.modelos= modelos
        self.paisCede= paisCede
        self.codigo= random.randint(0,10000000000)
        self.anoCreacion= anoCreacion
        self.correo=correo
        self.dueno=dueno

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getModelos(self):
        return self.modelos
    def setModelos(self,*modelos):
        for i in modelos:
            self.modelos.append(i)

    def getCede(self):
        return self.paisCede
    def setCede(self,paisCede):
        self.paisCede= paisCede

    def getCodigo(self):
        return self.codigo

    def getCreacion(self):
        return self.anoCreacion
    def setCreacion(self,anoCreacion):
        self.anoCreacion=anoCreacion

    def getCorreo(self):
        return self.correo
    def setCorreo(self, correo):
        self.correo= correo

    def getDueno(self):
        return self.dueno
    def setDueno(self, dueno):
        self.dueno= dueno

    def __str__(self):
        return f"La agencia se llama: {self.nombre}\
            \nSu codigo es: {self.codigo}\
            \nTiene las modelos: {self.modelos}\
            \nLa cede principal queda en: {self.paisCede}\
            \nEl codigo es: {self.codigo}\
            \nFue creada el: {self.anoCreacion}\
            \nEl correo es: {self.correo}\
            \nSu dueño es: {self.dueno}."