#Realiza un juego de Piedra, Papel o Tijeras!!!
import random #Importamos la libreria RANDOM

numero_aleatorio = random.randint(1,3) #Generamos un numero random entre tres posibilidades (Piedra, papel o Tijeras)


if numero_aleatorio == 1: #Para que sea mas facil la logica, cambiamos los numeros por palabras
    eleccion_PC = "PIEDRA"
elif numero_aleatorio == 2:
    eleccion_PC = "PAPEL"
else:
    eleccion_PC = "TIJERA"

eleccion_usuario = input("Selecciona PIEDRA(1)[✊], PAPEL(2)[✋] o TIJERAS(3)[✌] para jugar: ") #Le pedimos al usuario ingresar su eleccion, dandole la opcion de escribir o ingresar el numero

eleccion_usuario = eleccion_usuario.upper() #Por si el usuario escribio en minuscula lo cambiamos a mayusculas

if eleccion_usuario == "1" or eleccion_usuario == "PIEDRA" or eleccion_usuario == "✊": #Para que sea mas facil la logica, cambiamos los numeros por palabras
    eleccion_usuario = "PIEDRA"
elif eleccion_usuario == "2" or eleccion_usuario == "PAPEL" or eleccion_usuario == "✋":
    eleccion_usuario = "PAPEL"
elif eleccion_usuario == "3" or eleccion_usuario == "TIJERAS" or eleccion_usuario == "✌":
    eleccion_usuario = "TIJERAS"
else:
    print("No elegiste una opcion valida")
    exit()



if eleccion_usuario == "PIEDRA"  and eleccion_PC == "PAPEL": #Comparamos las elecciones del usuario y la PC
    print(f"Perdiste!!!! Elejiste: {eleccion_usuario} y la PC: {eleccion_PC}")
elif eleccion_usuario == "PAPEL" and eleccion_PC == "TIJERAS":
    print(f"Perdiste!!!! Elejiste: {eleccion_usuario} y la PC: {eleccion_PC}")
elif eleccion_usuario == "TIJERAS" and eleccion_PC == "PIEDRA":
    print(f"Perdiste!!!! Elejiste: {eleccion_usuario} y la PC: {eleccion_PC}")
elif eleccion_usuario == eleccion_PC:
    print(f"Empate!!!! Elejiste: {eleccion_usuario} y la PC: {eleccion_PC}")
else:
    print(f"Ganaste!!!! Elejiste: {eleccion_usuario} y la PC: {eleccion_PC}")