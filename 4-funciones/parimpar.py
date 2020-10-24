def verf(a):
  res=a%2  #si res es 0 el numero es par, si es 1 el numero es impar 
  if res==0:
    print("el numero es par")
  else:
    print("el numero es impar")

X=int(input("ingrese un numero: "))
verf(X)