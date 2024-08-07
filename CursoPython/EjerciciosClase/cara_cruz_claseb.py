#Realiza un juego de cara o cruz

import random #Importamos la libreria RANDOM

def seleccion(eleccion_user:bool | None = False )-> str:
    """Esta funcion me va a devolver Cara o Cruz seleccionada por la computadora"""
    numero_aleatorio = random.randint(1,2)
    if eleccion_user:
        numero_aleatorio = input("Selecciona CARA(1) o CRUZ(2) para jugar: ")

    eleccion_PC = "CRUZ"
    if numero_aleatorio == 1:  eleccion_PC = "CARA"
    return eleccion_PC

def terminar():
    """Este procedimiento me va a permitir terminar el juego o seguir jugando"""
    continuar_juego = True
    while continuar_juego:
        pregunta = input("Quieres jugar de nuevo? (S/n): ").upper()
        if  pregunta == "S" or  pregunta == "SI" :
            continuar_juego = False
        elif  pregunta == "N" or   pregunta == "NO" :
                print("Gracias por jugar")
                exit()
        else : print ("Respuesta no valida")
    return

def respuesta(eleccion_usuario :str,eleccion_PC :str)->str:
    """Esta es una funcion que me va a devolver si el usuario gano, perdio """
    res =f"Perdiste!!!! Elejiste {eleccion_usuario} y la PC {eleccion_PC}"
    if eleccion_usuario == eleccion_PC :
        res = f"Ganaste!!!! Elejiste {eleccion_usuario} y la PC {eleccion_PC}"
    return res

while True:
    eleccion_PC  = seleccion()
    eleccion_usuario = seleccion(True)
    print(respuesta(eleccion_usuario,eleccion_PC))
    terminar()
