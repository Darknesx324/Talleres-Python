
nombreFichero = "prueba.txt"

def OpenAndRead():
    try:
        with open(nombreFichero) as fichero:
            lineas = fichero.readlines()
            return lineas
    except Exception as e:
        print("Exception: ",e)

def agregarLibro(nombre, precio, autor, fecha):
    try:
        with open(nombreFichero, "a") as fichero:
            nuevoLibro = '\n'+nombre+', '+precio+', '+autor+', '+fecha
            fichero.write(nuevoLibro)
    except Exception as e:
        print("Exception: ",e)

def convertirLista(lista):
    nuevaLista = []
    try:
        for libro in lista:
            libroLista = libro.split(',')
            nuevaLista.append(libroLista)
        return nuevaLista
    except Exception as e:
        print("Exception: ",e)

def buscarLibroPorNombre(nombreLibro, lista):
    libroBuscado = ""
    try:
        for libro in lista:
            if(libro[0] == nombreLibro):
                libroBuscado = ",".join(libro)
        return libroBuscado
    except Exception as e:
        print("Exception: ",e)

def buscarLibroPorMayorPrecio(lista):
    libroBuscado = ""
    precio = 0
    try:
        for libro in lista:
            precioLibroActual = int(libro[1].strip())
            if(precio < precioLibroActual):
                precio = precioLibroActual
                libroBuscado = ",".join(libro)
        return libroBuscado
    except Exception as e:
        print("Exception", e)
            
#En este apartado se realiza el programa principal.

lineas = OpenAndRead()
NewLines = convertirLista(lineas)
libroBuscado1 = buscarLibroPorNombre("",NewLines)
libroBuscado2 = buscarLibroPorMayorPrecio(NewLines)
print(NewLines)

nombre=input("Ingrese el nombre del nuevo libro: ")
precio=input("Ingrese el precio del nuevo libro: ")
autor=input("Ingrese el autor del nuevo libro: ")
fecha=input("Ingresa la fecha del nuevo libro: ")
print(NewLines)
print(libroBuscado1)
print(libroBuscado2)
