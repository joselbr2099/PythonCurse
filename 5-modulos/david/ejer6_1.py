# 1.- determine el mayor de tres numeros usando funciones

def mayor(a, b, c):
    if a > b:
        if a > c:
            print("el mayor es: ", a)
    elif b > c:
        print("el mayor es: ", b)
    else:
        print("el mayor es: ", c)