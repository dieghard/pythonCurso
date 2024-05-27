#3- Realizar un juego donde la computadora seleccione un numero aleatorio del 1 al 10 y nosotros como jugadores tengamos hasta tres oportunidades de adivinar el numero, si ganamos que nos muestre un mensaje felicitándonos y mostrando el numero aleatorio seleccionado. Tener en cuenta que el numero seleccionado por la computadora al inicio es el mismo que deben evaluar en los tres intentos!
#Deigui -tambien quiero ver en que numero de intento lo acerte

import random
numero_aleatorio = random.randint(1, 10)
print(f"Numero aleatorio entre 1 y 10: {numero_aleatorio}")
oportunidades = 1
continuar =True
num_usr = int(input("Que numero eligio la compu? : "))

if num_usr == numero_aleatorio :
    print(f"Muy bien!! a la primera! acertaste era el {num_usr}")
    exit()

if continuar ==True :
    num_usr= int(input("NO, SEGUNDA OPORTUNIDAD : "))
    oportunidades += 1 #Acumula los intentos5
if num_usr == numero_aleatorio :
    continuar=False

if continuar == True:
    num_usr= int(input("NO, ULTIMA OPORTUNIDAD!!! : "))
    oportunidades +=1  #Acumula los intentos
if num_usr == numero_aleatorio :
    print(f"Muy bien felicitado, la pegaste! El numero era el {numero_aleatorio} acertaste en el {oportunidades}  " )
else:
    print("Lo siento PERDISTE")