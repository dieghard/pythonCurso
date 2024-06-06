#Hacer un juego cara/cruz donde el usuario tenga dos oportunidades para elegir si jugar contra la comput o
#jugar con un amigo. Si elige la opcion 2 deberíamos preguntar el nombre a ambos jugadores


import random
resultado =  random.randint(0,1)

if resultado == 0:
    resultado_cara = "CARA"
    resultado = resultado_cara
else:
    resultado_cruz = "CRUZ"
    resultado = resultado_cruz


continuar = True
print ("Bienvenid@ al juego cara/cruz")
contra_quien = input("¿contra quien deseas jugar? Elige entre las opciones: COMPUTADORA/AMIGO: ")

if  contra_quien == "amigo":
    contra_quien = contra_quien.upper()
    nombre_amigo = input("ingresá el nombre de tu amigo:")
    nombre_usuario = input ("ingresá tu nombre:")
    valor_usuario = valor_usuario = input(f"{nombre_usuario}, elegí CARA o CRUZ, ingresá tu opción ahora:").upper()
    valor_amigo = valor_amigo = input (f"{nombre_amigo}, elegí CARA o CRUZ, ingresá tu opción ahora:").upper()

else:
    contra_quien == "computadora"
    contra_quien = contra_quien.upper()
    print("Agarrate Catalina. Jugás en mi contra")
    valor_usuario = input("elegí CARA o CRUZ, ingresá tu opción ahora:").upper()

while valor_usuario != "CARA" and valor_usuario != "CRUZ":
        print("ingresaste una opción incorrecta, por favor ingresá CARA o CRUZ")
        valor_usuario = input("elegí CARA o CRUZ, ingresá tu opción ahora:")

if resultado == valor_usuario:
        print("¡Acertaste! Felicitaciones, me has ganado, crack!")
        continuar = False #puedo usar break acá? cómo?
else:
        print("volvé a intentarlo, no te desanimes")

print(f"el resultado era {resultado}")


#dónde debo ingresar esta opción para que juegue usuario contra amigo?? lo probé en varias opciones, usando
# mi lógica, pero hasta ahora no funcionó
"""while valor_usuario != "CARA" and valor_usuario != "CRUZ":
        print("Ingresaste una opción incorrecta. Por favor ingresa CARA o CRUZ.")
        valor_usuario = input(f"{nombre_usuario}, elige CARA o CRUZ: ").upper()

valor_amigo = input(f"{nombre_amigo}, elige CARA o CRUZ: ").upper()
while valor_amigo != "CARA" and valor_amigo != "CRUZ":
    print("Ingresaste una opción incorrecta. Por favor ingresa CARA o CRUZ.")
    valor_amigo = input(f"{nombre_amigo}, elige CARA o CRUZ: ").upper()

resultado = random.choice(["CARA", "CRUZ"])

print("El resultado es:", resultado)


if continuar == True and valor_usuario == resultado:
    print(f"{nombre_usuario} ha ganado.")
elif valor_amigo == resultado:
    print(f"{nombre_amigo} ha ganado.")
else:
    print("¡Es un empate!")"""




























