class Computadora:
    #atributos
    #color=""
    #hdd=""
    #id=""
    _marca="Dell"
    #modelo=""
    #pantalla=""
    #ram=""
    #service_tag

    def __init__(self, color, hdd, id, modelo, pantalla, ram, service_tag):
        self.color=color
        self.hdd=hdd
        self.id=id
        self.modelo=modelo
        self.pantalla=pantalla
        self.ram=ram
        self.service_tag=service_tag

    def almacenamiento(self):
        print("Esta computadora color", self.color, "posee un HDD de ", self.hdd, "GB del modelo: ", self.modelo, "con una pantalla de ", self.pantalla, "pulgadas, con capacidad de memoria RAM de ", self.ram, "GB y service tag ", self.service_tag)

    def iniciar(self):
        print("Se iniciara la computadora ", self._marca, " ", self.modelo)

    def procesar(self):
        print("Esta computadora procesara su software con ", self.ram)

    def prueba(self):
        print("Se realizaran pruebas al service tag ", self.service_tag)
        
comp1=Computadora("negro", "256", 1, "Inspiron 15 7000 Gaming", 15.6, 16, "XVF15E9R8")
comp1.almacenamiento()
comp1.iniciar()
comp1.procesar()
comp1.prueba()
print("------------------------------------")
comp2=Computadora("rojo", "512", 2, "Inspiron 15 5000 HomeWork", 14, 8, "GTRS4W58F")
comp2.almacenamiento()
comp2.iniciar()
comp2.procesar()
comp2.prueba()