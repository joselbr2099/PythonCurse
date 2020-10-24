def funcion_a():
    x = 2
    def funcion_b():
        x = 3
        print(x)

    funcion_b()
    print(x)

x = 1
funcion_a()
print(x)