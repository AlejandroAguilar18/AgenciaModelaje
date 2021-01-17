from Empleados import Empleados
class Disenador(Empleados):
    def __init__(self,nombre="desconocido",salario=0,desfile=[],pasaporte="desococido",paisOrigen="desconocido"):
        Empleados.__init__(self, nombre,salario)
        self.desfile= desfile
        self.pasaporte=pasaporte
        self.paisOrigen= paisOrigen

    def getOrigen(self):
        return self.paisOrigen
    def setOrigen(self,paisOrigen):
        self.paisOrigen= paisOrigen

    def getPasaporte(self):
        return self.pasaporte
    def setPasaporte(self,pasaporte):
        self.pasaporte= pasaporte

    def vincularDesfiles(self,*nombreDesfile):
        for i in nombreDesfile:
            self.desfile.append(i)

    def __str__(self):
        return f"{Empleados.__str__(self)}\
            \nEl nombre de los desfiles son: {self.desfile}\
            \nSu pasaporte es: {self.pasaporte}\
            \nSu país de origen es: {self.paisOrigen}\
            \n_____________________________________________________"