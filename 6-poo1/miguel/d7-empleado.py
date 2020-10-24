class Empleado:
  #atributos
  nombre=""
  carnet=""
  edad=""
  item=""
  salario=""
    
  #constructor
  def __init__(self,nom,car,ed,it,sal):
      self.nombre=nom
      self.carnet=car
      self.edad=ed
      self.item=it
      self.salario=sal
    #metodos
  def marcar(self):
         print("Hola soy ",self.nombre,"mi C.I es: ", self.carnet,"tengo :",self.edad,"mi item es el: ",self.item,"Gano : ",self.salario,"Bs.","y marco en el biométrico")
  def producir(self):
      print("Hola soy ",self.nombre," la producción es diaria")
  def cumplir(self):
      print("Hola soy ",self.nombre," Cumplo al 100 %")
  def aportar(self):
      print("Hola soy ",self.nombre," el aporte es total")
         
#emp1 es una instancia de la clase Empleado
emp1=Empleado
emp1=Empleado("Raul","605660","35","29","5000")
emp1.marcar()
emp1.producir()
emp1.cumplir()
emp1.aportar()
#emp2 otro objeto
emp2=Empleado
emp2=Empleado("Rosemary","7053408","25","13","3000")
emp2.marcar()
emp2.producir()
emp2.cumplir()
emp2.aportar()
         