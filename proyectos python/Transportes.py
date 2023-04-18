def IngresoDeRuta():
    for i in range(0,NumeroRuta):
        Rutas[i]=input(" Ingrese el nombre de la ruta: ")
        Pasajeros[i]=int(input(" Ingrese la cantidad de pasajeros movilizados por la "+Rutas[i]+" : "))


def ImprimirRutasYPasajeros():
    for i in range(0,NumeroRuta):
     print(Rutas[i] + ":" +str(Pasajeros[i]))

def Total():
    total=0
    for i in range(0,NumeroRuta):
        total=total+Pasajeros[i]
        print(" El total de pasajeros movilizados en el dia es de: ",total)

def ImprimirMayor():
    ruta=Rutas[0]
    pasajeros=Pasajeros[0]
    for i in range(0,NumeroRuta):
        if(Pasajeros[i]>pasajeros):
            ruta=Rutas[i]
            pasajeros=Pasajeros[i]
            print(" La ruta "+ruta+" Fue la que mas movilizo con una cantidad de "+str(pasajeros)+"Pasajeros")

NumeroRuta=5
Rutas=[None]*NumeroRuta
Pasajeros=[None]*NumeroRuta
IngresoDeRuta()
print("")
print(" Rutas Y Pasajeros ")
ImprimirRutasYPasajeros()
print("")
Total()
ImprimirMayor()