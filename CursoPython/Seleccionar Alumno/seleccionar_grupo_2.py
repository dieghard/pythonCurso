import random
lista_alumnos = ["brisa","cristian", "emanuel", "franco"]
lista_alumnos = [alumno.upper() for alumno in lista_alumnos]

alumnos_pasados = ["brisa", "franco"]


alumnos_restantes = [alumno for alumno in lista_alumnos if alumno not in alumnos_pasados]
#utilizamos una comprensión de lista para filtrar y crear una nueva lista llamada 
#alumnos_restantes a partir de la lista original lista_alumnos

lista_alumnos_seleccion = random.choice(alumnos_restantes)
print(lista_alumnos_seleccion)