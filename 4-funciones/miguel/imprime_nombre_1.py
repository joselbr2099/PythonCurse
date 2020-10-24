#imprima su nombre n veces 
def Nombre(nombre,numero):
    rep=numero
    while rep>0:
      print("--> ",rep," ",nombre)
      rep=rep-1
    return
    print("terminado")

nombre=input("dame tu nombre: ")
numero=int(input("Dame un número: "))
Nombre(nombre,numero)

