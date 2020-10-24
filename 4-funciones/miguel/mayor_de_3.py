def Mayor(a,b,c):    
#usando elif
  res=0
  if a>b:
    if a>c:
      res=a
  elif b>c:
    res=b
  else:
    res=c
  return res

a=int(input("ingrese numero a:"))
b=int(input("ingrese numero b:"))
c=int(input("ingrese numero c:"))
res=Mayor(a,b,c)
print(res)