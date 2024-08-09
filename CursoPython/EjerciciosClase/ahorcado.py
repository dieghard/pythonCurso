import random

palabras = ["manzana", "banana", "pera", "uva", "naranja"]
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
intentos = 6

print("¡Bienvenido al juego del ahorcado!")

while intentos > 0:
    palabra_actual = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_actual += letra
        else:
            palabra_actual += "_"
    print("Palabra:", palabra_actual)

    letra = input("Introduce una letra: ").lower()

    if letra in palabra_secreta:
        letras_adivinadas.append(letra)
        print("¡Correcto!")
    else:
        intentos -= 1
        print("Incorrecto. Te quedan", intentos, "intentos.")

    if "_" not in palabra_actual:
        print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
        break

if intentos == 0:
    print("¡Has perdido! La palabra era:", palabra_secreta)