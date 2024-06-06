import random
cara_o_cruz = random.randint (1,2)
resultado_final = cara_o_cruz
cara = 1
cruz = 2


nombre = input("Ingresa tu nombre: ")
jugar_compu_o_persona = input("Ingresa '1' si quieres jugar contra la computadora o '2' si juegas contra un amigo:  ")
jugar_compu = ("1")
jugar_amigo = ("2")

#jugar compu
if jugar_compu_o_persona == 1:
    print(f"Comencemos haz eleguido jugar contra mí, estas listo {nombre}?")
cara_o_cruz_compu = random.randint (1,2)
resultado_compu = random.randint
cara = 1
cruz = 2

if resultado_compu == cara:
    print(f"Elegí Cara, te toca {nombre}")
else:
    print(f"Elegí Cruz, te toca {nombre}")
jugar_contra_compu = input("ingresa cara o cruz {nombre}: ")

if resultado_compu ==  resultado_final:
    print(f"El resultado final es {resultado_final}")
    print(f"Te gané, tal vez la proxima....😉🤭")

if jugar_contra_compu == resultado_final:
    print(f"El resultado es {resultado_final}")
    print(f"Me ganaste, esta vez😏")

if not resultado_compu == resultado_final and jugar_contra_compu == resultado_final:
    print("Ambos perdimos😢")
else:
    print(f"Ganamos, que copion que sos😉🤭")

#Jugar amigo
if jugar_compu_o_persona == 2:
    print(f"Ahora te vamos a pedir unos datos")
jugador_2 = input("Ingresar el nombre de tu amigo: ")
jugador_1 = {nombre}
jugador_1 = input("{jugador_1} ingresa Cara o Cruz: ")
jugador_2 = input("{jugador_2} elegí si Cara o Cruz:")

if jugador_1 == resultado_final:
    print(f"Ganó {jugador_1}, felicidades!!!")
if jugador_2 == resultado_final:
    print(f"Ganó {jugador_2}, felicidades!!!")






