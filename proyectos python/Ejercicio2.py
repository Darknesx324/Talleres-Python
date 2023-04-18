nombres=[]
documento=[]
salario=[]
totalsalarios=[]
for x in range(3):
    nom=input("Ingrese el nombre del empleado:")
    nombres.append(nom)
    doc = input("Ingrese el documento del empleado:")
    documento.append(doc)
    su1 = int(input("Ingrese el salario del empleado:"))


    salario.append([su1])

    for x in range(3):
        total = salario[x][0] + salario[x][1] + salario[x][2]
        totalsalarios.append(total)
