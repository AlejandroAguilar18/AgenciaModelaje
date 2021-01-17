from Persona import Persona
class Empleados(Persona):
    def __init__(self,nombre="desconocido",salario=0,celular="desconocido"):
        Persona.__init__(self,nombre)
        self.salario = salario
        self.celular = celular

    def getSalario(self):
        return self.salario
    def setSalario(self,salario):
        self.salario=salario

    def getCelular(self):
        return self.celular
    def setCelular(self, celular):
        self.celular= celular

    def __str__(self):
        return f"{Persona.__str__(self)}\
            \nsu salario es: {self.salario}\
            \nsu celular es: {self.celular}"