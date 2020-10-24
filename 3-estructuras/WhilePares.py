print("cuantos pares quieres ver? ")
a=int(input())
cont=1
control=0
while control<a:
    if cont%2==0:
        print("el numero ",cont," es par")
        control+=1
    cont+=1
    
