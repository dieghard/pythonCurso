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
#Ejercicio 1:
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

mi_rectangulo = Rectangulo(4, 5)
print("Área:", mi_rectangulo.area())          # Salida: Área: 20
print("Perímetro:", mi_rectangulo.perimetro())  # Salida: Perímetro: 18

#Ejercicio 2:
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depositaste {cantidad}. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiraste {cantidad}. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"El saldo actual es: {self.saldo}")

mi_cuenta = CuentaBancaria("Juan Perez", 1000)
mi_cuenta.depositar(500)                # Salida: Depositaste 500. Nuevo saldo: 1500
mi_cuenta.retirar(200)                  # Salida: Retiraste 200. Nuevo saldo: 1300
mi_cuenta.mostrar_saldo()               # Salida: El saldo actual es: 1300

#Ejercicio 3:
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

mi_producto = Producto("Laptop", 1000, 5)
print("Valor total:", mi_producto.calcular_valor_total())  # Salida: Valor total: 5000
mi_producto.actualizar_precio(1200)
print("Nuevo valor total:", mi_producto.calcular_valor_total())  # Salida: Nuevo valor total: 6000
#Ejercicio 4:
class Contador:
    def __init__(self):
        self.cuenta = 0

    def incrementar(self):
        self.cuenta += 1

    def decrementar(self):
        if self.cuenta > 0:
            self.cuenta -= 1

    def mostrar_cuenta(self):
        return self.cuenta

    def reiniciar(self):
        self.cuenta = 0

mi_contador = Contador()
mi_contador.incrementar()
mi_contador.incrementar()
print("Cuenta:", mi_contador.mostrar_cuenta())  # Salida: Cuenta: 2
mi_contador.decrementar()
print("Cuenta:", mi_contador.mostrar_cuenta())  # Salida: Cuenta: 1
mi_contador.reiniciar()
print("Cuenta:", mi_contador.mostrar_cuenta())  # Salida: Cuenta: 0
