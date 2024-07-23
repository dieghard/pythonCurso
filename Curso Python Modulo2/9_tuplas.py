#Tuplas en Python
# Las tuplas en Python son un tipo de dato inmutable que se utiliza para almacenar una colección ordenada de elementos. Son similares a las listas, pero no se pueden modificar una vez creadas.
# Para crear una tupla, se utilizan paréntesis y se separan los elementos por comas. Por ejemplo:
# Tupla con un solo elemento
tupla_1 = ("Hola",)

# Tupla con dos elementos
tupla_2 = ("Hola", "Mundo")

# Tupla con tres elementos
tupla_3 = ("Hola", "Mundo", "!")

# Las tuplas se pueden usar para almacenar cualquier tipo de dato, como números, cadenas, listas, diccionarios, etc.

# Las tuplas tienen las siguientes ventajas:

# Son inmutables: Esto significa que no se pueden modificar una vez creadas. Esto puede ser útil para garantizar la integridad de los datos.
# Son eficientes: Las tuplas son más eficientes que las listas en términos de memoria y velocidad.
# Son compatibles con la indexación: Se puede acceder a los elementos de una tupla por su índice.
# Las tuplas tienen las siguientes desventajas:

# Son inmutables: Esto significa que no se pueden modificar una vez creadas. Esto puede ser un inconveniente si necesitas modificar los datos.
# No son tan flexibles como las listas: Las listas se pueden modificar, mientras que las tuplas no.
# En general, las tuplas son una buena opción para almacenar colecciones de datos que no necesitan ser modificadas.

# Aquí hay algunos ejemplos de cómo se pueden usar las tuplas:

# Almacenar información sobre una persona:

persona = ("Juan", "Pérez", 30)
# Almacenar las coordenadas de un punto:

punto = (10, 20)
# Almacenar los resultados de una función:

def sumar(a, b):
    return a + b

resultado = sumar(1, 2)

print(resultado)  # Salida: 3