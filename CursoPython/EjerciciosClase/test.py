lista_nombres = ["Ana", "Pedro", "María"] 

tuplas_numeros = (10,20,30) 

diccionario_edades = {"Ana": 25, "Gaspar": 23, "Roberto":45, "Maria":84}

conjunto_colores = {"Azul", "Rojo", "Verde"}
"""
print(f"Esto tiene la lista de nombres en su interior {lista_nombres}")
print(f"Esto tiene la tupla de numeros en su interior {tuplas_numeros}")
print(f"Esto tiene el diccionario de nombres en su interior {diccionario_edades}")
print(f"Esto tiene el conjunto de colores en su interior {conjunto_colores}")
"""


print(f"Esto tiene la lista de nombres en su interior {lista_nombres[0]}")
print(f"Esto tiene la tupla de numeros en su interior {tuplas_numeros[2]}")
print(f"Esto tiene el diccionario de nombres en su interior {diccionario_edades["Ana"]}") # No se puede acceder a sus datos mediante indice, solamente con su clave valor
# print(f"Esto tiene el conjunto de colores en su interior {conjunto_colores[1]}") # No se puede acceder a sus datos mediante indice