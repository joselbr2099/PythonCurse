class Computadora:
  #atributos
  modelo=""
  marca=""
  generacion=""
  dimension=""
  color=""
    
  #constructor
  def __init__(self,mod,mar,gen,dim,col):
      self.modelo=mod
      self.marca=mar
      self.generacion=gen
      self.dimension=dim
      self.color=col
    #metodos
  def funcionar(self):
      print("La computadora ",self.modelo," marca ",self.marca,"de",self.generacion,"funciona 12 horas diarias")
  def procesar(self):
      print("La computadora ",self.modelo," marca ",self.marca,"de",self.generacion,"debe procesar planillas de pago")
  def apoyar(self):
      print("La computadora ",self.modelo," marca ",self.marca,"de",self.generacion,"apoya al area de presupuestos")
           
#comp1 es una instancia de la clase Computadora
comp1=Computadora("15-da","HP","10ma","15","PLOMA")
comp1.funcionar()
comp1.procesar()
comp1.apoyar()
#comp2 otro objeto
comp2=Computadora("Inspiron","DELL","8va","15","NEGRA")
comp2.funcionar()
comp2.procesar()
comp2.apoyar()
         