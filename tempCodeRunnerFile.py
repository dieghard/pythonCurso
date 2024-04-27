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