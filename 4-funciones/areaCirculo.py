PI=3.14159 #variable constante

def areaCirculo(radio):
  area=PI*radio**2 #el **2 significa elevado al cuadrado
  return area

radio=int(input("ingrese radio:"))
area=areaCirculo(radio)
print("el area es: ", area)