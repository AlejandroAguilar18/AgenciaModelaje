print("------------------------------------")
print("-----  Alejandro Aguilar UJTL  -----")
print("------------------------------------")
from Pabellon import Pabellon
from ArtistaContrato import ArtistaContrato
from Agencia import Agencia
from Modelos import Modelos
from Portafolio import Portafolio
from Pabellon import Pabellon
from Grupo import Grupo
from Evento import Evento
from Disenador import Disenador
from Directivo import Directivo
from Desfile import Desfile
from Artista import Artista
from ArtistaAuxiliar import ArtistaAuxiliar
from Empleados import Empleados
diseñadores=[]
disenador1=Disenador("juan",2000000,["hot","invierto"],"124536","venezuela")
disenador2=Disenador("jose",9000000,["primavera","otoño"],"354820","colombia")
disenador3=Disenador("fernando",1000000,["chontaduro","banana"],"930152","egipto")
diseñadores.append(disenador1)
diseñadores.append(disenador2)
diseñadores.append(disenador3)

modelos=[]
modelo1=Modelos("jhuliana",2000000,3102699010,82573,"italia","11/junio/2002","verdes","blanca",160,70,60,[70,60],36,50,"inteligente"
,["historiadores","Mundo arte"],"Historicos",["arte moderno","arte clasico"])
modelo2=Modelos("alejandra",700000,3102670542,930411,"francia","18/julio/2000","azules","blanca",170,90,60,[90,60],38,45,"voluptuosa"
,["gran mundo","veraneo"],"eco moda",["bikini","casa"])
modelo3=Modelos("darcy",500000,3156745324,34601,"colombia","25/marzo/1997","cafes","morena",175,80,70,[80,70],34,38,"divertida"
,["clareto","marineo"],"middles",["verano caliente","arte golosal"])
modelos.append(modelo1)
modelos.append(modelo2)
modelos.append(modelo3)

rasos=[]
raso1=Empleados("damiam",27890,3124576804)
raso2=Empleados("ozuna",63048,3208867413)
raso3=Empleados("andres",123421,3124576804)
rasos.append(raso1)
rasos.append(raso2)
rasos.append(raso3)

directivos=[]
directivo1=Directivo("pepinilo",12587,3408642121,"si","UJTL","chupemestepenco")
directivo2=Directivo("victor",0,3125678977,"si","andes","dame mas plata")
directivo3=Directivo("kevin",900000,3124358635,"no","la vida","agt roma")
directivos.append(directivo1)
directivos.append(directivo2)
directivos.append(directivo3)

artistas=[]
artista1=Artista("pepito","merengue","nada")
artista2=Artista("william","regueton","banda")
artista3=Artista("pedro","opera","banda")
artistas.append(artista1)
artistas.append(artista2)
artistas.append(artista3)

agencias=[]
agencia1=Agencia("dominico",["no hay"],"venezuela",13642,"21/noviembre/2000","valepito@gmail.com","sebastino")
agencia2=Agencia("mala mia",["baby1","baby2","baby3","baby4"],"colombia",13764,"18/febrero/2002","preattyboy@gmail.com","maluma")
agencia3=Agencia("conejillos",["tu ex"],"venezuela",93120,"29/mayo/2012","todaviatequiero@gmail.com","bad bunny")
agencias.append(agencia1)
agencias.append(agencia2)
agencias.append(agencia3)

artistasContrato=[]
artistaC1=ArtistaContrato("jose","rock","beattles",20000,"con gusto")
artistaC2=ArtistaContrato("marico","bachata","bachateros",50000,"pegadito")
artistaC3=ArtistaContrato("alejandro","reggae","marihuanos",100000,"a volar")
artistasContrato.append(artistaC1)
artistasContrato.append(artistaC2)
artistasContrato.append(artistaC3)

