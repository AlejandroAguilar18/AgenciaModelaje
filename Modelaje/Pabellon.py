class Pabellon:
    def __init__(self,nombre="desconocido",empleadoCargo="desconocido",telefono="desconocido",desfile="desconocido"):
        self.nombre = nombre
        self.empleadoCargo=empleadoCargo
        self.telefono= telefono
        self.desfile= desfile

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getEmpleadoCargo(self):
        return self.empleadoCargo
    def setEmpleadoCargo(self,empleadoCargo):
        self.empleadoCargo=empleadoCargo

    def getTelefono(self):
        return self.telefono
    def setTelefono(self,telefono):
        self.telefono= telefono

    def getDesfile(self):
        return self.desfile
    def setDesfile(self,desfile):
        self.desfile= desfile

    def __str__(self):
        return f"el pabellon se llama: {self.nombre}\
            \nTiene de empleado a cargo a: {self.empleadoCargo}\
            \nEl telefono del pabellon es: {self.telefono}\
            \n____________________________________________________"