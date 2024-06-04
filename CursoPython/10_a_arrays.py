# ¿Qué es un array en programación?
# Lo que es un array en programación (o arreglo) es: un dato estructurado que almacena un conjunto de datos homogéneo (todos del mismo tipo y relacionados). Cada uno de los elementos que componen un vector pueden ser:

# Simples: como caracteres, entero o real.
# Compuestos o estructurados: como son vectores, estructuras o listas.

#Creación de arrays: Puedes crear un array a partir de una lista, como se mostró anteriormente, o puedes usar funciones de NumPy como arange(), zeros(), ones(), linspace(), etc.

import numpy as np

array = np.array([1, 2, 3, 4, 5])  # Crear un array a partir de una lista
print (array)

array = np.arange(10)  # Crear un array con los números del 0 al 9
print (array)

array = np.zeros(5)  # Crear un array de ceros con 5 elementos
print (array)

array = np.ones(5)  # Crear un array de unos con 5 elementos
print (array)

array = np.linspace(0, 1, 5)  # Crear un array con 5 números espaciados uniformemente entre 0 y 1
print (array)

#Operaciones matemáticas: Puedes realizar operaciones matemáticas en todos los elementos de un array a la vez.

array = np.array([1, 2, 3, 4, 5])
print (array)

array = array + 1  # Sumar 1 a cada elemento
print (array)

array = array * 2  # Multiplicar cada elemento por 2
print (array)

array = np.sqrt(array)  # Calcular la raíz cuadrada de cada elemento
print (array)
#Operaciones de arrays: Puedes realizar operaciones entre arrays, como la suma, la resta, la multiplicación, etc.
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
suma = array1 + array2  # Sumar los arrays
resta = array1 - array2  # Restar los arrays
multiplicacion = array1 * array2  # Multiplicar los arrays

#Indexación y segmentación: Puedes acceder a elementos individuales de un array o a segmentos de un array.

array = np.array([1, 2, 3, 4, 5])
primer_elemento = array[0]  # Obtener el primer elemento
ultimo_elemento = array[-1]  # Obtener el último elemento
segmento = array[1:4]  # Obtener el segmento del segundo al cuarto elemento

#Funciones de agregación: Puedes calcular agregaciones como la suma, el promedio, el máximo, el mínimo, etc.

array = np.array([1, 2, 3, 4, 5])
suma = np.sum(array)  # Calcular la suma de los elementos
promedio = np.mean(array)  # Calcular el promedio de los elementos
maximo = np.max(array)  # Obtener el máximo de los elementos
minimo = np.min(array)  # Obtener el mínimo de los elementos

# AGREGAR DATOS
import numpy as np
# Crear un array inicial
array = np.array([1, 2, 3, 4, 5])
# Obtener la entrada del usuario
dato = input("Por favor, introduce un número: ")
# Convertir la entrada del usuario a un número
dato = float(dato)
# Agregar la entrada del usuario al array
array = np.append(array, dato)
print(array)  # Imprime el array con el nuevo dato

import numpy as np

# Crear un array inicial
array = np.array([])

# Agregar datos en un bucle while
while True:
    dato = input("Introduce un número (o 'salir' para terminar): ")

    if dato.lower() == 'salir':
        break

    dato = float(dato)
    array = np.append(array, dato)

print(array)  # Imprime el array con los nuevos datos
