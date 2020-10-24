class Empleado(object):
    #contructor
    def __init__(self, nom, ci, res, sexo, ed, area, prof):
        self.nombre = nom
        self.ci = ci
        self.residencia = res
        self.sexo = sexo
        self.edad = ed
        self.area = area
        self.profesion = prof

    def estudiar(self):
        print("Hola soy ", self.nombre, " no molestes estoy estudiando")

    def trabajar(self):
        print("Hola soy ", self.nombre, " no molestes estoy trabajando a  mis", self.edad, " años")

class Profesional(Empleado):
    profesion="Desarrollador"

    def __init__(self, nom, ci, res, sexo, ed, area, prof, exp):

        Empleado.__init__(self, nom, ci, res, sexo, ed, area, prof)
        self.experiencia = exp

    def producir(self):
        print("Hola soy ", self.profesion, "trabajo en el area de ", self.area)

prof1=Profesional("Dave", "6890309", "La Paz", "Masculino", "29", "Sistemas", "Ingeniero de Sistemas", "3 Años")
prof1.producir()
prof1.estudiar()
print("Tengo ", prof1.experiencia, " años")
