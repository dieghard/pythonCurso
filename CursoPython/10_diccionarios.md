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

---

[VOLVER](/readme.md)