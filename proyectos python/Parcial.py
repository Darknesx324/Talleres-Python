def Subsidios(edad, numhijos):
    subsidio = 5000000
    if edad > 25 and edad < 40 and numhijos < 2:
        subsidio = 12000000
        print(" El valor del subsidio de esta familia es de: ", subsidio)
    elif edad > 40 and numhijos > 2:
        subsidio = 15000000
        print(" El subsidio de esta familia es de: ", subsidio)
    elif edad > 40 or numhijos > 2:
        subsidio = 13000000
        print(" El subsidio de esta familia es de: ", subsidio)

    else:
        print(" El subsidio de la persona es de: ",subsidio)


        return subsidio


def SubsidioM(genero):
    Subsidiom = 0
    if genero == "M":
        Subsidiom = 7000000
        print(" El subsidio municipal es de: ", Subsidiom)
    elif genero == "F":
        Subsidiom = 8000000
        print(" El Subsidio municipal es de: ", Subsidiom)

        return Subsidiom


edad=int(input(" Digite la edad del propietario "))
numhijos=int(input(" Digite el numero de hijos que tiene el propietario: "))
genero=input(" Digite el genero del propietario: ")
print(" La cantidad de subsidio recibida por la persona es de:  ",Subsidios(edad,numhijos))
print("  La cantidad de subsidio recibidad por el municipio segun el genero es: ",SubsidioM(genero))

#Harry Fabian Henao F.