artistasAuxiliar=[]
artistaA1=ArtistaAuxiliar("juanito","merengue","ninguna","solista")
artistaA2=ArtistaAuxiliar("el pepe","salsa","banda","muchachines")
artistaA3=ArtistaAuxiliar("ete sech","regueton","ninguna","solista")
artistasAuxiliar.append(artistaA1)
artistasAuxiliar.append(artistaA2)
artistasAuxiliar.append(artistaA3)

eventos=[]
evento1=Evento(["jijiji","already"],12943,"Viveres","2/noviembre/2021","3/noviembre/2021")
evento2=Evento(["fucked","gooo"],13975,"añoros","9/julio/2019","10/julio/2019")
evento3=Evento(["me quiero matar","viancias"],37961,"triste","30/marzo/2020","31/marzo/2020")
eventos.append(evento1)
eventos.append(evento2)
eventos.append(evento3)

desfiles=[]
desfile1=Desfile("321654",["juliana","andrea","maria"],"12/octubre/2020","5:30","jugueteo")
desfile2=Desfile("653015",["valentina","juliana","gabriela"],"22/agosto/2020","7:30","verano americano")
desfile3=Desfile("982305",["daniela","sharon","camila"],"30/diciembre/2020","10:30","nuevos años")
desfiles.append(desfile1)
desfiles.append(desfile2)
desfiles.append(desfile3)

pabellones=[]
pabellon1=Pabellon("victorino","juan",3222241404,desfile1.setDesfiles)
pabellon2=Pabellon("aureliano","david",3213638470,desfile3.setDesfiles)
pabellon3=Pabellon("padilla","mateo",3124805417,desfile3.setDesfiles)
pabellones.append(pabellon1)
pabellones.append(pabellon2)
pabellones.append(pabellon3)

portafolios=[]
portafolio1=Portafolio(["mama","papa","hermano"],"verano","22/septiembre/2018",12543)
portafolio2=Portafolio(["tia","tio","hermana"],"invierno","20/junio/2017",35402)
portafolio3=Portafolio(["primo","prima","sobrino"],"otoño","21/julio/2017",93106)
portafolios.append(portafolio1)
portafolios.append(portafolio2)
portafolios.append(portafolio3)

bandas=[]
banda1=Grupo("sad",["mateo","diego","david"])
banda2=Grupo("funnyest",["sergio","sebastian","daniel"])
banda3=Grupo("bilini",["pablo","merchan","frederick"])
bandas.append(banda1)
bandas.append(banda2)
bandas.append(banda3)

