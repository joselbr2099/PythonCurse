# 6.- sumar los n primeros numeros naturales

n = int(input("Ingrese la cantidad de numeros a sumar "))

cont = 0
for i in range(n):
    cont = cont + i
    print(i)
print(cont)
