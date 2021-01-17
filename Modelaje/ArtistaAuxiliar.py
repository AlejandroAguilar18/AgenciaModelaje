from Artista import Artista
class ArtistaAuxiliar(Artista):
    def __init__(self,nombre="desconocido",genero="desconocido",pertenece="desconocido",banda="desconocido"):
        Artista.__init__(self, nombre, genero, pertenece)
        self.banda=banda

    def getBanda(self):
        return self.banda
    def setBanda(self, banda):
        self.banda = banda

    def __str__(self):
        return f"El artista se llama: {self.nombre}\
            \nToca el genero: {self.genero}\
            \nPerfetence a: {self.pertenece}\
            \nSu banda es {self.banda}\
            \n________________________________________"