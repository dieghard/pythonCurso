# Generadores de Expresiones en Python
# Los generadores de expresiones son una característica poderosa y eficiente en Python para crear secuencias de datos de manera concisa.
# Son similares a las "comprensiones de lista", pero con algunas diferencias clave en términos de sintaxis y comportamiento.
#  A diferencia de las listas, que almacenan todos los elementos a la vez, los generadores liberan memoria al generar elementos uno a uno.
# Esto los hace ideales para trabajar con grandes conjuntos de datos o cuando la memoria es limitada.
# Sintaxis Básica
# La sintaxis de un generador de expresiones es:

# (expresion for item in iterable [if condicion])

# expresion: Es el valor que se generará para cada item.
# item: Variable que toma cada valor del iterable.
# iterable: Secuencia sobre la que se itera.
# if condicion: (Opcional) Filtro para incluir solo ciertos elementos.

# Características Principales

# Paréntesis: Usan paréntesis () en lugar de corchetes [] 
# (que se usan en comprensiones de lista).
# Evaluación Perezosa: Los valores se generan solo cuando se solicitan, lo que ahorra memoria.
# Uso Único: Una vez que se han consumido todos los elementos, el generador se agota y no puede reutilizarse.
# Eficiencia de Memoria: Ideal para trabajar con grandes conjuntos de datos o secuencias infinitas.

#Ejemplos


texto = "Este es un ejemplo de texto con palabras clave."
palabras_clave = ["ejemplo", "texto", "clave"]

palabra_detectada = next(palabra   for palabra in palabras_clave if palabra in texto)
#                       (expresion for item     in iterable      [if condicion]     )
# expresion: Es el valor que se generará para cada item.
# item: Variable que toma cada valor del iterable.
# iterable: Secuencia sobre la que se itera.
# if condicion: (Opcional) Filtro para incluir solo ciertos elementos.

print(f"Palabra detectada: {palabra_detectada}")  # Salida: Palabra detectada: ejemplo

cuadrados = (x**2 for x in range(10))
# PARA IMRIMIRLOS:
# Definimos el generador de expresiones
cuadrados = (x**2 for x in range(10))
# Método 1: Usando un bucle for
print("Método 1: Usando un bucle for")
for cuadrado in cuadrados:
    print(cuadrado, end=" ")
print("\n")

# Nota: El generador se ha agotado después del bucle for anterior
# Para los siguientes métodos, necesitamos recrear el generador
cuadrados = (x**2 for x in range(10))
# Método 2: Convertir a lista y luego imprimir
print("Método 2: Convertir a lista y luego imprimir")
lista_cuadrados = list(cuadrados)
print(lista_cuadrados)

# Método 3: Usar la función print con desempaquetado
cuadrados = (x**2 for x in range(10))  # Recreamos el generador
print("Método 3: Usar la función print con desempaquetado")
print(*cuadrados)

# Método 4: Usar comprension de lista en print (crea una lista temporal)
cuadrados = (x**2 for x in range(10))  # Recreamos el generador
print("Método 4: Usar comprension de lista en print")
print([x for x in cuadrados])

# Método 5: Usar join con map (para grandes conjuntos de datos)
cuadrados = (x**2 for x in range(10))  # Recreamos el generador
print("Método 5: Usar join con map")
print(", ".join(map(str, cuadrados))) # Abajo se expolica el uso de map y join
#La función map toma dos argumentos: una función y un iterable. En este caso, 
# 
# la función str convierte cada número al cuadrado en una cadena de texto. 
# El resultado es un nuevo iterable que contiene las cadenas de texto de los cuadrados.
numeros_como_strings = map(str, cuadrados)
# Usar join:
# La función join concatena elementos de un iterable en una cadena, 
# separándolos por un delimitador especificado. En este caso, utilizamos , como delimitador para unir las cadenas de texto de los cuadrados.
resultado = ", ".join(numeros_como_strings)
print(resultado)



#Generador de números pares:
pares = ((i, i**2) for i in range(4))

# 4. Generador con filtro:

# Este generador filtra los números pares del 0 al 10:
pares_filtrados = (x for x in range(100) if x % 5 == 0)
print(*pares_filtrados)


# Comprensiones de listas:

# Crean listas: Su objetivo principal es crear una lista de elementos en memoria.
# Sintaxis más concisa: Utilizan una sintaxis compacta similar a las listas para definir la lógica de creación.
# Eficiencia para conjuntos de datos pequeños: Adecuadas para conjuntos de datos pequeños que caben en la memoria.
# Resultado completo: Almacenan la lista completa en la memoria antes de devolverla.
# VS
# Generadores de expresiones:

# Crean iterables: Su objetivo principal es generar elementos uno a uno, sin almacenar toda la secuencia.
# Sintaxis similar a las comprensiones de listas: Utilizan una sintaxis similar a las comprensiones de listas,
# pero con paréntesis en lugar de corchetes o llaves.
# Eficiencia para conjuntos de datos grandes: Ideales para procesar grandes conjuntos de datos de forma iterativa, liberando memoria.
# Resultado progresivo: Devuelven un objeto iterable que genera elementos uno a uno, sin almacenar la secuencia completa.
#EJEMPLO
#Crear una lista de cuadrados de 1 a 10:
#Comprensión de lista:
cuadrados_lista = [x**2 for x in range(1, 110000)]
print(*cuadrados_lista)
#Generador de expresión:
cuadrados_generador = (x**2 for x in range(1, 110000))
print(*cuadrados_generador)


