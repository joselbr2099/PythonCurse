
class Empleado(object): 
    nombre="default"
    apellido="default"
    edad="default"
    
    def __init__(self,nombre, apellido, edad): 
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    def getNombre(self):
        print("Hola soy ",self.nombre)



class Desarrollador(Empleado):
    nombre="default"
    
    def __init__(self, nombre,apellido,edad):
        self.nombre=nombre
        Empleado.__init__(self,nombre, apellido, edad) 
        
    def saludar(self):
        print("hola soy ",self.nombre, "y mi apelldido es",self.apellido)
        
    def presentar(self):
        print("tengo",self.edad,"años y me gusta programar")
        

obj1=Desarrollador("Jorge","Lopez","41")
obj1.getNombre()
obj1.saludar()


obj1=Desarrollador("joel","alcon","33")
obj1.getNombre()
obj1.saludar()
obj1.presentar()