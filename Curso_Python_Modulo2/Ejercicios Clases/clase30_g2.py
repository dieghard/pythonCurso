# Ejercicio 1: 
# Crear una clase llamada Rectangulo 
# que tenga dos atributos: ancho y alto.
# que tenga dos metodos: area y perimetro.
import funciones as fp

class Rectangulo:
    def __init__(self) -> None:
        self.alto = fp.ingresar_numero("Ingrese el alto:")
        self.ancho = fp.ingresar_numero("Ingrese el ancho:")
        pass
    def mostrar_caracteristicas(self):
        data = f"El alto del Rectangulo declarado es {self.alto} y el ancho es {self.ancho}" 
        print(data)
        fp.hablar(data)
    def area(self):
        data = f"El area es {(self.alto * self.ancho)}"
        print(data)
        fp.hablar(data)
        return
    
    def perimetro(self):
        print(f"El perimetro es {(self.ancho + self.alto) * 2}")
        return 
    
cuadradito = Rectangulo()
cuadradito.mostrar_caracteristicas()
cuadradito.area()
cuadradito.perimetro()
        