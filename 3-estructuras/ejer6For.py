n=int(input("cuantos quieres sumar:"))
#acum=0
suma=0
#otra forma
#while acum<n:
  #acum=acum+1
#  acum+=1
#  suma=suma+acum  
#print("resultado2: ", suma)
#0+1+2+3
for num in range(n+1):
  suma=suma+num
print("resultado: ",suma)