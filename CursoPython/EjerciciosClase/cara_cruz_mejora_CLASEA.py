#Realiza un juego de cara o cruz

import random #Importamos la libreria RANDOM

def eleccion(eleccion_pc: bool |None = True)-> str:
    """
    Esta funcion me va a permitir elegir entre cara o cruz
    y la reutilizo tanto para la eleccion de la computadora
    como la del usuario. Si no le paso ningun parametro, la variable se va a cargar con datos Random.
    """
    if eleccion_pc:
        numero_aleatorio = random.randint(1,3) #Generamos un numero random entre dos posibilidades ya que las monedas solo tienen dos formas de caer
    else:
        numero_aleatorio = int(input("Selecciona CARA(1) o CRUZ(2): "))

    if numero_aleatorio == 1: #Para que sea mas facil la logica, cambiamos los numeros por palabras
        eleccion_pc_user = "CARA"
    elif numero_aleatorio == 2: #Si numero_aleatorio es 2:
        eleccion_pc_user = "CRUZ"
    elif numero_aleatorio == 3: #Si numero_aleatorio es 2:
        eleccion_pc_user = "CANTO"
    else:
        print("Ingreso mal el numero!")
        eleccion_pc_user = "error"
    return eleccion_pc_user

def respuesta(eleccion_usuario :str|None = "CARA",eleccion_PC:str |None ="CARA" )-> str:
    """ Esta función devolvera la respuesta de si el usuario gano o perdio
    eleccion_usuario esta variable es la que eligio el usuario y esta variable es la que eligio la pc eleccion_PC
    """
    res = "Perdiste!!!! "
    if eleccion_usuario ==  eleccion_PC :
        res = f"Ganaste!!!! Elejiste {eleccion_usuario} y la PC {eleccion_PC}"
    return res

while True:
    eleccion_usuario = eleccion(False)
    eleccion_PC = eleccion(True)

    # resultado = respuesta(eleccion_PC,eleccion_usuario)
    resultado = respuesta()

    print(resultado )
    pregunta = input("¿Desea volver a jugar (S/N)")
    if pregunta.upper() == 'N' or pregunta.upper() == 'NO'  :
        break
