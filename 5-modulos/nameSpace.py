def funcion_a():
    y = 2
    def funcion_b():
        z = 3
        print(z)
    funcion_b()
    print(y)
    print(z)
x = 1      
funcion_a()
print(x)