import random
lista_alumnos = ["Monica", "maricel", "carlos", "guillermo","paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia", "leticia", "shirley", "patricia", "marcelo"]

alumnos_pasados = ["Monica", "maricel", "carlos", "guillermo","paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia"]

alumnos_restantes = [alumno for alumno in lista_alumnos if alumno not in alumnos_pasados]
#utilizamos una comprensión de lista para filtrar y crear una nueva lista llamada alumnos_restantes a partir de la lista original lista_alumnos

lista_alumnos_seleccion = random.choice(alumnos_restantes)
print(lista_alumnos_seleccion)
