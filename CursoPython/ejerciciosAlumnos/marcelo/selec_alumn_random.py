import random
lista_alumnos = ["Monica", "maricel", "carlos", "guillermo" ]
#resto_alumnos = ["paula", "fermin", "gonzalo", "javier", "Jonathan", "florencia", "leticia", "shirley", "patricia", "marcelo"]
alumnos_pasados = []
largo_lista = len(lista_alumnos) - 1
continuar_seleccion = True

while True:
    while continuar_seleccion:
        rand = random.randint(0, largo_lista)
        alumno_seleccionado = lista_alumnos[rand]

        if alumnos_pasados == []:
            print(f"El alumno seleccionado es: {alumno_seleccionado}")
            alumnos_pasados.append(alumno_seleccionado)
            continuar_seleccion = False
        else:
            for alumno in alumnos_pasados:
                if alumno_seleccionado == alumno: #Si el alumno seleccionado es igual al alumno cargado anteriormente pasamos al while de nuevo
                    continuar_seleccion = True
                    break
                else:
                    print(f"El alumno seleccionado es: {alumno_seleccionado}")
                    alumnos_pasados.append(alumno_seleccionado)
                    print(alumnos_pasados)
                    break
        continuar_seleccion = False
        alumnos_pasados.sort()
        lista_alumnos.sort()
        if alumnos_pasados == lista_alumnos:
            exit("Ya no quedan alumnos para elegir")

    continuar = input("¿Desea seleccionar otro alumno?(s/n)")
    if continuar == "s":
        continuar_seleccion = True
    elif continuar == "n":
        continuar_seleccion = False
        break
    else:
        print("Opcion no valida")