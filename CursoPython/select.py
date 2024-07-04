import random
lista_alumnos =  ["Gaspar", "Diego", "Camila", "Franco", "Brisa", "Agustin", "Cristian", "Pame"]

lista_pasaron = ["Camila", "Franco", "Brisa", "Agustin", "Cristian","Gaspar"]

lista_alumnos_iterable = lista_alumnos

seleccionado = random.choice(lista_alumnos)

for item_lista in lista_alumnos_iterable:
    for item_pasaron in lista_pasaron:
        if item_pasaron == seleccionado:
            lista_alumnos.remove(seleccionado)
            seleccionado=random.choice(lista_alumnos)
        else:
            continue
print(f"El alumno/a seleccionado es {seleccionado}")