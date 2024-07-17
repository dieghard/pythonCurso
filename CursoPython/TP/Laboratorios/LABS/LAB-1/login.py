"""
Realizar un login que permita ingresar con varios usuarios y contraseñas.
"""

USUARIO = "Diego" 
PASSWORD = "Diego*123"

contador = 0

while True:
    
    ingrese_usuario = input("Ingrese el usuario a continuacion:")
    ingrese_pass = input("Ingrese el contraseña a continuacion:")

    if USUARIO == ingrese_usuario and PASSWORD == ingrese_pass:
        print("Bienvenido Usuario")
        break 
    else:
        print("Alguno de los Datos ingresados es incorrecto.")
        contador += 1
    if contador == 3:
        exit("Te quedaste sin intentos, vuelve a intentarlo en 30 segundos.")

