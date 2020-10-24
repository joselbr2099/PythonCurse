def getNum(a,b):
    if a>b:
        return a,"es el mayor"
    else:
        return b,"es el mayor"

a=int(input("give a number: "))
b=int(input("give v number: "))

may,msg=getNum(a,b)

print("the greatest is: ",may,msg)



