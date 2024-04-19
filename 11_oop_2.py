
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

class Auto(Vehiculo):
    def __init__(self, marca, modelo, color, cantidad_puertas):
        super().__init__(marca, modelo, color)  # Llamada al constructor de la clase padre
        self.cantidad_puertas = cantidad_puertas

    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} acelera rápidamente!")  # Sobreescritura

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, color, capacidad_carga):
        super().__init__(marca, modelo, color)
        self.capacidad_carga = capacidad_carga

    def acelerar(self):
        print(f"La camioneta {self.marca} {self.modelo} acelera con potencia.")  # Sobreescritura

auto1 = Auto("Ford", "Fiesta", "Rojo", 5)
camioneta1 = Camioneta("Toyota", "Hilux", "Plateada", 1000)
auto1.acelerar()
camioneta1.acelerar()
