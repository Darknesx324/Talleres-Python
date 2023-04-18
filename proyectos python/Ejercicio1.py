def TipoPan(integral,semillas):
    integral = 1200
    semillas = 1700

def TipoCarne(Pavo,Pollo,Jamon):
    Pavo=5600
    Pollo=4100
    Jamon=2200

def TipoVegetal(Pepinillos,Lechuga,Tomate):
    Pepinillos=2500
    Lechuga=1200
    Tomate=2000

def PrecioSandwich():
    if(TipoPan() and TipoCarne() and TipoVegetal()):
        TotalPagar= TipoPan() + TipoCarne() + TipoVegetal():
        print("El valor a pagar por el sandwich es: ",TotalPagar)


