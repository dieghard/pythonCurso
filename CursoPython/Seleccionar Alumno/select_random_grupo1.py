import pprint
import random
lista_alumnos = ["Monica","carlos", "guillermo","paula", "fermin", "javier", "Jonathan", "florencia", "leticia", "shirley", "emanuel", "pamela", "salvador"]
alumnos_pasados = ["Monica", "paula", "leticia","gonzalo", "maricel", "shirley", "guillermo"]
lista_alumnos = [alumno.upper() for alumno in lista_alumnos]
alumnos_restantes = [alumno for alumno in lista_alumnos if alumno not in alumnos_pasados]
#utilizamos una comprensión de lista para filtrar y crear una nueva lista llamada 
#alumnos_restantes a partir de la lista original lista_alumnos

lista_alumnos_seleccion = random.choice(alumnos_restantes)
pprint.pprint(lista_alumnos_seleccion)