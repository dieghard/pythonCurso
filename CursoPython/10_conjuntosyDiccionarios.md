# Diccionarios📚

## ¿Qué son los diccionarios?
Un diccionario en Python es una colección desordenada de elementos que se almacenan en pares clave-valor. Cada elemento tiene una clave única que se usa para acceder a su valor correspondiente.

### Caracteristicas de los diccionarios:
- Desordenados: Los elementos no tienen un orden fijo.
- Mutables: Puedes cambiar, agregar o eliminar pares clave-valor.
- Claves únicas: Las claves deben ser únicas dentro de un diccionario.
- Clave de cualquier tipo: Las claves pueden ser de cualquier tipo de dato inmutable.

## Sintaxis Basica de los diccionarios:

```python
# Definición de un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

#Tambien se puede de esta forma:
mi_diccionario = { "nombre" : "Juan", "edad" : 30, "ciudad" : "Madrid" }

```
---
### Metodos comunes de diccionarios:

- Acceder a los valores mediante sus claves:
```python
valor = mi_diccionario["nombre"]
print(valor)	# Imprime: Juan
```
- Agregar o modificar elementos:
```python
mi_diccionario["edad"] = 35
mi_diccionario["pais"] = "España"
print(mi_diccionario)	# Imprime: {"nombre": "Juan", "edad": 35, "ciudad": "Madrid", "pais": "España"}
```
- Eliminar elementos:
```python
del mi_diccionario["ciudad"]
print(mi_diccionario)	# Imprime: {"nombre": "Juan", "edad": 35, "pais": "España"}
```
- Verificar la existencia de una clave:
```python
if "edad" in mi_diccionario:
    print("La clave 'edad' existe en el diccionario.")
else:
    print("La clave 'edad' no existe en el diccionario.")
```
- Devolver todas las claves de un diccionario:
```python
claves = mi_diccionario.keys()
print(claves)	# Imprime: dict_keys(["nombre", "edad", "pais"])
```
- Devolver todos los valores de un diccionario:
```python
valores = mi_diccionario.values()
print(valores)	# Imprime: dict_values(["Juan", 35, "España"])
```
- Devolver todos los pares clave-valor de un diccionario:
```python
pares = mi_diccionario.items()
print(pares)	# Imprime: dict_items([("nombre", "Juan"), ("edad", 35), ("pais", "España")])
```
---
## Ejemplo de uso de un diccionario:
```python
# Definición de un diccionario
contacto = {
    "nombre": "Ana",
    "teléfono": "123-456-7890",
    "correo": "ana@example.com"
}

# Acceso a un valor
print(contacto["nombre"])  # Salida: Ana

# Modificación de un valor
contacto["teléfono"] = "098-765-4321"
print(contacto["teléfono"])  # Salida: 098-765-4321

# Agregar un nuevo par clave-valor
contacto["dirección"] = "Calle Falsa 123"
print(contacto)

# Eliminar un par clave-valor
del contacto["correo"]
print(contacto)

# Uso de métodos
print(contacto.keys())
print(contacto.values())
print(contacto.items())
```
---
# Conjuntos📑

## ¿Qué son los conjuntos?
Un conjunto en Python es una colección desordenada y mutable de elementos únicos. Esto significa que un conjunto no puede contener elementos duplicados.

### Caracteristicas de los conjuntos:
- Desordenados: Los elementos no tienen un orden fijo.
- Mutables: Puedes agregar o eliminar elementos.
- Elementos únicos: No se permiten duplicados.
- Tipos de elementos: Los elementos deben ser inmutables.

## Sintaxis básica de un conjunto:
Para definir un conjunto, se usan llaves {} o la función set(). Es importante recordar que para un conjunto vacío se debe usar set() ya que {} crea un diccionario vacío.
```python
# Definición de un conjunto
mi_conjunto = {1, 2, 3, 4, 5}

# Conjunto vacío
conjunto_vacio = set()
```
---
## Operaciones con conjuntos:
- Agregar elementos:
```python
mi_conjunto.add(6)
print(mi_conjunto)	# Imprime: {1, 2, 3, 4, 5, 6}
```
- Eliminar elementos:
```python
mi_conjunto.remove(3)
print(mi_conjunto)	# Imprime: {1, 2, 4, 5, 6}
```
- Verificar la existencia de un elemento:
```python
if 4 in mi_conjunto:
    print("El elemento 4 existe en el conjunto.")
else:
    print("El elemento 4 no existe en el conjunto.")
```
- Unir conjuntos:
```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2
print(union)  # Salida: {1, 2, 3, 4, 5}
```
- Interseccion de conjuntos:
La intersección de dos conjuntos contiene solo los elementos que están en ambos conjuntos.
```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
interseccion = conjunto1 & conjunto2
print(interseccion)  # Salida: {3}
```
- Diferencia de conjuntos: 
La diferencia de dos conjuntos contiene los elementos que están en el primer conjunto pero no en el segundo.
```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia = conjunto1 - conjunto2
print(diferencia)  # Salida: {1, 2}
```
- Diferencia simetrica de conjuntos:
La diferencia simétrica de dos conjuntos contiene los elementos que están en un conjunto pero no en ambos.
```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Salida: {1, 2, 4, 5}
```
---
## Metodos comunes de conjuntos:

