#Realiza un juego de cara o cruz

import random #Importamos la libreria RANDOM

numero_aleatorio = random.randint(1,2) #Generamos un numero random entre dos posibilidades ya que las monedas solo tienen dos formas de caer


if numero_aleatorio == 1: #Para que sea mas facil la logica, cambiamos los numeros por palabras
    eleccion_PC = "CARA"
else: #Si numero_aleatorio es 2:
    eleccion_PC = "CRUZ"

eleccion_usuario = input("Selecciona CARA(1) o CRUZ(2) para jugar: ") #Le pedimos al usuario ingresar su eleccion, dandole la opcion de escribir o ingresar el numero

eleccion_usuario = eleccion_usuario.upper() #Por si el usuario escribio en minuscula lo cambiamos a mayusculas

if eleccion_usuario == "1" or eleccion_usuario == "CARA": #Para que sea mas facil la logica, cambiamos los numeros por palabras
    eleccion_usuario = "CARA"
elif eleccion_usuario == "2" or eleccion_usuario == "CRUZ":
    eleccion_usuario = "CRUZ"
else: 
    print("Pusiste otra cosa") #Si el usuario no coloco 1, 2, Cara o Cruz pasa de largo y termina el programa
    exit()


if eleccion_usuario == "CARA"  and eleccion_PC == "CRUZ":
    print(f"Ganaste!!!! Elejiste {eleccion_usuario} y la PC {eleccion_PC}")

elif eleccion_usuario == "CRUZ" and eleccion_PC == "CARA":
    print(f"Ganaste!!!! Elejiste {eleccion_usuario} y la PC {eleccion_PC}")

elif eleccion_usuario == eleccion_PC:
    print(f"Empate!!!! Elejiste {eleccion_usuario} y la PC {eleccion_PC}")

else:
    print(f"Perdiste!!!! Elejiste {eleccion_usuario} y la PC {eleccion_PC}")