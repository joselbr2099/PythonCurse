class Perro:
    
    tipo="perro" #atributo 
    
    def __init__(self, raza, edad, color, nombre):
        self.raza=raza #atributos disponible para cada instancia
        self.edad=edad  #de manera unica
        self.color=color
        self.nombre=nombre
    
    def correr(self):
        print("Estoy corriendo")
        
    def ladrar(self):
        print("waw waw waw")
        
    def jugar(self):
        print("Tirame algo y te lo traigo")
    
    #def edad(self):#no puede haber un metodo con el mismo nombre de un atributo
    #    print("mi edad es: ",self.edad)
        
ob1=Perro("poodle",2,"leonardo","firulais")  #se instancia 
print("nombre obj1",ob1.nombre)

print("---------------------------")

ob2=Perro("normal",1,"leonardo2","teniente")
print("nombre obj2",ob2.nombre)


"""una clase con esos atributos
#ob1.correr() #se llama a un metodo
#print("edad: ",ob1.edad) #se imprime un atributo
#ob1.edad=10  #se modifica el atributo
#print("edad(mod): ",ob1.edad)
#print("tipo de animal: :",ob1.tipo)
#ob1.tipo="perro-a"
#print("tipo de animal: :",ob1.tipo)
#print("nombre obj1",ob1.nombre)
"""
