def getNum(a,b,c):
    if a>b>c:
        return a,"es el mayor"
    if b>a>c:
        return b,"es el mayor"
    else:
        return c,"es el mayor"

a=int(input("give a number: "))
b=int(input("give b number: "))
c=int(input("give c number: "))

may,msg=getNum(a,b,c)
print("the greatest is: ",may,msg)
