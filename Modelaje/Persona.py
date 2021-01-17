import random
class Persona:
    def __init__(self,nombre="desconocido"):
        self.nombre = nombre
        self.id = random.randint(0,10000000000)
        if self.nombre=="desconocido":
            self.nombre=str(self.id)
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getId(self):
        return self.id
    def __str__(self):
        return f"{self.nombre} y su ID es {self.id}."
