def verf(a):
    res = a % 2 #si res es 0 el numero es par, si es 1 el numero es impar 
    if res == 0:
        print("el numero es par")
    else:
        print("el numero es impar")


continuar = True

while continuar:
    X = input("ingrese un numero: ")  #retorna tipo de dato cadena
    if X != "stop":
        verf(int(X))
    else:
        continuar = False
