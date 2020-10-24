#superclase perro
class Perro(object): 
    raza="default"
    color="default"
    tamaño="default"
    
    def __init__(self,color, raza, tamaño):
        self.raza=raza
        self.color=color
        self.tamaño=tamaño
        
    def getRaza(self):
        print("Hola soy el perro base de raza ",self.raza)
        
    def saludar(self):
        print("mi raZa es:", self.raza)

#superclase habilidad
class Habilidad(object):
    habilidad="default"
    
    def __init__(self, habilidad):
        self.habilidad=habilidad
        
    def getHabilidad(self):
        print("Mi habilidad es ",self.habilidad)
        
    def saludar(self):
        print("mi habilidad es:", self.habilidad)
  
#subclase  
class mascota(Perro,Habilidad):
    nombre="default"
    def __init__(self, nombre,color, raza, tamaño, habilidad):
        self.nombre=nombre
        
        Perro.__init__(self,color, raza, tamaño) #constructor de clase perro
        
        Habilidad.__init__(self, habilidad) #constructor de clase habilidad
        
    def saludar(self):
        print("hola soy ",self.nombre, "soy de raza",self.raza)
    
    def saludar(self):
        print("mi nombre es:", self.nombre)
        
   
#crear objeto   
obj1=mascota("firulais","negro","poodle","grande", "traer cosas")
obj1.getRaza()
obj1.getHabilidad()
obj1.saludar()

        