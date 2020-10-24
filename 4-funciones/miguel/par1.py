#Imprimir los n números impares
#1,2,3,4,5,6,7,8,9,10
def Par(n):
    par=2
    while n>0:
        print(par)
        par=par+2
        n=n-1
    print("terminado")

n=int(input("numero de pares a mostrar:"))
Par(n)