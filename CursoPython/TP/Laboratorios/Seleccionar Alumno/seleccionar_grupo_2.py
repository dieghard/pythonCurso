import random
listas = ["Diego","Gaspar","Pame","Agustin","Brisa", "Cristian","Camila","Franco", "Emanuel"]

seleccionado = random.choice(listas)

listas_seleccionadas = ["Brisa","Pame"]

recorrido = listas

if (listas_seleccionadas == listas):
    print("No hay mas alumnos para seleccionar")
    exit()

for item_lista in recorrido:
    for item_lista_seleccionado in listas_seleccionadas:
        if item_lista_seleccionado == seleccionado:
            listas.remove(seleccionado)
            seleccionado=random.choice(listas)
        else:
            continue
print(f"El alumno/a suertudo para salir a programar es {seleccionado}")

#for lista in listas:
    #print(lista)