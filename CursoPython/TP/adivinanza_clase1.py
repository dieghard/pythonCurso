# ! un programa que adivina un número secreto y nos de 3 # intentos para adivinarlo- El numero va a ser del 1 al 10
import random

print("""
                                ٩(͡๏̯͡๏)۶

. +   .       ' .      '    * `     .      .     '  )    .   +        *       .     '  )    .   +        *
:::'###::::'########::'####:'##::::'##:'####:'##::: ##::::'###::::'##::: ##:'########::::'###::::
::'## ##::: ##.... ##:. ##:: ##:::: ##:. ##:: ###:: ##:::'## ##::: ###:: ##:..... ##::::'## ##:::
:'##:. ##:: ##:::: ##:: ##:: ##:::: ##:: ##:: ####: ##::'##:. ##:: ####: ##::::: ##::::'##:. ##::
'##:::. ##: ##:::: ##:: ##:: ##:::: ##:: ##:: ## ## ##:'##:::. ##: ## ## ##:::: ##::::'##:::. ##:
 #########: ##:::: ##:: ##::. ##:: ##::: ##:: ##. ####: #########: ##. ####::: ##::::: #########:
 ##.... ##: ##:::: ##:: ##:::. ## ##:::: ##:: ##:. ###: ##.... ##: ##:. ###:: ##:::::: ##.... ##:
 ##:::: ##: ########::'####:::. ###::::'####: ##::. ##: ##:::: ##: ##::. ##: ########: ##:::: ##:
..:::::..::........:::....:::::...:::::....::..::::..::..:::::..::..::::..::........::..:::::..::
                               ( ( (
                                ) ) )
                               ( ( (
                             '. ___ .'
                            '  (> <) '
                    --------ooO-(_)-Ooo----------


""")
print("")
input("Presione ENTER tecla para continuar...") # Esperar a que el usuario presione una tecla
# Limpiar la pantalla
print("\n"*50)



saludo_1="Hola genio , bienvenido al juego de las adivinzas, en esta oportunidad vas a tener 3 intentos para adivinar el numero secreto que pensé, el numero va a ser del 1 al 10"

saludo_2="Hola Astro... todo bien? jugamos?"

saludo_3="Hola gros@, vamos a jugar a adivinar el numero secreto que pensé, el numero va a ser del 1 al 10"
saludoselecciondo= random.randint(1,3)
if saludoselecciondo == 1:
    saludo_seleccionado = saludo_1
elif saludoselecciondo == 2:
    saludo_seleccionado = saludo_2
else:
    saludo_seleccionado = saludo_3

numero_secreto =  random.randint(1,10)
print (saludo_seleccionado)
nombre_usuario = input("¿Como te llamas?: ")
numero_seleccionado_x_usuario = input("Ingrese el numero a adivinar del 1 al 10: ")
mensaje_error_1 = f" {nombre_usuario}!!! te dije que ingreses un numero del 1 al 10, volvé a empezar 🤦‍♂   ️"
# Primer intento
#Validacion de que se un numero y no letras
if numero_seleccionado_x_usuario.isdigit():
    numero_seleccionado_x_usuario = int(numero_seleccionado_x_usuario )
else:
    print(mensaje_error_1)
    exit()
# validacion de que este entre el rango permitido
if numero_seleccionado_x_usuario <1 or  numero_seleccionado_x_usuario >10:
    mensaje_error_1
    exit()

#Primera oportunidad
if numero_secreto == numero_seleccionado_x_usuario:
    print(f"Felicidades {nombre_usuario}✌️🪄, adivinaste el número  secreto DE UNA CAMPEON")
    exit()
else:
    print(f"Lo siento {nombre_usuario} 😗, no adivinaste el número secreto, volve a intentarlo 🚀")
    diferencia = numero_secreto - numero_seleccionado_x_usuario
    if diferencia == 2 or diferencia == -2:
        print(f"peeeero esta bastante caliente, caliente 🚀 dale {nombre_usuario} vos podes")
    if diferencia == 4 or diferencia == -4:
        print(f"peeeero esta bastante tibio, tibio 🧐, {nombre_usuario} tenes 2 oportunidades mas")
    if diferencia > 4 or diferencia < -4:
        print(f"Bastante helado 🧐 {nombre_usuario} mejora la punteria")

#segunda oportunidad
numero_seleccionado_x_usuario = input("Ingrese por segunda vez el numero a adivinar: ")
#Validacion de que se un numero y no letras
if numero_seleccionado_x_usuario.isdigit():
    numero_seleccionado_x_usuario = int(numero_seleccionado_x_usuario )
else:
    print(f"{nombre_usuario} te dije que ingreses un numero del 1 al 10, volvé a empezar 🤦‍♂   ️")
    exit()

# validacion de que este entre el rango permitido
if numero_seleccionado_x_usuario <1 or  numero_seleccionado_x_usuario >10:
    print(f"{nombre_usuario} te dije que ingreses un numero del 1 al 10, volvé a empezar 🤦‍♂   ️")
    exit()

if numero_secreto == numero_seleccionado_x_usuario:
    print(f"Felicidades {nombre_usuario} ✌️🪄, adivinaste el número secreto la segunda vez GRANDE GENIO!!!!!")
    exit()
else:
    print(f"Lo siento {nombre_usuario} 😗, no adivinaste el número secreto, volve a intentarlo 🚀, te queda una ultima oportunidad!!!!")
    diferencia = numero_secreto - numero_seleccionado_x_usuario
    if diferencia == 2 or diferencia == -2:
        print(f"{nombre_usuario} le erraste peeeero esta bastante caliente, caliente 🚀")
    if diferencia == 4 or diferencia == -4:
        print(f"{nombre_usuario} le erraste peeeero esta bastante tibio, tibio 🧐")
    if diferencia > 4 or diferencia < -4:
        print(f"{nombre_usuario} le erraste por bastante pq estas bastante helado 🧐")

#tercera oportunidad
numero_seleccionado_x_usuario = input("Ingrese por tercera vez el numero a adivinar: ")
#Validacion de que se un numero y no letras
if numero_seleccionado_x_usuario.isdigit():
    numero_seleccionado_x_usuario = int(numero_seleccionado_x_usuario )
else:
    print("Te dije que ingreses un numero del 1 al 10, volvé a empezar 🤦‍♂  ️")
    exit()

# validacion de que este entre el rango permitido
if numero_seleccionado_x_usuario <1 or  numero_seleccionado_x_usuario >10:
    print("Te dije que ingreses un numero del 1 al 10, volvé a empezar 🤦‍♂   ️")
    exit()

if numero_secreto == numero_seleccionado_x_usuario:
    print("Felicidades ✌️🪄, adivinaste el número secreto la tercera vez")
    exit()
else:
    print(f"Lo siento 😗, no adivinaste el número secreto. Alpiste  Perdiste!!!!🧙‍♂️, el numero magico que pensé es {numero_secreto} ")
