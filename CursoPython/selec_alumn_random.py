import random

lista_alumnos = ["Monica", "maricel", "carlos", "guillermo", "paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia", "leticia", "shirley", "patricia", "marcelo"]

alumnos_pasados = [ "leticia", "shirley", "patricia", "marcelo"]

largo_lista = len(lista_alumnos) - 1

while True:
    rand = random.randint(0, largo_lista)
    alumno_seleccionado = lista_alumnos[rand]
    if alumnos_pasados == []:
        print(f"El alumno seleccionado es: {alumno_seleccionado}")
        alumnos_pasados.append(alumno_seleccionado)
        break
    else:
        for alumno in alumnos_pasados:
            if alumno_seleccionado == alumno:
                print(f"el alumno ya fue seleccionado")
            else:
                print(f"El alumno seleccionado es: {alumno_seleccionado}")
                alumnos_pasados.append(alumno_seleccionado)
                break
    break