class Empleado:
    #atributos
    #ci=""
    #direccion=""
    #id=""
    #nombre=""
    #telefono=""

    def __init__(self, ci, direccion, id, nombre, telefono):
        self.ci=ci
        self.direccion=direccion
        self.id=id
        self.nombre=nombre
        self.telefono=telefono

    def analizar(self):
        print("Hola soy ", self.nombre, " estoy analizando")

    def asistir(self):
        print("Mi asistencia es marcada con ", self.ci)

    def atender(self):
        print("Puedo atender desde el numero", self.telefono)

    def producir(self):
        print("Mi producción esta en la direccion ", self.direccion)

emp1=Empleado("6890309", "San Antonio Alto Calle Uru Uru # 15", 1, "Dave Mercado Juanes", "71525038")
emp1.analizar()
emp1.asistir()
emp1.atender()
emp1.producir()
print("Nombre de Empleado: ", emp1.nombre)
print("------------------------------------------------")
emp2=Empleado("1234567", "San Pedro N 14", 2, "Juan Carlos Juanes", "72006542")
emp2.analizar()
emp2.asistir()
emp2.atender()
emp2.producir()
print("Nombre de Empleado: ", emp2.nombre)