z=1
while z==1:
    print("__________________________")
    print(" ")
    print("******The Star Rover******")
    print("__________________________")
    print("")
    print("------------------------------------------")
    print("-----      ¿Que deseas hacer?        -----")
    print("------------------------------------------")
    print("-----    1.Contrtar empleados        -----")#Este ya
    print("-----    2.Crear un evento           -----")#Este ya
    print("-----    3.Contratar un artista      -----")#Este ya
    print("-----    4.Mostar datos de empresa   -----")#Este ya
    print("-----    5.Despedir                  -----")#Este ya
    print("-----    6.Crear una banda           -----")#Este ya
    print("-----    7.Crear portafolio          -----")#Este ya
    print("-----    8.Crear Agencia             -----")#Este ya
    print("-----    9.Asignarciones             -----")
    print("-----    10.Salir del programa        -----")#Este ya
    print("------------------------------------------")
    opcion1=int(input())
    print("----------------------------------")
    if opcion1==1:
        print("¿Que trabajador desea contratar?")
        print("Diseñador(1)\
            \nModelo(2)\
            \nDirectivo(3)\
            \nRaso(4)")
        print("----------------------------------")
        opcion2=int(input())
        print("----------------------------")
        if opcion2==1:
            diseñador=Disenador()
            print("Muy bien necesito que me des unos datos")
            nombre=input("Nombre: ")
            diseñador.vincularDesfiles("Ninguno")
            diseñador.setSalario("no tiene")
            celular=input("Celular: ")    
            pasaporte=input("Pasaporte: ")
            paisOrigen=input("Pais origen: ")
            diseñador.setNombre(nombre)
            diseñador.setPasaporte(pasaporte)
            diseñador.setOrigen(paisOrigen)
            diseñador.setCelular(celular)
            diseñadores.append(diseñador)
            print(f"Contrtaste a {diseñador}")
        elif opcion2==2:
            print("Seguro? es mucha informacion")
            opcion7=input("(Y/N)")
            print("----------------------------")
            if opcion7.upper()=="Y":
                modelo=Modelos()
                nombre=input("Nombre: ")
                celular=input("Celular: ")
                pasaporte=input("Pasaporte: ")
                paisOrigen=input("Pais origen: ")
                fechaNacimiento=input("Fecha nacimiento: ")
                colorOjos=input("Color de ojos: ")
                colorPiel=input("Color de piel: ")
                estatura=int(input("Estatura: "))
                medidaBusto=int(input("Busto: "))
                medidaCintura=int(input("Cintura: "))
                medidas=[medidaBusto,medidaCintura]
                tallaZapatos=int(input("Talla zapatos: "))
                peso=int(input("Peso: "))
                particularidades=input("Particularidades: ")
                nomDesfiles=("Ninguno")
                nomAgencias=("Ninguna")
                portafolio=("No asignados")
                modelo.setNombre(nombre)
                modelo.setCelular(celular)
                modelo.setPasaporte(pasaporte)
                modelo.setPais(paisOrigen)
                modelo.setNacimiento(fechaNacimiento)
                modelo.setOjos(colorOjos)
                modelo.setPiel(colorPiel)
                modelo.setEstatura(estatura)
                modelo.setBusto(medidaBusto)
                modelo.setCintura(medidaCintura)
                modelo.setTalla(tallaZapatos)
                modelo.setPeso(peso)
                modelo.setParticularidades(particularidades)
                modelos.append(modelo)
                print(f"Contrtaste a {modelo}")
            elif opcion7.upper()=="N":
                print("Floj@")
        elif opcion2==3:
            print("Deseas contrtar un directivo")
            print("Dame los datos")
            directivo=Directivo()
            nombre=input("Nombre: ")
            celular=input("Celular: ")
            profesional=input("Es profesional?(Y/N): ")
            if profesional.upper()=="Y":
                profesional="Si"
                universidad=input("Universidad que egreso: ")
            elif profesional.upper()=="N":
                profesional="No"
                universidad="No tuvo"
            directivo.setNombre(nombre)
            directivo.setCelular(celular)
            directivo.setProfesional(profesional)
            directivo.setUniversidad(universidad)
            directivos.append(directivo)  
            print(f"Contrtaste a {directivo}")        
        elif opcion2==4:
            print("Necesito que me des unos datos")
            raso=Empleados()
            nombre=input("Nombre: ")
            salario=int(input("Pago: "))
            celular=input("Celular: ")
            raso.setNombre(nombre)
            raso.setCelular(celular)
            raso.setSalario(salario)
            rasos.append(raso)
            print(f"Contrtaste a {raso}")
    elif opcion1==2:
        evento=Evento()
        print("Que quieres crear?")
        print("Evento general(1)\
            \nDesfile(2)\
            \npabellon(3)")
        print("----------------------------------")
        opcion10=int(input())
        print("----------------------------------")
        if opcion10==1:
            codigo=input("Codigo: ")
            nombre=input("Nombre: ")
            fechaInicio=input("Fecha de inicio: ")
            fechaFinal=input("Fecha de finalizacion: ")
            a=int(input("Cuantos desfiles quieres meter al evento?"))
            if 1<=a<=10:
                for i in range(0,a):
                    nom=input(f"Dime el nombre del desfile n°{i+1}:")
                    evento.setDesfiles(nom)
            else:
                print("Opcion invalida, continuemos")
            evento.setNombre(nombre)
            evento.setInicio(fechaInicio)
            evento.setFin(fechaFinal)
            print(f"Has creado el evento {evento}")
            eventos.append(evento)
        if opcion10==2:
            desfile=Desfile()
            print("Muy bien, regaleme unos datos para crear el desfile")
            fecha=input("Fecha: ")
            hora=input("Hora: ")
            nomColeccion=("Nombre de la coleccion: ")
            desfile.setFecha(fecha)
            desfile.setHora(hora)
            desfile.setColeccion(nomColeccion)
            if len(modelos)==0:
                print("No hay modelos disponibles, ve y contrata algunas")
                desfile.setModelos("No hay")
            elif len(modelos)>=1:
                j=1
                print("Decide que modelo quieres vincular")
                for i in modelos:
                    print(f"{j}.{i}")
                    j+=1
                n=int(input())
                desfile.setModelos(modelos[n])
        if opcion10==3:
            pabellon=Pabellon()
            print("Muy bien, regaleme unos datos para crear el pabellon")
            nombre=input("Nombre: ")
            telefono=input("Telefono: ")
            if len(desfiles)==0:
                print("No hay desfiles para vincular a este pabellon")
                pabellon.setDesfile("No hay ninguno")
            else:
                j=1
                print("Decide que desfile quieres vincular")
                for i in desfiles:
                    print(f"{j}.{i}")
                    j+=1
                n=int(input())
                pabellon.setDesfile(desfiles[n])
            pabellon.setNombre(nombre)         
            pabellon.setTelefono(telefono)
            if len(directivos)==0:
                print("No hay directivos para vincular a este pabellon")
                pabellon.setEmpleadoCargo("No hay ninguno disponible")
            else:
                k=1
                print("Decide que empleado quieres colocar a cargo")
                for i in directivos:
                    print(f"{k}.{i}")
                    j+=1
                n=int(input())
                pabellon.setEmpleadoCargo(directivos[n])
    elif opcion1==3:
        print("Deseas contrtar un artista")
        print("Que tipo de artista quieres contrtar?")
        print("Normal(1)\
            \nAuxiliar(2)")
        print("----------------------------------")
        opcion6=int(input())
        print("----------------------------------")
        if opcion6==1:
            print("Necesito que me digas sus datos")
            artista=ArtistaContrato()
            nombre=input("Nombre: ")
            genero=input("Genero: ")
            pertenece=input("Banda a la que pertenece: ")
            if len(desfiles)==0:
                print("No hay desfiles para vincular a este pabellon")
                artista.setDesfile("No hay ninguno")
            else:
                j=1
                print("Decide que desfile quieres vincular")
                for i in desfiles:
                    print(f"{j}.{i}")
                    j+=1
                n=int(input())
                artista.setDesfile(desfiles[n])
            pago=int(input("Pago por el desfile: "))
            artista.setNombre(nombre)
            artista.setGenero(genero)
            artista.setPertenece(pertenece)
            artista.setPago(pago)
            artistasContrato.append(artista)
            artistas.append(artista)
            print(f"Has creado al artista {artista}")
        elif opcion6==2:
            print("Necesito que me digas sus datos")
            artista=ArtistaContrato()
            nombre=input("Nombre: ")
            genero=input("Genero: ")
            pertenece=input("pertenece a una banda o esta solo(B/S): ")
            if pertenece.upper()=="B":
                pertenece="Banda"
                banda=input("Banda a la que pertenece: ")
                bandas.append(banda)
            elif pertenece.upper()=="S":
                pertenece="Solo"
                banda="No pertenece a ninguina banda"
            artista.setNombre(nombre)
            artista.setGenero(genero)
            artista.setPertenece(pertenece)
            artistasAuxiliar.append(artista)
            artistas.append(artista)
            print(f"Has creado al artista {artista}")
    elif opcion1==4:        
        print("Que deseas ver")
        print("Empleados(1)\
            \nArtistas(2)\
            \nEventos(3)")
        print("----------------------------------")
        opcion4=int(input())
        print("----------------------------------")
        if opcion4==1:
            print("Que empleados deseas ver?")
            print("Modelos(1)\
                \nDiseñadores(2)\
                \nDirectivos(3)\
                \nRasos(4)")
            print("----------------------------------")    
            opcion3=int(input())
            print("----------------------------------")
            if opcion3==1:
                if len(modelos)==0:
                    print("No hay modelos")
                else:
                    print("Estas son las modelos")
                    print("----------------------------------")
                    for i in modelos:
                        print(i)
            elif opcion3==2:
                if len(diseñadores)==0:
                    print("No hay diseñadores")
                else:
                    print("Estos son los diseñadores")
                    print("----------------------------------")
                    for i in diseñadores:
                        print(i)
            elif opcion3==3:
                if len(directivos)==0:
                    print("No hay directivos")
                    print("----------------------------------")
                else:
                    print("Estos son los directivos")
                    for i in directivos:
                        print(i)
            elif opcion3==4:
                if len(rasos)==0:
                    print("No hay empleados rasos")
                else:
                    print("Estos son los empleados rasos")
                    print("----------------------------------")
                    for i in rasos:
                        print(i)
        elif opcion4==2:
            print("Que artistas deseas ver?")
            print("Todos los artistas(1)\
                \nArtistas de contrato(2)\
                \nArtistas auxiliares(3)")
            print("----------------------------------")
            opcion5=int(input())
            print("----------------------------------")
            if opcion5==1:
                if len(artistas)==0:
                    print("No han habido artistas")
                else:
                    print("Estos todos los artistas que han pasado por tu agencia")
                    print("------------------------------------------------------")
                    for i in artistas:
                        print(i)
            elif opcion5==2:
                if len(artistasContrato)==0:
                    print("No han habido artistas de contrato")
                else:
                    print("Estos son los artistas que has contrtado")
                    print("----------------------------------------")
                    for i in artistasContrato:
                        print(i)
            elif opcion5==3:
                if len(artistasAuxiliar)==0:
                    print("No han habido artistas auxiliares")
                else:
                    print("Estos son los artistas que se contrataron pero son parte de una banda")
                    print("---------------------------------------------------------------------")
                    for i in artistasAuxiliar:
                        print(i)
        elif opcion4==3:
            print("Que Eventos deseas ver?")
            print("Eventos generales(1)\
                \nDesfiles(2)\
                \nPabellones(3)")
            print("----------------------------------")
            opcion3=int(input())
            print("----------------------------------")
            if opcion3==1:
                if len(eventos)==0:
                    print("No hay eventos")
                else:
                    print("Estos son todos los eventos")
                    print("----------------------------------")
                    for i in eventos:
                        print(i)
            elif opcion3==2:
                if len(desfiles)==0:
                    print("No hay desfiles")
                else:
                    print("Estos son los desfiles")
                    print("----------------------------------")
                    for i in desfiles:
                        print(i)
            elif opcion3==3:
                if len(pabellones)==0:
                    print("No hay pabellones")
                else:
                    print("Estos son los pabellones")
                    print("----------------------------------")
                    for i in pabellones:
                        print(i)
    elif opcion1==5:
        print("Seguro? tienen famila")
        opcion8=input("(Y/N)")
        if opcion8.upper()=="Y":
            print("Que mal ser vivo eres, pero bueno, continuemos")
            print("En que area deseas depedir")
            print("Diseñadores(1)\
                \nModelos(2)\
                \nDirectivos(3)\
                \nRasos(4)")
            print("-----------------------------------------------")
            opcion9=int(input())
            print("-----------------------------------------------")
            if opcion9==1:
                a=1
                for i in diseñadores:
                    print(f"{a}.{i}")
                    a+=1
                n=int(input("Que empleado deseas despedir? "))
                diseñadores.pop(n-1)
                print(f"Asi quedo el area de diseño {diseñadores}")
            elif opcion9==2:
                a=1
                for i in modelos:
                    print(f"{a}.{i}")
                    a+=1
                n=int(input("Que empleado deseas despedir? "))
                modelos.pop(n-1)
                print(f"Asi quedo el area de modelos {modelos}")
            elif opcion9==3:
                a=1
                for i in directivos:
                    print(f"{a}.{i}")
                    a+=1
                n=int(input("Que empleado deseas despedir? "))
                directivos.pop(n-1)
                print(f"Asi quedo el area de directivos {directivos}")
            elif opcion9==4:
                a=1
                for i in rasos:
                    print(f"{a}.{i}")
                    a+=1
                n=int(input("Que empleado deseas despedir? "))
                rasos.pop(n-1)
                print(f"Asi quedo el area de rasos {rasos}")
        elif opcion8.upper()=="N":
            print("Muy bien, eres una buena persona")
    elif opcion1==6:
        grupo=Grupo()
        print("Perfecto, sera divertido")
        print("Necesitaresmos unos datos")
        nombre=input("Nombre de la banda: ")
        n=int(input("Cuantos integrantes va a tener? "))
        j=1
        for i in range(0,n):
            integrantes=input(f"Dime el nombre del integrante n°{j}")
            banda.setIntegrantes(integrantes)
        banda.setNombre(nombre)
        bandas.append(banda)
    elif opcion1==7:
        portafolio=Portafolio()
        print("Has decidido crear un portafolio")
        a=int(input("Cuantos portafolios deseas crear? "))
        j=1
        for i in range(0,a):
            print(f"Portafolio {j}")
            b=int(input("Cuantas fotos deseas en el portafolio?"))
            for i in range(0,b):
                fotos=input("Dame el nombre de la foto: ")
                portafolio.setFotos(fotos)
            objetivo=input("Objetivo: ")
            anoCreacion=input("Año de la creacion: ")
            numPortafolio=input("Numero del portafolio: ")
            portafolio.setObjetivos(objetivo)
            portafolio.setCreacion(anoCreacion)
            portafolio.setNumPortafolio(numPortafolio)
            portafolios.append(portafolio)
            j+=1
    elif opcion1==8:
        agencia=Agencia()
        print("Decidiste crear una agencia")
        print("Necesitaremos unos datos")
        nombre=input("Nombre: ")
        paisCede=input("Pais de la cede principal: ")
        anoCreacion=input("Año de creacion: ")
        correo=input("Correo: ")
        dueno=input("Dueño: ")
        agencia.setNombre(nombre)
        agencia.setCede(paisCede)
        agencia.setCreacion(anoCreacion)
        agencia.setCorreo(correo)
        agencia.setDueno(dueno)
        agencia.setModelos("De momento no hay")
        agencias.append(agencia)
        print(f"Creaste la agencia {agencia}")
    elif opcion1==9:
        print("----------------------------")
        print("Que deseas asignar?")
        print("----------------------------")
        print("1.Desfiles a evento")
        print("2.Desfile a pabellon")
        print("3.Modelos a desfile")
        print("4.Evento a directivo")
        print("5.Desfiles a diseñadores")
        print("6.Modelos a agencia")
        print("7.Desfile a artista")
        print("8.Desfiles a modelos")
        print("9.Portafolios a modelos")
        print("----------------------------")
        opcion11=int(input())
        print("----------------------------")
        if opcion11==1:#Desfiles a evento
            j=1
            for i in eventos:
                print(f"{j}.{i}")
                j+=1
            n=int(input("Digame a que evento desea agregarle los desfiles: "))
            print("_________________________________________________________")
            l=1
            for q in desfiles:
                print(f"{l}.{i}")
                l+=1
            m=int(input("Digame que desfile desea agregar al evento: "))
            print("_________________________________________________________")
            eventos[n-1].setDesfiles(desfiles[m-1])
        elif opcion11==2:#Desfile a pabellon
            j=1
            for i in pabellones:
                print(f"{j}.{i}")
                j+=1
            n=int(input("Digame a que pabellon desea asignarle un desfile: "))
            print("_________________________________________________________")
            l=1
            for q in desfiles:
                print(f"{l}.{i}")
                l+=1
            m=int(input("Digame que desfile desea agregar al pabellon: "))
            print("_________________________________________________________")
            pabellones[n-1].setDesfiles(desfiles[m-1])
        elif opcion11==3:#modelos a desfile
            j=1
            for i in desfiles:
                print(f"{j}.{i}")
                j+=1
            n=int(input("Digame a que desfile desea asignarle las modelos: "))
            print("_________________________________________________________")
            l=1
            for q in desfiles:
                print(f"{l}.{i}")
                l+=1
            m=int(input("Digame que modelos desea agregar al desfile: "))
            print("_________________________________________________________")
            desfiles[n-1].setModelos(modelos[m-1])
        elif opcion11==4:#Evento a directivo
            j=1
            for i in directivos:
                print(f"{j}.{i}")
                j+=1
            n=int(input("Digame a que directivo desea asignarle un evento: "))
            print("_________________________________________________________")
            l=1
            for q in eventos:
                print(f"{l}.{i}")
                l+=1
            m=int(input("Digame que evento desea asignarle al directivo: "))
            print("_________________________________________________________")
            directivos[n-1].setEvento(eventos[m-1])
        elif opcion11==5:#Desfiles a diseñadores
            j=1
            for i in diseñadores:
                print(f"{j}.{i}")
                j+=1
            n=int(input("Digame a que diseñador desea asignarle desfiles: "))
            print("_________________________________________________________")
            l=1
            for q in desfiles:
                print(f"{l}.{i}")
                l+=1
            m=int(input("Digame que desfile desea asignarle al diseñador: "))
            print("_________________________________________________________")
            diseñadores[n-1].vincularDesfiles(desfiles[m-1])
        elif opcion11==6:#Modelos a agencia
            j=1
            for i in agencias:
                print(f"{j}.{i}")
                j+=1
            n=int(input("Digame a que agencia desea asignarle modelos: "))
            print("_________________________________________________________")
            l=1
            for q in modelos:
                print(f"{l}.{i}")
                l+=1
            m=int(input("Digame que modelos desea asignarle a la agencia: "))
            print("_________________________________________________________")
            agencias[n-1].setModelos(modelos[m-1])
        elif opcion11==7:#Desfile a artista
            j=1
            for i in artistas:
                print(f"{j}.{i}")
                j+=1
            n=int(input("Digame a que artista desea asignarle un desfile: "))
            print("_________________________________________________________")
            l=1
            for q in desfiles:
                print(f"{l}.{i}")
                l+=1
            m=int(input("Digame que desfile desea asignarle al artista: "))
            print("_________________________________________________________")
            artistas[n-1].setDesfile(desfiles[m-1])
        elif opcion11==8:#Desfiles a modelos
            j=1
            for i in modelos:
                print(f"{j}.{i}")
                j+=1
            n=int(input("Digame a que modelo desea asignarle un desfile: "))
            print("_________________________________________________________")
            l=1
            for q in desfiles:
                print(f"{l}.{i}")
                l+=1
            m=int(input("Digame que desfile desea asignarle a la modelo: "))
            print("_________________________________________________________")
            modelos[n-1].setDesfile(desfiles[m-1])
        elif opcion11==9:#Portafolios a modelos
            j=1
            for i in modelos:
                print(f"{j}.{i}")
                j+=1
            n=int(input("Digame a que modelo desea asignarle un portafolio: "))
            print("_________________________________________________________")
            l=1
            for q in desfiles:
                print(f"{l}.{i}")
                l+=1
            m=int(input("Digame que portafolio desea asignarle a la modelo: "))
            print("_________________________________________________________")
            modelos[n-1].setPortafolio(portafolios[m-1])
    elif opcion1==10:
        print("Gracias, vuelva pronto")
        z=2