- Definición
```python
mi_conjunto = {1, 2, 3}
```
- Agregar elementos
```python
mi_conjunto.add(4)
print(mi_conjunto)  # Salida: {1, 2, 3, 4}
```
- Eliminar elementos
```python
mi_conjunto.remove(2)
print(mi_conjunto)  # Salida: {1, 3, 4}
```
- Eliminar elemento aleatorio
```python
elemento = mi_conjunto.pop()
print(elemento)     # Salida: (un elemento aleatorio de {1, 3, 4})
print(mi_conjunto)  # Salida: (los elementos restantes en {1, 3, 4})
```
- Limpiar el conjunto
```python
mi_conjunto.clear()
print(mi_conjunto)  # Salida: set()
```
- Copiar un conjunto
```python
nuevo_conjunto = {5, 6, 7}
copia_conjunto = nuevo_conjunto.copy()
print(copia_conjunto)  # Salida: {5, 6, 7}
```
- Actualizar un conjunto
```python
conjunto_a = {1, 2, 3}
conjunto_b = {4, 5}
conjunto_a.update(conjunto_b)
print(conjunto_a)  # Salida: {1, 2, 3, 4, 5}
```
---
# Ejemplo completo de un Conjunto:
```python
# Definición de un conjunto
estudiantes = {"Ana", "Luis", "Pedro"}

# Agregar un nuevo estudiante
estudiantes.add("Maria")
print(estudiantes)  # Salida: {'Ana', 'Luis', 'Pedro', 'Maria'}

# Eliminar un estudiante
estudiantes.remove("Luis")
print(estudiantes)  # Salida: {'Ana', 'Pedro', 'Maria'}

# Comprobar si un estudiante está en el conjunto
print("Pedro" in estudiantes)  # Salida: True
print("Luis" in estudiantes)   # Salida: False

# Operaciones de conjuntos
grupo_a = {"Ana", "Pedro", "Carlos"}
grupo_b = {"Carlos", "Maria", "Jose"}

# Unión
print(grupo_a | grupo_b)  # Salida: {'Ana', 'Pedro', 'Carlos', 'Maria', 'Jose'}

# Intersección
print(grupo_a & grupo_b)  # Salida: {'Carlos'}

# Diferencia
print(grupo_a - grupo_b)  # Salida: {'Ana', 'Pedro'}

# Diferencia simétrica
print(grupo_a ^ grupo_b)  # Salida: {'Ana', 'Pedro', 'Maria', 'Jose'}
```
---
# Actividades 💬
- Escribe un programa que cuente la frecuencia de cada palabra en un texto dado.
- Crea un diccionario para almacenar la información de los estudiantes (nombre, edad, y calificación). Despues, realizá las siguientes acciones:
    - Agregar dos estudiantes.
    - Mostrar la información de todos los estudiantes.
    - Actualizar la calificación de uno de los estudiantes.
    - Mostrar la información actualizada de todos los estudiantes.
- Dada la siguiente lista de tuplas conviertela en un diccionario:
>lista = [("nombre", "Ana"), ("edad", 20), ("ciudad", "Madrid")]
- Dada una lista de números, elimina los duplicados utilizando conjuntos.
- Escribe un programa que me muestre los elementos repetidos en los siguientes dos conjuntos (Copia y pegalos en tu codigo).
> primer_conjunto = {1, 2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 17, 18, 21, 22, 23, 24, 25, 26, 28, 30, 31, 34, 35, 36, 39, 42, 44, 46, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 62, 64, 65, 66, 68, 69, 70, 71, 72, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 86, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99}
> segundo_conjunto = {1, 3, 4, 5, 6, 7, 8, 10, 11, 12, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 97, 98, 99}

---

[VOLVER](/pythonCurso/readme.md)