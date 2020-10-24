class Persona(object):
  
  #constructor
  def __init__(self,nom,ci,res,sexo,ed):
    self.nombre=nom 
    self.ci=ci 
    self.residencia=res 
    self.sexo=sexo
    self.edad=ed

  def estudiar(self):
    print("Hola soy ",self.nombre," no molestes estoy estudiando")

  def trabajar(self):
    print("Hola soy ",self.nombre," no molestes estoy trabajando a  mis",self.edad," años")
    
class Estudiante(Persona):

  carrera="informatica"
 
  #constructor
  def __init__(self,nom,ci,res,sexo,edad,grad):
    #llamamos al constructor dela calse principal
    Persona.__init__(self,nom,ci,res,sexo,edad)
    self.grado=grad

    
  def estudiar(self):
    print("Hola soy ",self.nombre," no molestes estoy estudiando")

  def materias(self):
    print("Hola soy ", self.nombre," y estoy en la carrera de ",self.carrera, "y llevo 60 mataerias y estoy en el grado" , self.grado  )    

#programa principal----------------------------------------------
estu1=Estudiante("jose","3424","La Paz","masculino","23","4")
estu1.estudiar()
estu1.trabajar()
print("mi ci  es: ",estu1.ci)
print("mi grado  es: ",estu1.grado)
