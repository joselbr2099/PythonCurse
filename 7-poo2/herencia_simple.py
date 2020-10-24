#superclase
class Perro(object): 
    raza="default"
    color="default"
    tamaño="default"
    
    def __init__(self,color, raza, tamaño): #constructor
        self.raza=raza
        self.color=color
        self.tamaño=tamaño
        
    def getRaza(self):
        print("Hola soy el perro base de raza ",self.raza)


#subclase
class Mascota(Perro):
    nombre="default"
    
    def __init__(self, nombre,color, raza, tamaño):
        self.nombre=nombre
        Perro.__init__(self,color, raza, tamaño) #constructor de clase perro
        
    def saludar(self):
        print("hola soy ",self.nombre, "soy de raza",self.raza)
        
        
#crear objeto
obj1=Mascota("firulais","negro","poodle","grande")
obj1.getRaza()
obj1.saludar()

print("-----------------------------------")

obj1=Mascota("teniente","blanco","doverman","mediano")
obj1.getRaza()
obj1.saludar()


