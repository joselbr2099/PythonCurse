def funcion_a():
    global x
    x = 2
    def funcion_b():
        global x
        x = 3
        print(x)

    funcion_b()
    print(x)

x = 1
funcion_a()
print(x)