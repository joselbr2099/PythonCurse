#Sumar los n primeros numeros naturales
def SumNatu(n):
    s=0
    c=1
    while c<=n:
      s=int(s)+int(c)
      c=int(c)+1
    return s
