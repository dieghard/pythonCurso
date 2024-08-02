# ¿Qué son las listas? [🛒]
## Explicacion Rapida: Una lista es un conjunto de elementos

### Las listas en Python son estructuras de datos que se utilizan para almacenar una colección de elementos ordenados, estos elementos pueden ser de cualquier tipo, como números, cadenas de texto, booleanos, etc.
---
# Características de las listas: ⭕
- ## Ordenadas: Las listas mantienen el orden en el que se agregan los elementos.
- ## Mutables: Los elementos de una lista se pueden modificar, agregar o eliminar.
- ## Heterogéneas: Una lista puede contener elementos de diferentes tipos.
- ## Anidadas: Se pueden crear listas dentro de otras listas.
---
# Crear una lista: 🤖
## Las listas se pueden crear utilizando corchetes [] y separando los elementos por comas.
## Lista de números
```python
numeros = [1, 2, 3, 4, 5]
```
## Lista de cadenas
```python
nombres = ["Ana", "Juan", "María"]
```
## Lista mixta
```python
mixta = [1, "Hola", True]
```
---
# Acceder a elementos: 🦾
## Se puede acceder a un elemento específico de una lista utilizando su índice, el índice comienza en 0 para el primer elemento.
### Acceder al segundo elemento de la lista "numeros"
```python
numeros = [1, 2, 3, 4, 5]
segundo_numero = numeros[1]
print (segundo_numero)
```
### Acceder al último elemento de la lista "nombres"
```python
nombres = ["Ana", "Juan", "María"]
ultimo_nombre = nombres[-1]
print (ultimo_nombre)
```
### Cambio de valor de la lista "nombres"
```python
nombres[0] ="Diego"
print(nombres)
```
---

# Operaciones con listas: 😛

- ## Agregar elementos: Se pueden agregar elementos al final de la lista usando el método append().
- ## Eliminar elementos: Se pueden eliminar elementos de la lista usando el método remove() o pop().
- ## Encontrar elementos: Se puede buscar un elemento en la lista usando el operador in.
- ## Ordenar la lista: Se puede ordenar la lista usando el método sort().
## Ejemplo de uso:
### Crear una lista de compras
```python
lista_compras = ["Leche", "Pan", "Huevos", "Manzanas"]
print (lista_compras)
```
### Agregar un elemento a la lista
```python
lista_compras.append("Tomates")
print (lista_compras)
```
### Eliminar un elemento de la lista
```python
lista_compras.remove("Pan")
print (lista_compras)
```

### Buscar un elemento en la lista
```python
if "Manzanas" in lista_compras:
  print("Las manzanas están en la lista")
```
### Comprobar si un elemento está en la lista
```python
lista = [1, 2, 3, 4, 5]
elemento = 3

if elemento in lista:
    print(f"{elemento} está en la lista")  # Imprime: 3 está en la lista
else:
    print(f"{elemento} no está en la lista")
```
```python
nombres = ["Diego", "Juan", "Maria"]
nombre = "Diego"
if nombre in nombres:
    print(f"{nombre} está en la lista - es un genio")
else:
    print(f"{nombre} no está en la lista")
```
### Ordenar la lista
```python
lista_compras = ["Leche", "Pan", "Huevos", "Manzanas"]
lista_compras.sort()
print(lista_compras)
```
---
# Funciones de las listas: 😎

- ## len(lista): Devuelve la longitud de la lista.
- ## list.count(elemento): Devuelve el número de veces que aparece un elemento en la lista.
- ## list.index(elemento): Devuelve el índice de la primera aparición de un elemento en la lista.
- ## list.reverse(): Invierte el orden de la lista.
- ## list.copy(): Crea una copia de la lista.
## Ejemplos de Funciones 

### Crear una lista de números 
```python
lista_numeros = [1, 2, 3, 4, 5]
```
### Calcular la suma de todos los números de la lista
```python
suma = sum(lista_numeros)
print(suma)  # Imprime: 15
```
### Encontrar el número máximo y mínimo de la lista
```python
maximo = max(lista_numeros)
minimo = min(lista_numeros)
print(maximo)  # Imprime: 5
print(minimo)  # Imprime: 1
```

