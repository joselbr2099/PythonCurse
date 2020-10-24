# 7.- pedir datos al usuario hasta que se escriba STOP

cond=True
while cond:
  pal=input("dame algo: ")
  if pal=="STOP":
    cond=False
print("terminado") 