def Nombre(nombre):
    rep=10
    while rep>0:
      print("--> ",rep," ",nombre)
      rep=rep-1
    print("terminado")

nombre=input("dame tu nombre: ")
Nombre(nombre)
