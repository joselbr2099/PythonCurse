class Estudiante_colegio:
    nombre="jose"
    apellido="ralde"
    colegio="San Jorge"
    curso="sexto"
    telefono="7156666"
    direccion="Villa victoria"
    __notafinal="10"
    
    def __init__(self , nombre, apellido, colegio, curso, telefono, direccion):
        self.nombre=nombre
        self.apellido=apellido
        self.colegio=colegio
        self.curso=curso
        self.telefono=telefono
        self.direccion=direccion
        
    def estudiar(self):
        print("Hola soy ",self.nombre," estoy estudiando")
        
    def aprender(self):
        pritn("Hola, yo aprendo en el colegio ",self.colegio)
        
    def reasolve(self):
        print("Hola yo resuelvo ejercicios de programación")
        


estudiante1=Estudiante_colegio("aaron","ralde","San Jorge","5to","465646","Villa victoria")

# estudiante1.__notafinal=1

print(estudiante1.__notafinal)