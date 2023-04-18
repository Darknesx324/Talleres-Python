def calcularComision(categoria,ventas):
    if categoria==1:
        comision=ventas*0.1
    elif categoria==2:
        comision=ventas*0.2
    elif categoria==3:
        comision=ventas*0.35
    elif categoria==4:
        comision=ventas*0.45
    elif categoria==5:
        comision=ventas*0.5
    elif categoria==6:
        comision=ventas*0.6
    else:
        print(" Categoria Inexistente. ")
        return calcularComision()



    #Programa principal
    ventas=float(input(" Digite el valor de las ventas: "))
    categoria=int(input(" Digite el valor de la categoria: "))
    print(" La comision es tanto: ",calcularComision(categoria,ventas))
