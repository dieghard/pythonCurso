#🔮Adivina el numero🔮 Realizar un programa que adivine un numero con 3intentos para adivinar el  numero secreto entre 1 y 10

print(""" █████╗ ██████╗ ██╗██╗   ██╗██╗███╗   ██╗ █████╗     ███████╗██╗         ███╗   ██╗██╗   ██╗███╗   ███╗███████╗██████╗  ██████╗
██╔══██╗██╔══██╗██║██║   ██║██║████╗  ██║██╔══██╗    ██╔════╝██║         ████╗  ██║██║   ██║████╗ ████║██╔════╝██╔══██╗██╔═══██╗
███████║██║  ██║██║██║   ██║██║██╔██╗ ██║███████║    █████╗  ██║         ██╔██╗ ██║██║   ██║██╔████╔██║█████╗  ██████╔╝██║   ██║
██╔══██║██║  ██║██║╚██╗ ██╔╝██║██║╚██╗██║██╔══██║    ██╔══╝  ██║         ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗██║   ██║
██║  ██║██████╔╝██║ ╚████╔╝ ██║██║ ╚████║██║  ██║    ███████╗███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║╚██████╔╝
╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝

""")
import random
num_secreto = random.randint(1,10)
num_secreto = str(num_secreto)
print()
jugador=0
contador=0
texto_inicial="Hola, del 1 al 10, que numero eleji ???  🔮Adivina el numero🔮 :"
no_adivina="No es ese, segui intentando! "

while jugador != num_secreto:
  contador+=1
  jugador= input(texto_inicial)
  if jugador != num_secreto:
    print (no_adivina)
    print()
#Cuando adivina el numero sale del while
ganador= f"Muy Bien lo adivinaste en el {contador}° intento"
print(ganador)
