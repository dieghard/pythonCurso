# Ejercicio 2. Crear una lista de números y luego:
# Calcular la suma de todos los números de la lista.
# Encontrar el número máximo y mínimo de la lista.
# Multiplicar cada número de la lista por 2.
# Imprimir los números pares de la lista.

lista_numeros = [1, 23, 63, 14, 95, 46, 77, 8, 39, 51]
print("lista de números")
print(lista_numeros) # salida = [1, 23, 63, 14, 95, 46, 77, 8, 39, 51]
print("\n")

# Calcular la suma de todos los números de la lista.
suma_numeros = sum(lista_numeros)
print(f"suma de todos los números: {suma_numeros}") # salida = 417
print("\n")

# Encontrar el número máximo y mínimo de la lista.
numero_max = max(lista_numeros)
numero_min = min(lista_numeros)
print(f"número máximo: {numero_max}") # salida = 95
print("\n")
print(f"número mínimo: {numero_min}") # salida = 1
print("\n")

# Multiplicar cada número de la lista por 2.
lista_numeros_x_2 = [x * 2 for x in lista_numeros]
print(f"lista de números multiplicados por 2: {lista_numeros_x_2}") # salida = [2, 46, 126, 28, 190, 92, 154, 16, 78, 102]
print("\n")

# Imprimir los números pares de la lista.
for numero in lista_numeros:
    if numero % 2 == 0:
        print(f"El número {numero} es par") # salida = El número 46 es par, El número 14 es par, El número 8 es par
print("\n")