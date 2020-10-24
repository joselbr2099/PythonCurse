import random

def getNum():
  return random.randint(1,4)
 
user=getNum()
while getNum()!=user:
  user=getNum()

if user==1:
  print("le toca a david")
if user==2:
  print("le toca a jose")
if user==3:
  print("le toca a juan")
if user==4:
  print("le toca a miguel")  