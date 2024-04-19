class Vehiculo:
  def __init__(self, marca, modelo, color):
    self.marca = marca  # Atributo público
    self.modelo = modelo  # Atributo público
    self.color = color  # Atributo público

  def arrancar(self):
    print(f"El vehículo {self.marca} {self.modelo} está arrancando.")

  def acelerar(self):
    print(f"El vehículo {self.marca} {self.modelo} está acelerando.")

  def frenar(self):
    print(f"El vehículo {self.marca} {self.modelo} está frenando.")

miAuto = Vehiculo("Toyota", "Corolla", "Azul")
miMoto = Vehiculo("HARLEY DAVIDSON", "1200", "Negra")

# Accionando los métodos de los objetos:
miAuto.arrancar()
miMoto.acelerar()
miAuto.frenar()

miMoto.arrancar()
miMoto.acelerar()
miMoto.frenar()