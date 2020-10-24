def mayor(a,b,c):
    
    if a>b and a>c:
        return a,"es el mayor"
    else:
        if b>a and b>c:
            return b,"es el mayor"
        else:
            if c>a and c>b:
                return c,"es el mayor"
    
    
a=int(input("ingrese numero a:"))
b=int(input("ingrese numero b:"))
c=int(input("ingrese numero c:"))    
may,msg=mayor(a,b,c)

print("El número mayor es: ",may,msg)