rutas=[]
pasajeros=[]
tamaño=10

for i in range(tamaño):
        print(" Ingrese las rutas escogidas... ",i+1)
        Rutass=input(" Ingrese las rutas correspondientes: ")
        rutas.append(Rutass)
        print(" Numero de pasajeros diarios ",i+1)
        Pasajeros=int(input(" Ingrese el numero de pasajeros: "))
        pasajeros.append(Pasajeros)
        print(" Mostrando listado diario... ",i+1)

    for i in range(tamaño):
        print(" Rutas: ",rutas[i])
        print(" Numero de pasajeros: ",pasajeros[i])