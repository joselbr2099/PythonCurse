def Carac(nombre):
    cont=0
    for carac in nombre:
      print("--> ",carac)
      cont+=1
    return cont

nombre=input("ingresa una palabra: ")
res=Carac(nombre)
print("total: ",res,"caracteres")