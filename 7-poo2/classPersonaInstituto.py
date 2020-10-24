class Persona(object):
  
  #constructor
  def __init__(self,nom):
    self.nombre=nom 

  def estudiar(self):
    print("Hola soy ",self.nombre," no molestes estoy estudiando")

class Instituto(object):
  
  #constructor
  def __init__(self,nom):
    self.nombreInsti=nom 

  def saludo(self):
    print("Hola soy el instituto ",self.nombreInsti," y te  saludo")

class Estudiante(Persona,Instituto):

  carrera="informatica"
 
  #constructor
  def __init__(self,nomp,nomi,grad):
    #llamamos al constructor dela calse principal
    Persona.__init__(self,nomp)
    Instituto.__init__(self,nomi)
    self.grado=grad

  def materias(self):
    print("Hola llevo 60 mataerias y estoy en el grado" , self.grado)

 #prog prinncipal----------------------------------

estu1=Estudiante("jose","Educomser","5")
estu1.estudiar()
estu1.saludo()
estu1.materias()
print("mi nombre es: ",estu1.nombre)
print("mi instituto es: ",estu1.nombreInsti)
print("mi grado es: ",estu1.grado)