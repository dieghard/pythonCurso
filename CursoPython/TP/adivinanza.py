#Tengo que desarrolllar un juego para el cumpleaños de mi sobrino
#El juego consiste en adivinar un número del 1 al 10
#Si adivina el número, le tengo que decir cuántos intentos le tomó adivinarlo
#tambien tengo que poner si esta frio o caliente
#Si no adivina el número, le tengo que decir que no adivinó el número y que lo siga intentando
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


import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

valor_seleccionado_por_la_maquina = random.randint(1,10)
nombre_jugador =input("Ingrese el nombre del jugador: ")
saludo_1 = f"Hola {nombre_jugador} bienvenido al juego de adivinanza, tenes 3 oportunidades para adivinar el número que seleccione, el número es del 1 al 10"

saludo_2 =f"Vamos GENI@ DE LA VIDA se que te llamas {nombre_jugador} pq lo pusiste recien , tenes 3 oportunidades para adivinar el número que seleccione, el número es del 1 al 10"

saludo_3 = f"ooooooh gran {nombre_jugador}, tenes 3 oportunidades para adivinar el número que seleccione, el número es del 1 al 10"

saludo_4 = f"dale loco!!!! {nombre_jugador} adiviname y te llevas un beso."

elegi_un_saludo = random.randint(1,4)
if (elegi_un_saludo == 1):
    saludo = saludo_1
if (elegi_un_saludo == 2):
    saludo = saludo_2
if (elegi_un_saludo == 3):
    saludo = saludo_3
if (elegi_un_saludo == 4):
    saludo = saludo_4

print (saludo)
print("")
varlor_seleccionado_usuario = input("ingresa el numero que crees que seleccione (el juego es del 1 al 10): ")
#Valido que haya ingresado un numero y no una letra
error_numero_uno_diez ="Te dije que pongas un numero del 1 al 10, Volve a empezar"
adivino_1 = f"{nombre_jugador} Adivinaste el número ALA PRIMERA VEZ ... sos un genuio de la vida!!!!🚀🚀🚀🚀🚀🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️"
adivino_2 = f"{nombre_jugador} Adivinaste el número en la segunda oportunidad ... CAPO TOTAL ! 🚀🚀🚀🚀🚀🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️"
adivino_3 = f"{nombre_jugador} Adivinaste el número en la ultima  oportunidad ... TE FELICITO!! 🚀🚀🚀🚀🚀🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️🧙‍♂️"

no_adivino_1 = f"{nombre_jugador} No adivinaste el número lo lamento mucho, volve a probar , te quedan 2 oportunidades🧙‍♂️"
no_adivino_2 = f"{nombre_jugador} No adivinaste, pensa un poco mas,  volve a probar ya que te queda la ultima oportunidad🧙‍♂️"
no_adivino_3 = f"{nombre_jugador} aaaay {nombre_jugador}, {nombre_jugador}   lo lamento mucho,dejale la oportunidad a otro jugador y paga laprata 🧙‍♂️"

# aca voy declarar las variables para el texte de las diferencias
diferencia_dos = "Estas muy hot 🌋"
diferencia_tres = "Esta tibio 😗"
diferencia_cuatro = "Estas re frio negro 🥶"

if not  varlor_seleccionado_usuario.isdigit() :
    print(error_numero_uno_diez)
    exit()
#lo convierto a int
varlor_seleccionado_usuario = int(varlor_seleccionado_usuario)

#valido que este dentro del rango de numeros
if  varlor_seleccionado_usuario <1 or varlor_seleccionado_usuario >10:
    print(error_numero_uno_diez)
    exit()



#aca muestro el resultado si adivino o no
if valor_seleccionado_por_la_maquina == varlor_seleccionado_usuario:
    print(adivino_1)
    exit()
else:
    print(no_adivino_1)
    calculo = valor_seleccionado_por_la_maquina - varlor_seleccionado_usuario
    if calculo >= 2 or calculo >= -2:
        print(diferencia_dos)
    if calculo == 3 or calculo == -3:
        print(diferencia_tres)
    if calculo > 4 or calculo <= -4:
        print(diferencia_cuatro)
#ahora voy a hacer el segundo intento de adivinar el numero
varlor_seleccionado_usuario = input("ingresa el numero que crees que seleccione por segunda vez 🧙‍♂️🪄 (el juego es del 1 al 10): ")
#Valido que haya ingresado un numero y no una letra
if not  varlor_seleccionado_usuario.isdigit() :
    print(error_numero_uno_diez)
    exit()
#lo convierto a int
varlor_seleccionado_usuario = int(varlor_seleccionado_usuario)

#valido que este dentro del rango de numeros
if  varlor_seleccionado_usuario <1 or varlor_seleccionado_usuario >10:
    print(error_numero_uno_diez)
    exit()

#aca muestro el resultado si adivino o no
if valor_seleccionado_por_la_maquina == varlor_seleccionado_usuario:
    print(adivino_2)
    exit()
else:
    print(no_adivino_2)
    calculo = valor_seleccionado_por_la_maquina - varlor_seleccionado_usuario
    if calculo >= 2 or calculo >= -2:
        print(diferencia_dos)
    if calculo == 3 or calculo == -3:
        print(diferencia_tres)
    if calculo > 4 or calculo <= -4:
        print(diferencia_cuatro)

#tercer intento

varlor_seleccionado_usuario = input("ingresa el numero que crees que seleccione por ultima vez 🧙‍♂️🪄 (el juego es del 1 al 10): ")
#Valido que haya ingresado un numero y no una letra
if not  varlor_seleccionado_usuario.isdigit() :
    print(error_numero_uno_diez)
    exit()
#lo convierto a int
varlor_seleccionado_usuario = int(varlor_seleccionado_usuario)

#valido que este dentro del rango de numeros
if  varlor_seleccionado_usuario <1 or varlor_seleccionado_usuario >10:
    print(error_numero_uno_diez)
    exit()

#aca muestro el resultado si adivino o no
if valor_seleccionado_por_la_maquina == varlor_seleccionado_usuario:
    print(adivino_3)
    exit()
else:
    print(no_adivino_3)
    print (f"El número que tenías que adivinar era {valor_seleccionado_por_la_maquina} 🧙‍♂️🪄🚀")