import pprint
lista_alumnos = ["Monica", "maricel", "carlos", "guillermo","paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia", "leticia", "shirley", "patricia", "marcelo"]
alumnos_con_indice = [(indice, alumno) for indice, alumno in enumerate(lista_alumnos)]
#print(alumnos_con_indice)
pprint.pprint(alumnos_con_indice)