### Multiplicar cada número de la lista por 2
```python
lista_numeros = [numero * 2 for numero in lista_numeros]
print(lista_numeros)  # Imprime: [2, 4, 6, 8, 10]
```
### Imprimir los números pares de la lista
```python
for numero in lista_numeros:
    if numero % 2 == 0:
        print(numero)  # Imprime: 2, 4, 6, 8, 10
```
---

# Operadores con listas: 😲
- ## +: Concatenar dos listas.
- ## *: Repetir una lista un número de veces.
- ## in: Comprobar si un elemento está en la lista.

### +: Concatenar dos listas. ➕
```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada)  # Imprime: [1, 2, 3, 4, 5, 6]
```
### *: Repetir una lista un número de veces. ♻
```python
lista = ["Hola"]
lista_repetida = lista * 3
print(lista_repetida)  # Imprime: ['Hola', 'Hola', 'Hola']
```
---

# Slicing: 🔪
## La operación de slicing en Python es una forma eficiente de extraer elementos de una secuencia, como una lista o una cadena de texto, de acuerdo con una cierta lógica.
### La sintaxis del slicing es la siguiente: secuencia[inicio:final:paso]
```python
numeros = [1, 2, 3, 4, 5]
sublista = numeros[:2]  #Obtener los dos primeros elementos de la lista "numeros"
print (sublista)
```
## Obtener los últimos tres elementos de la lista "nombres"
```python
nombres = ["Ana", "Juan", "María"]
sublista = nombres[-3:]
print (sublista)
sublista = nombres[0:2]
print (sublista)
```
## Obtener los elementos del 1 al 4 de la lista "mixta"
```python
sublista = mixta[1:4]
```
---
# Listas anidadas: 🧶
## Se pueden crear listas dentro de otras listas.
```python
lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
## Acceder a un elemento de la lista anidada
```
elemento = lista_anidada[1][2]
print (elemento)
```

## Iterar listas
```python
nombres = ["Ana", "Juan", "María","Diego","etc"]
for nombre in nombres:
  print (nombre)
else:
  print("no hay mas nombres en la lista")
```
## len(lista): Devuelve la longitud de la lista.
```python
nombres = ["Ana", "Juan", "María","Diego","etc"]
print(len(nombres))
```
## list.count(elemento): Devuelve el numero de veces que aparece un elemento en la lista.
```python
nombres = ["Ana", "Juan", "María","Diego","etc"]
print(nombres.count('Diego')) #1
print(nombres.count('Susanita')) #0 
```
## list.index(elemento): Devuelve el índice de la primera aparición de un elemento en la lista.
```python
print(nombres.index('Juan')) #1
```
## list.reverse(): Devuelve la lista con orden inverso
```python
nombres = ["Ana", "Juan", "María","Diego","etc"]
nombres.reverse()
print(nombres)
```
## list.copy(): Crea una copia de la lista.
```python
lista_original = ["Ana", "Juan", "María", "Diego", "etc"]
```
---
# Actividades 💬
## Ejercicio 1- Crear una lista de nombres y luego:
- ### Imprimir la longitud de la lista.
- ### Agregar un nuevo nombre al final de la lista.
- ### Eliminar el primer nombre de la lista.
- ### Buscar un nombre en la lista e imprimir si está o no presente.
- ### Ordenar la lista alfabéticamente.

## Ejercicio 2. Crear una lista de números y luego:

- ### Calcular la suma de todos los números de la lista.
- ### Encontrar el número máximo y mínimo de la lista.
- ### Multiplicar cada número de la lista por 2.
- ### Imprimir los números pares de la lista.

## Ejercicio 3. Crear una lista de palabras y luego:
- ### Contar cuántas veces aparece una palabra específica en la lista.
- ### Invertir el orden de la lista.
- ### Unir dos listas en una sola.
- ### Dividir una lista en dos sublistas.

## Ejercicio 4. Simular una cesta de la compra:

- ### Crear una lista con los productos que se van a comprar.
- ### Agregar un nuevo producto a la lista.
- ### Eliminar un producto de la lista.
- ### Imprimir la lista
---
[VOLVER](/readme.md)