#Objetivo del ejercicio: Arreglar los siguientes programas con errores:

#Ejercicio 1: Saludar usuario. 
#Cantidad errores: 3
nombre_usuario = input("Ingrese su nombre:" )
print(f"Hola, {nombre_usuario}! Bienvenido!")


#Ejercicio 2: Promedio de 4 numeros. 
#Cantidad errores: 5
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

promedio = num1 + num2 + num3 + num4 / 4
print(f"El promedio es: {promedio}")

#Ejercicio 3: Verificar si el estudiante aprobo:
#Cantidad de errores: 2

calificacion = int(input("Ingrese la calificación del estudiante: "))

if calificacion >= 6:
    print("El estudiante ha aprobado")
else:
    print("El estudiante ha reprobado")

#Ejercicio 4: Lista de Compras.
#Cantidad de errores: 1
lista_compras = []

while True:
    item = input("Ingrese un artículo para agregar a la lista (o 'salir' para terminar): ")
    if item == 'salir':
        break
    lista_compras.append(item)

print("Lista de compras:")
for i in range(len(lista_compras)):
    print("- " + lista_compras[i])

#Ejercicio 5: Clase Circulo.
#Cantidad de errores: 3

class Circulo:
    def __init__(self,radio):
        self.radio = radio
    
    def calcular_area(self):
        return 3.14159 * self.radio ** 2

mi_circulo = Circulo(5)
print(f"El área del círculo es:  {mi_circulo.calcular_area()}")


#Ejercicio 6: Generar un numero Aleatorio.
#Cantidad de errores: 3
import random
numero = random.randint(1, 10)
print(f"El número aleatorio generado es: {numero}")

#Ejercicio 7: Contar Vocales en una Cadena:
#Cantidad errores: 4

cadena = "Hola Mundo"
vocales = "aeiou"
contador = 0

for letra in cadena:
    if letra.lower() in vocales:
        contador += 1

print(f"Número de vocales en la cadena:{contador}")

#Ejercicio 8: Funcion para repetir cadenas.
#Cantidad de errores: 3
def repetir_cadena(cadena, veces):
    resultado = cadena * veces
    return resultado

texto = input("Ingrese un texto: ")
repeticiones = int(input("¿Cuántas veces desea repetir el texto? "))
print(f"El texto repetido es: {repetir_cadena(texto,repeticiones)}")