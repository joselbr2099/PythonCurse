a=int(input("dame un numero: "))
b=int(input("dame otro numero: "))
c=int(input("dame un numero mas: "))
print("codigo inicial-----------------------------")
if a>b:
  if a>c:
    print("el mayor es: ", a)
else:
  if b>c:
    print("el mayor es: ", b)
  else:
    print("el mayor es: ",c)
print("codigo secundario-----------------------------")
#usando elif
if a>b:
  if a>c:
    print("el mayor es: ", a)
elif b>c:
    print("el mayor es: ", b)
else:
    print("el mayor es: ",c)

#codigo de juan carlos
print("codigo de juan-----------------------------")
if a>b and a>c:
    print("primer número es mayor")
else:
    if b>a and b>c:
        print("segundo número es mayor")
    else:
        if c>a and c>b:
            print("tercer número es mayor")