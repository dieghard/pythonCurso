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

# Aplicar una función a cada elemento: Puedes aplicar una operación o función a cada elemento de la lista original.
lista_alumnos_mayuscula = [alumno.upper() for alumno in lista_alumnos]

# Crear listas de listas: Puedes crear listas de listas usando comprensiones anidadas.
lista_alumnos_longitud = [[alumno, len(alumno)] for alumno in lista_alumnos]

# Usar múltiples ciclos for: Puedes usar más de un ciclo for para generar listas a partir de múltiples iterables.
parejas_alumnos = [(alumno1, alumno2) for alumno1 in lista_alumnos for alumno2 in lista_alumnos if alumno1 != alumno2]

# Incluir un else: Aunque no es tan común, se puede incluir un bloque else en la comprensión de lista, pero esto suele hacerse más en comprensiones de listas que están aplicando una función o transformación a los elementos.
lista_transformada = [alumno.upper() if alumno[0].lower() < 'm' else alumno.lower() for alumno in lista_alumnos]