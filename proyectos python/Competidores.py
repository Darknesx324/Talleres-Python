N=int(input(" Ingrese el numero de competidores en la competencia: "))
Tiempos=[None]*N
Nadadores=[None]*N
CopiarLista=[]

def Competencia():
    for i in range(0,N):
        Nadadores[i]=input(" Ingrese el nombre del competidor "+str(i+1)+" : ")
        Tiempos[i]=int(input(" Ingrese el puntaje de cada competidor "+str(i+1)+" : "))
        print(" Los puntajes de los competidores son: "+str(Tiempos))
        print(" Los participantes de la competencia son: "+str(Nadadores))

Competencia()


def ElegirMenor():
    CopiarLista=Tiempos.copy()
    Tiempos.sort()
    for i in range(0,N,1):
        Resultado=Tiempos[i]
        Indice=CopiarLista.index(Resultado)
        print(" El ",str(i+1)+" er Lugar es de:  ",Nadadores[Indice]," Con ",Tiempos[i])

ElegirMenor()
