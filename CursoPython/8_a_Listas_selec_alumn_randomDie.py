import random
lista_alumnos = ["Monica", "maricel", "carlos", "guillermo","paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia", "leticia", "shirley", "patricia", "marcelo"]

alumnos_pasados = ["Monica", "maricel", "carlos", "guillermo","paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia"]

alumnos_restantes = [alumno for alumno in lista_alumnos if alumno not in alumnos_pasados]
#utilizamos una comprensión de lista para filtrar y crear una nueva lista llamada alumnos_restantes a partir de la lista original lista_alumnos

lista_alumnos_seleccion = random.choice(alumnos_restantes)
print(lista_alumnos_seleccion)

# Las comprensiones de lista en Python son una forma concisa de crear listas.
# POR EJEMPLO:

# Filtrar elementos: Se puede usar una condición para filtrar elementos de una lista original y crear una nueva lista solo con los elementos que cumplan esa condición.

nombres_con_p = [alumno for alumno in lista_alumnos if alumno.startswith('p')]

#Filtrar con múltiples condiciones:

#Queremos una lista de alumnos que tengan tanto la letra "a" como la "o" en su nombre. Podemos usar una comprensión de listas con dos condiciones:
alumnos_con_ao = [alumno for alumno in lista_alumnos if "a" in alumno and "o" in alumno]


# Aplicar una función a cada elemento: Se puede aplicar una operación o función a cada elemento de la lista original.
lista_alumnos_mayuscula = [alumno.upper() for alumno in lista_alumnos]

#Filtrar y aplicar una función:

#Queremos obtener una lista de los nombres de los alumnos en mayúscula que no estén en la lista de alumnos_pasados. Podemos combinar el filtrado con la aplicación de una función:
nombres_restantes_mayuscula = [alumno.upper() for alumno in alumnos_restantes if alumno not in alumnos_pasados]


# Crear listas de listas: Puedes crear listas de listas usando comprensiones anidadas.
lista_alumnos_longitud = [[alumno, len(alumno)] for alumno in lista_alumnos]

# Usar múltiples ciclos for: Puedes usar más de un ciclo for para generar listas a partir de múltiples iterables.
parejas_alumnos = [(alumno1, alumno2) for alumno1 in lista_alumnos for alumno2 in lista_alumnos if alumno1 != alumno2]

# Incluir un else: Aunque no es tan común, se puede incluir un bloque else en la comprensión de lista, pero esto suele hacerse más en comprensiones de listas que están aplicando una función o transformación a los elementos.
lista_transformada = [alumno.upper() if alumno[0].lower() < 'm' else alumno.lower() for alumno in lista_alumnos]

#Agrupar elementos por una condición:
#Queremos agrupar los alumnos por la primera letra de su nombre. Podemos usar una comprensión de listas :
alumnos_agrupados = []
for alumno in lista_alumnos:
  primera_letra = alumno[0]
  # Si la lista para la primera letra no existe, la creamos
  if len(alumnos_agrupados) <= ord(primera_letra) - ord('A'):
    alumnos_agrupados.extend([[] for _ in range(ord(primera_letra) - ord('A') + 1)])
  # Agregamos el alumno a la lista correspondiente
  alumnos_agrupados[ord(primera_letra) - ord('A')].append(alumno)
print(alumnos_agrupados)

# Crear una lista a partir de una range con pasos:
# Queremos crear una lista de números del 1 al 100 pero con saltos de 2.
# Podemos usar una comprensión de listas con la función range:

numeros_con_salto = [numero for numero in range(1, 101, 2)]
print(numeros_con_salto)
# Obtener el índice y el elemento de una lista:
# Queremos crear una lista de tuplas donde cada tupla contenga el índice y el elemento de la lista original. Podemos usar la función enumerate:

alumnos_con_indice = [(indice, alumno) for indice, alumno in enumerate(lista_alumnos)]
print(alumnos_con_indice)

# Usar una condición "else":

# Queremos crear una lista donde los nombres que comiencen con "M" estén en minúscula y los demás en mayúscula. Podemos usar una condición "else":
nombres_mayuscula_minuscula = [alumno.lower() if alumno[0] == "M" else alumno.upper() for alumno in lista_alumnos]
print(nombres_mayuscula_minuscula)

# Uso de la función pprint (pretty print):
import pprint
lista_alumnos = ["Monica", "maricel", "carlos", "guillermo","paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia", "leticia", "shirley", "patricia", "marcelo"]
alumnos_con_indice = [(indice, alumno) for indice, alumno in enumerate(lista_alumnos)]
#print(alumnos_con_indice)
pprint.pprint(alumnos_con_indice)
