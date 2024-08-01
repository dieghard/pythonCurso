import random
numero_compu = random.randint(0,10)
numero_computadora = numero_compu
contador = 0
seguir = True

nombre_jugador = input("Ingresa tu nombre: ")
adivino_primer_intento = f"Felicidades {nombre_jugador} sos un genio, acertaste en la primera🤭🎆✨"
adivino_segundo_intento = f"Muy bien {nombre_jugador}!!!🤗🤩"
adivino_tercer_intento = f"Haz acertado {nombre_jugador}, pero creo que lo puedes hacer mejor🤭😏"

perdio_primer = f"Que lastima {nombre_jugador} , haz fallado pero puedes intentarlo 2 veces más"
perdio_segunda = f"Hooo no puedes adivinarme {nombre_jugador}??? Pensé que eras más inteligente, te queda 1 intento"
perdio_tercero = f"Haz fallado {nombre_jugador}, tal vez solo tal vez la proxima puedas. El resultado era {numero_computadora}"


while True:
    numero_jugador = input("Ingresa el número que crees que tengo en mente entre o y 10: ")
    contador += 1
    if numero_computadora == numero_jugador :
        print(f"¡Felicidades {nombre_jugador}! Has adivinado el número en {contador} intentos")
        seguir = False
        exit()
    if contador == 1:
        print(perdio_primer)
    if  contador == 2:
        print(perdio_segunda)
    if  contador == 3 :
        print(perdio_tercero)
    if contador >= 3:
        seguir = False

print(f"El número que tenía en mente es {numero_computadora} ")
print(f"Espero te haya gustado jugar conmigo🤗😉")


