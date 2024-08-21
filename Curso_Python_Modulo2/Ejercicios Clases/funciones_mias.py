#FUNCIONES!!!!!!!!

import random
def seleccion(eleccion_user:bool | None = False )-> str:
    """Esta funcion me va a devolver Cara o Cruz seleccionada por la computadora"""
    numero_aleatorio = random.randint(1,2)
    if eleccion_user:
        numero_aleatorio = input("Selecciona CARA(1) o CRUZ(2) para jugar: ")

    eleccion_PC = "CRUZ"
    if numero_aleatorio == 1:  eleccion_PC = "CARA"
    return eleccion_PC

def terminar_juego():
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

def respuesta_juego(eleccion_usuario :str,eleccion_PC :str)->str:
    """Esta es una funcion que me va a devolver si el usuario gano, perdio """
    res =f"Perdiste!!!! Elejiste {eleccion_usuario} y la PC {eleccion_PC}"
    if eleccion_usuario == eleccion_PC :
        res = f"Ganaste!!!! Elejiste {eleccion_usuario} y la PC {eleccion_PC}"
    return res

def comprobacion_dig (texto_input:str|None= "Ingrese un numero:")-> int:
    """Va a comprobar si es un int y si no lo es va a pedir que ingrese lo pedido"""
    while True:
        numero = input(texto_input)
        if numero.isdigit():
            numero = int(numero)
            return numero
        else: 
            print("Pusiste cualquier cosa vuelve a intentarlo")    
    return


# Funciones para terminar

def terminar():
    """Este procedimiento me va a permitir terminar o continuar la operación"""
    continuar = True
    while continuar:
        pregunta = input("Quiere hacer otra operación? (S/n): ").upper()
        if  pregunta == "S" or  pregunta == "SI" :
            continuar = False
        elif  pregunta == "N" or   pregunta == "NO" :
                print("Gracias por confiar en nosotros, que le valla bien")
                exit()
        else : print ("Respuesta no valida")
    return
