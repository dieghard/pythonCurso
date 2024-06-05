import random

# Listas de alumnos por grupo


grupo_1 = [
    "Agustin Abello", "Caritá Maricel Ana", "Fauda Fermin", "Dominguez Paula",
    "Mobilia Leticia", "Romero Mariana", "Carlos W Jimenez", "Miranda Florencia",
    "Buffoni Monica", "Ana Toledo", "Beltramone Maria Eugenia", "Cochrane Guillermo",
    "Javier Costamagna", "Shirley Janet Rodriguez", "Maria Andino",
    "Jonathan Gallardo", "Leonardo Tomas Acosta", "Gonzalo Gimenez" , "Gaspar Oddovero", "Diego Markiewicz"
]
grupo_1_paso = ["Monica Buffoni", "Dominguez Paula", "Mobilia Leticia", "Beltramone Maria Eugenia"]

grupo_2 = [
    "Dutto Santiago", "Daga Brisa", "Perna Emanuel",
    "Lorenzo Agustina", "Cristian Vincenti", "Pamela Gisela Izaguerre",
    "Marcelo Fenoglio", "Franco Ferreira Rodriguez", "Patricia Bosco",
    "Salvador Musso", "Pia Ferreira Rodriguez", "Sofia Dutto", "Franco Aguado",
    "Camila Casali", "Caritá Maricel Ana"
]
grupo_2_paso = ["Daga Brisa", "Sofia Dutto", "Caritá Maricel Ana"]
# Seleccionar un nombre al azar de cada grupo
alumno_azar_grupo_1 = random.choice(grupo_1)
alumno_azar_grupo_2 = random.choice(grupo_2)

# Imprimir los nombres seleccionados
#print(f"Alumno seleccionado al azar del Grupo 1: {alumno_azar_grupo_1}")
print(f"Alumno seleccionado al azar del Grupo 2: {alumno_azar_grupo_2}")