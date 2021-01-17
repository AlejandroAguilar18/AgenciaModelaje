from Empleados import Empleados
class Modelos(Empleados):
    def __init__(self,nombre="desconocido",salario=0,celular="desconocido",pasaporte="desconocido",paisOrigen="desconocido",
        fechaNacimiento="desconocida",colorOjos="desconocida",colorPiel="desconocido",estatura=0,medidaBusto=0,
        medidaCintura=0,medidas=[],tallaZapatos=0,peso=0,particularidades="desconocidos",
        nomDesfiles=[],nomAgencia="desconocidos",portafolio=[]):
        Empleados.__init__(self, nombre,salario,celular)
        self.pasaporte= pasaporte
        self.paisOrigen= paisOrigen
        self.fechaNacimiento=fechaNacimiento
        self.colorOjos= colorOjos
        self.colorPiel= colorPiel
        self.estatura= estatura
        self.medidaBusto= medidaBusto
        self.medidaCintura=medidaCintura
        self.medidas=medidas
        self.medidas.append(self.medidaBusto)
        self.medidas.append(self.medidaCintura)
        self.tallaZapatos=tallaZapatos
        self.peso= peso
        self.particularidades=particularidades
        self.nomDesfiles=nomDesfiles
        self.nomAgencia=nomAgencia
        self.portafolio= portafolio

    def getPasaporte(self):
        return self.pasaporte
    def setPasaporte(self,pasaporte):
        self.pasaporte= pasaporte

    def getPais(self):
        return self.pais
    def setPais(self, pais):
        self.pais= pais

    def getNacimiento(self):
        return self.fechaNacimiento
    def setNacimiento(self,fechaNacimiento):
        self.fechaNacimiento=fechaNacimiento

    def getOjos(self):
        return self.colorOjos
    def setOjos(self, colorOjos):
        self.colorOjos= colorOjos

    def getPiel(self):
        return self.colorPiel
    def setPiel(self,colorPiel):
        self.colorPiel= colorPiel

    def getEstatura(self):
        return self.estatura
    def setEstatura(self, estatura):
        self.estatura=estatura

    def getBusto(self):
        return self.medidaBusto
    def setBusto(self,medidaBusto):
        self.medidaBusto=medidaBusto

    def getCintura(self):
        return self.medidaCintura
    def setCintura(self,medidaCintura):
        self.medidaBusto=medidaCintura

    def getTalla(self):
        return self.tallaZapatos
    def setTalla(self,tallaZapatos):
        self.tallaZapatos=tallaZapatos

    def getPeso(self):
        return self.peso
    def setPeso(self,peso):
        self.peso = peso

    def getParticularidades(self):
        return self.particularidades
    def setParticularidades(self,particularidades):
        self.particularidades=particularidades

    def getDesfiles(self):
        return self.nomDesfiles
    def setDesfiles(self,*nomDesfiles):
        for i in nomDesfiles:
            self.nomDesfiles.append(i)

    def getAgencia(self):
        return self.nomAgencia
    def setAgencia(self,nomAgencia):
        self.nomAgencia=nomAgencia

    def aumentarBusto(self,aumento):
        self.medidaBusto+= aumento
    
    def aumentarCintura(self,aumento):
        self.medidaCintura+= aumento

    def disminuirCintura(self,dismi):
        self.medidaCintura-= dismi    

    def aumentarEstatura(self,aumento):
        self.estatura+= aumento

    def getPortafolio(self):
        return self.portafolio
    def setPortafolio(self,*portafolio):
        for i in portafolio:
            self.portafolio.append(i)

    def __str__(self):
        return f"Su nombre es: {self.nombre}\
            \nTiene un salario de: {self.salario}\
            \nSu celular es: {self.celular}\
            \nSu pasaporte es: {self.pasaporte}\
            \nSu pais de origen es: {self.paisOrigen}\
            \nNacio el: {self.fechaNacimiento}\
            \nSu color de ojos es: {self.colorOjos}\
            \nSu color de piel es: {self.colorPiel}\
            \nMide: {self.estatura}\
            \nLa medida de su busto es: {self.medidaBusto}\
            \nLa de su cintura es: {self.medidaCintura}\
            \nSus medidas en general son: {self.medidas}\
            \nSu talla de zapatos es: {self.tallaZapatos}\
            \nSu peso es: {self.peso}\
            \nSus particularidades son: {self.particularidades}\
            \nEl nombre del desfile que participa es: {self.nomDesfiles}\
            \nEl nombre de su agencia es: {self.nomAgencia}\
            \nTiene los portafolios: {self.portafolio}\
            \n_______________________________________________________________"