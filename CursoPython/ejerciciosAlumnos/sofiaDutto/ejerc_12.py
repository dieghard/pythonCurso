
#3- Realizar un juego donde la computadora seleccione un numero aleatorio del 1 al 10 y 
# nosotros como jugadores tengamos hasta tres oportunidades de adivinar el numero, 
# si ganamos que nos muestre un mensaje felicitándonos y mostrando el numero aleatorio seleccionado. 
# Tener en cuenta que el numero seleccionado por la computadora al inicio es el mismo que deben evaluar 
# en los tres intentos! tambien quiero ver en que numero de intento lo acerte

import random

numero_aleatorio = random.randint(1, 10)
numero_ingresado = input("ingrese su número:")
contador = 0
continuar = True


if continuar == True:
    if numero_ingresado == numero_aleatorio:
        print(f"Felicitaciones, ¡acertaste en el primer intento!, ingresaste {numero_ingresado}")
        continuar = False
    else: 
        contador += 1
        print("Segunda oportunidad. Ingrese su número del 1 al 10:")
        continuar = True

if continuar == True:
    numero_ingresado = input("ingrese su número:")
    if numero_ingresado == numero_aleatorio:
        print(f"Felicitaciones, ¡acertaste en el segundo intento!, ingresaste {numero_ingresado}")
        continuar = False
    else: 
        contador += 1
        print("Tercerca y última oportunidad. Ingrese su número del 1 al 10:")
        continuar = True
        
if continuar == True:
    numero_ingresado = input("ingrese su número:")
    if numero_ingresado == numero_aleatorio:
        print(f"Felicitaciones, ¡acertaste en el tercer intento!, ingresaste {numero_ingresado}")
        continuar = False
    else: 
        print("No hay más oportunidades. Seguí participando;)")
        exit() 
              
print(f"Acertaste en el intento {contador}.")        
     





