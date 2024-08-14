#Definiendo OBJETOS

class vehiculos:
    def __init__(self, color:str, puertas:int , modelo:str , marca:str) -> None :
        self.color = color
        self.puertas = puertas
        self.modelo = modelo
        self.marca = marca
        self.encendido = False
    def mostrar_caracteristicas(self):
        esta_encendido = "el auto 😊 esta encendido"
        if self.encendido == False :
            esta_encendido = "el auto 😢 esta apagado"
            
        
        print (f"El auto es de color {self.color}, Tiene {self.puertas} puertas y el modelo es {self.modelo} de la marca {self.marca}. 🚗 {esta_encendido}")
    def encender (self):
        self.encendido = True
    def apagar (self):
        self.encendido = False

    def mostrar_color(self):
        
        return

auto_diego = vehiculos("rojo", 2, "Fiesta", "Ford")
auto_diego.mostrar_caracteristicas()
auto_diego.encender()
auto_diego.mostrar_caracteristicas()
auto_diego.apagar()
auto_diego.mostrar_caracteristicas()

# auto_gaspar = vehiculos("azul", 4, "Duster", "Renoult")
# auto_leti = vehiculos("Negro", 5, "208", "peugeot")
# auto_diego.mostrar_caracteristicas()
# print (f"El color es {auto_gaspar.color}")
# auto_gaspar.color = "verde"
# print (f"El color es {auto_gaspar.color}")
# auto_gaspar.mostrar_caracteristicas()
