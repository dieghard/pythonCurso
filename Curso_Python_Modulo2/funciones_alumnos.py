#Conversion de temperatura
## Ejemplo 1
def sumar(a :int , b:int):
    return a + b

resultado = sumar(5,5)
print(resultado) #Devuelve: 8
print(sumar(5,5))

#Calcular Perimitro de un rectangulo : 10
def calcular_perimetro_rectangulo(base, altura):
  # Función que calcula el perímetro de un rectángulo.
  perimetro = 2 * (base + altura)
  return perimetro

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
perimetro = calcular_perimetro_rectangulo(base, altura)
print(f"El perímetro del rectángulo es: {perimetro}")

def convertir_temperatura(temperatura, unidad):
    if unidad.upper() == 'C':
        return (temperatura - 32) * 5/9
    elif unidad.upper() == 'F':
        return (temperatura * 9/5) + 32
    else:
        return "Unidad no reconocida"
print(convertir_temperatura(68, 'F'))  # Devuelve: 20.0 (Celsius)
print(convertir_temperatura(30, 'C'))  # Devuelve: 86.0 (Fahrenheit)

## Numero par o impar
def es_par(numero):
  """Función que verifica si un número es par o impar."""
  if numero % 2 == 0:
    return True
  else:
    return False

# Ejemplo de uso
# numero = 10
numero = int(input("Ingresa un número: "))
if es_par(numero):
  print(f"{numero} es un número par")
else:
  print(f"{numero} es un número impar")  # Imprime: 10 es un número par


##Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # Devuelve: 120

#Fibonacci
def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]

print(fibonacci(10))  # Devuelve: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


## Encontrar el máximo de tres números:
def encontrar_maximo(numero1, numero2, numero3):
  maximo = numero1
  if numero2 > maximo:
    maximo = numero2
  if numero3 > maximo:
    maximo = numero3
  return maximo
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
maximo = encontrar_maximo(numero1, numero2, numero3)
print(f"El número máximo entre {numero1}, {numero2} y {numero3} es {maximo}")

### 1. Generar una lista de números aleatorios:

import random

def generar_lista_aleatoria(cantidad, minimo, maximo):
  """Función que genera una lista de números aleatorios entre un rango especificado."""
  lista_aleatoria = []
  for _ in range(cantidad):
    numero_aleatorio = random.randint(minimo, maximo)
    lista_aleatoria.append(numero_aleatorio)
  return lista_aleatoria

cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))
minimo = int(input("Ingrese el valor mínimo del rango: "))
maximo = int(input("Ingrese el valor máximo del rango: "))

lista_generada = generar_lista_aleatoria(cantidad, minimo, maximo)
print(f"Lista de números aleatorios: {lista_generada}")

#Nuestas funciones

def numero (texto_input:str|None= "Ingrese un numero:")-> int:
    """
    Funcion para ingresar y validar un numero,
    texto_input muestra el mensaje por consola
    """
    while True:
        numero_1 = input (texto_input)
        if numero_1.isdigit():
            numero_1 = int(numero_1)
            if numero_1 > 0:
                break
            else:
                print("El valor ingresado debe ser mayor a 0")
        else:
            print("El valor ingresado no es un Nro")
    return numero_1

#Ejemplo 1: Una funcion que salude, teniendo en cuenta que puede tener doble nombre y doble apellido:

def saludo(nombre:str, apellido:str | None = " ")->str:
    print(f"Hola {nombre}{apellido}")
    return
saludo("Eugenia", " de Escobar")


#Ejemplo 2: Calcular el área de un cuadrado:

def area (lado:int | None = 0)->int:
    return  lado**2

calculo = numero()
resultado = area(calculo)
print(f" El area del cuadrado es: {resultado}")
