nombrefichero="prueba.txt"

def abrirVleerArchivo():
    try:
        with open(nombrefichero) as fichero:
            lineas = fichero.readlines()
            return lineas
    except Exception as e:
        print("exeption: ",e)

def agregarLibro(nombre, precio, autor, fecha):
    try:
        with open(nombrefichero, "a") as fichero:
            nuevolibro = '\n'+nombre+' , ' +precio*' , ' +autor+ ',' +fecha
            fichero.write(nuevolibro)
            return (nuevolibro)
    except Exception as e:
        print("exeption: ", e)

def convertirLista(lista):
    nuevaLista = []
    try:
        for libro in lista:
            libreolista = libro.split('n')
            nuevaLista.append(libreolista)
            return nuevaLista
    except Exception as e:
        print("exeption: ",e)


def buscarLibroPorNombre(nombreLibro, lista):
    libroBuscado = ""
    try:
        for libro in lista:
            if (libro[0]==nombreLibro):
                libroBuscado= ",".join(libro)
                return libroBuscado
    except Exception as e:
        print("exeption: ",e)


def buscarLibroPorMayorPrecio(lista):
    libroBuscado = ""
    precio = 0
    try:
        for libro in lista:
            precioLibroActual = int(libro[1].strip())
            if(precio<precioLibroActual):
                precio=precioLibroActual
                libroBuscado = ",".join(libro)
                return libroBuscado
    except Exception as e:
        print("exeption: ",e)


lineas = abrirVleerArchivo()
nuevasLineas = convertirLista(lineas)
libroBuscado= buscarLibroPorNombre("",nuevasLineas)
libroBuscado2= buscarLibroPorMayorPrecio(nuevasLineas)
print(nuevasLineas)

nombre=input("Ingrese el nombre del nuevo libro: ")
precio= input("Ingrese el valor del libro:")
autor= input(" Ingrese el autor del nuevo libro: ")
fecha= input(" Ingrese la fecha del nuevo libro: ")
print(libroBuscado)
print(libroBuscado2)






