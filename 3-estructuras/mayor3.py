print("dame un numero: ")
a=int(input())
print("dame otro numero: ")
b=int(input())
print("dame uno mas: ")
c=int(input())

if a>b:
    if a>c:
        print("el mayor es: ",a)
elif b>c:
    print("el mayor es: ", b)
else:
    print("el mayor es: ", c)
