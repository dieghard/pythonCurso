import random

# Listas de alumnos por grupo
grupo_1 = [
    "Pantaleo Patricio", "Caritá Maricel Ana", "Fauda Fermin", "Dominguez Paula",
    "Mobilia Leticia", "Romero Mariana", "Carlos W Jimenez", "Miranda Florencia",
    "Buffoni Monica", "Ana Toledo", "Ortiz Ana Belen", "Cochrane Guillermo",
    "Javier Costamagna", "Shirley Janet Rodriguez", "Maria Andino",
    "Jonathan Gallardo", "Leonardo Tomas Acosta", "Gonzalo Gimenez"
]

grupo_2 = [
    "Beltramone Maria Eugenia", "Dutto Santiago", "Daga Brisa", "Perna Emanuel",
    "Lorenzo Agustina", "Cristian Vincenti", "Pamela Gisela Izaguerre",
    "Marcelo Fenoglio", "Franco Ferreira Rodriguez", "Patricia Bosco",
    "Salvador Musso", "Pia Ferreira Rodriguez", "Sofia Dutto", "Franco Aguado",
    "Camila Casali", "Agustin Abello"
]

# Seleccionar un nombre al azar de cada grupo
alumno_azar_grupo_1 = random.choice(grupo_1)
alumno_azar_grupo_2 = random.choice(grupo_2)

# Imprimir los nombres seleccionados
print(f"Alumno seleccionado al azar del Grupo 1: {alumno_azar_grupo_1}")
print(f"Alumno seleccionado al azar del Grupo 2: {alumno_azar_grupo_2}")