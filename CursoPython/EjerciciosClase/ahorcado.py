import random
#Funciones y procedimientos
#Datos Usuario
#Añadir Puntaje


print("¡Bienvenido al juego del ahorcado!")
puntaje = 0
palabras = ["manzana", "banana", "pera", "uva", "naranja"]
intentos = 6
            
def juego():
    #Variables
    global intentos
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    
    while intentos > 0:
        palabra_actual = verificacion_palabra(palabra_secreta, letras_adivinadas)    
        print("Palabra:", palabra_actual)
        
        validar = verificacion_letra(palabra_secreta,letras_adivinadas,palabra_actual)
        
        if not validar:
            intentos -= 1
            print(f"Incorrecto. {nombre} te quedan {intentos} intentos.")
    
    if intentos == 0:
        print(f"¡{nombre} has perdido! La palabra era: {palabra_secreta}")
        seguir_jugando()
    return

def verificacion_letra(palabra_secreta, letras_adivinadas,palabra_actual):
    letra = input("Introduce una letra: ").lower()
    verificar = True
    if letra in palabra_secreta:
        letras_adivinadas.append(letra)
        print("¡Correcto!")
    else:
        verificar = False
        
    if "_" not in palabra_actual:
        global puntaje
        puntaje += 1
        print(f"¡Felicidades {nombre}! Has adivinado la palabra: {palabra_secreta}. \n Tu puntaje acumulado es {puntaje}")
        seguir_jugando()
    return verificar 

def verificacion_palabra(palabra_secreta, letras_adivinadas):
    palabra_actual = "" 
    for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_actual += letra
            else:
                palabra_actual += "_"
    return  palabra_actual

def seguir_jugando():
    continuar_juego = input("Deseas seguir jugando(S/N): ").capitalize()
    if continuar_juego == "S":
        juego()
    else:
        print(f"Gracias {nombre} por jugar!")
    return

menu = input("¿Deseas Jugar o Ver las configuraciones? (Jugar/Config)").lower()
if not menu == "jugar":
    agregar = True
    config_intentos = input("¿Quieres modificar la cantidad de intentos? Pon No o la cantidad de intentos nueva:").capitalize()
    if not config_intentos == "No":
        intentos = int(config_intentos)
    print(f"La cantidad de intentos será {intentos}")
    while agregar:
        config_agregar = input("¿Quieres agregar más palabras a la lista? (S/N)").capitalize()
        if config_agregar == "S":
            palabras.append(input("Escribe la palabra a continuacion: ").lower())
            print(palabras)
        else: 
            agregar = False
    print("Saliendo de las configuraciones")
    nombre = input("Ingrese el nombre del jugador:")
    juego()
            
else:
    nombre = input("Ingrese el nombre del jugador:")
    juego()
    