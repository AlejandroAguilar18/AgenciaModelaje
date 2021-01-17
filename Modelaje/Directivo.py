from Empleados import Empleados
class Directivo(Empleados):
    def __init__(self,nombre="desconocido",salario=0,celular="desconocido",profesional="desconocido",universidad="desconocida",
        evento="desconocido"):
        Empleados.__init__(self, nombre, salario, celular)
        self.profesional= profesional
        self.universidad= universidad
        self.evento= evento

    def getEvento(self):
        return self.evento
    def setEvento(self,evento):
        self.evento= evento

    def getProfesional(self):
        return self.profesional
    def setProfesional(self,profesional):
        self.profesional=profesional

    def getUniversidad(self):
        return self.universidad
    def setUniversidad(self,universidad):
        self.universidad=universidad

    def vincularEvento(self,evento):
        self.evento = evento

    def __str__(self):
        return f"{Empleados.__str__(self)}\
            \nEvento asigado: {self.evento}\
            \nEs egresado de la universidad: {self.universidad}\
            \n___________________________________________________"
