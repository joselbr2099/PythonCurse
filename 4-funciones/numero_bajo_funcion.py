
#funcion que retorna el menor de dos numeros
def numero_menor(a,b):
  if a <= b:
    menor=a
  else:
    menor=b

  return menor #toda funcion retorna algo
#termina la funcion

#procedimiento que muestra el menor de dos numeros
def numero_menorProc(a,b):
  if a <= b:
    menor=a
  else:
    menor=b
  print("el numero menor es:", menor)
#los procedimientos no retornan nada  
  

#se pide datos al usuario
a=int(input("numero a: "))
b=int(input("numero b: "))

#se llama a la funcion
menor=numero_menor(a,b)

#se obtiene el resultado con funcion
print("el numero menor es:", menor) 


#se obtiene el resultado con procedimiento
numero_menorProc(a,b)