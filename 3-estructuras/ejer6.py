n=int(input("cuantos quieres sumar:"))
#0+1+2+3+4+5...n
acum=0
suma=0
while True:
  #acum=acum+1
  acum+=1
  suma=suma+acum
  if acum==n:
    break
print("resultado1: ", suma)

acum=0
suma=0
#otra forma
while acum<n:
  #acum=acum+1
  acum+=1
  suma=suma+acum  
print("resultado2: ", suma)  

"""
ajhkjkk
hjkdkj
"""