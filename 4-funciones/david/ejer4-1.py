def mayor(a,b,c):
    if a>b:
      if a>c:
        print("el mayor es: ", a)
    elif b>c:
        print("el mayor es: ", b)
    else:
        print("el mayor es: ",c)
        
a=int(input("dame un numero: "))
b=int(input("dame otro numero: "))
c=int(input("dame un numero mas: "))

mayor(a,b,c)