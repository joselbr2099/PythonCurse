class Estudiante:
  #atributos
  #nombre=""
  #grado=""
  carrera="informatica"
  #carnet=""
  #edad=""

  #constructor
  def __init__(self,nom,grad,car,edad):
    self.nombre=nom
    self.grado=grad
    #self.carrera=carr
    self.carnet=car
    self.edad=edad

  def estudiar(self):
    print("Hola soy ",self.nombre," no molestes estoy estudiando")

  def materias(self):
    print("Hola soy ", self.nombre," y estoy en la carrera de ",self.carrera, "y llevo 60 mataerias y estoy en el grado" , self.grado  )

#estu1 es una instancia de la clase estudiante
estu1=Estudiante("jose","5","33434","34")  
estu1.estudiar()
estu1.materias()
print("nombre de estudiante:", estu1.nombre)
estu1.nombre="joseLuis"
print("nombre de estudiante(new):", estu1.nombre)
print("---------------------------------")
#otro objeto
estu2=Estudiante("martin","20","3334535","14")
estu2.estudiar()
estu2.materias()
print("nombre de estudiante:", estu2.nombre)
estu2.nombre="martinVIzcarra"
print("nombre de estudiante:(new)", estu2.nombre)