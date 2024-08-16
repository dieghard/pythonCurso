# Ejercicio 1: 
# Crear una clase llamada Rectangulo 
# que tenga dos atributos: ancho y alto.
# que tenga dos metodos: area y perimetro.

import funciones as fp

class Rectangulo:
    """
    Clase que crea un objeto Rectangulo, con metodos para mostrar todas sus caracteristicas, area y perimetro.
    \n 
    En caso de que no se agreguen los argumentos al momento de declarar el objeto se tomaran los valores por defecto que es 0.
    """
    def __init__(self)->None:
        alto = fp.numero("Ingrese el Alto:")
        ancho = fp.numero("Ingrese el Ancho:")
        self.ancho = ancho
        self.alto = alto
    def mostrar_caracteristicas(self):
        print(f"El ancho del rectangulo es {self.ancho} y el alto del rectangulo es {self.alto}")
        return
    def area (self):
        area = self.ancho * self.alto
        print (f"El area del rectangulo es {area}")
        return
    def perimetro(self):
        perimetro = self.ancho * 2 + self.alto *2
        print (f"El perimetro del cuadrado es {perimetro}")
        return
    

"""rectangulo_1 = Rectangulo()
rectangulo_1.mostrar_caracteristicas()
rectangulo_1.area()
rectangulo_1.perimetro()"""
