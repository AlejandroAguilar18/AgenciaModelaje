class Grupo:
    def __init__(self,nombre="desconocido",integrantes=[]):
        self.nombre = nombre
        self.integrantes= integrantes

    def getIntegrantes(self):
        return self.integrantes
    def setIntegrantes(self, *integrantes):
        for i in integrantes:
            self.integrantes.append(i)

    def __str__(self):
        return f"el grupo se llama: {self.nombre}\
            \nTiene a los integrantes: {self.integrantes}.\
            \n______________________________________________"