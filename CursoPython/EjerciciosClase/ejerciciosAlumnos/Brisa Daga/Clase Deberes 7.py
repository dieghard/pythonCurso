#Imprimir mensaje en el borde
#La computadora tiene que tirar un  numero aleatorio
#La persona tiene que adivinarlo

print("")
print("#"*80)
print("#############                                                                            ############")
print("#############                   Bienvenido a ADIVINE EL NÚMERO                           ############")
print("#############   Tendrás 3 oportunidades para adivinar el número que pensé 😏🤭          ############")
print("#############                                                                            ############")
print("#############                                                                            ############")
print("#"*80)
print("")
print("Presione una tecla para continual....")

import random
#random(0,10)
random.randint(0,10) 
resultado_compu = {random.randint(0,10)}
primer_numero = input("Ingrese el número que cree que es el correcto del 1-10:  ") 
primer_numero = int
if primer_numero.isdigit():
    continuar = True
else:
    print("Pusiste culquien cosa")

if not resultado_compu == primer_numero 
    print(f"Vuelve a intentarlo, te quedan 2 intentos")
else:
     print(f"GANASTEEE! Felicidades! El resultado era {resultado_compu} ") 

       
#2 Intento
random.randint(0,10) 
resultado_compu = {random.randint(0,10)}
primer_numero = input("Ingrese el número que cree que es el correcto del 1-10:  ") 
primer_numero = int
if primer_numero.isdigit():
    continuar = True
else:
    print("Pusiste culquien cosa")

if not resultado_compu == primer_numero 
   print(f"Vuelve a intentarlo, te quedan 1 intentos")
else:
     print(f"GANASTEEE! Felicidades! El resultado era {resultado_compu} ") 
     
    
#3 Intento
random.randint(0,10) 
resultado_compu = {random.randint(0,10)}
primer_numero = input("Ingrese el número que cree que es el correcto del 1-10:  ") 
primer_numero = int
if primer_numero.isdigit():
    continuar = True
else:
    print("Pusiste culquien cosa")

if not resultado_compu == primer_numero 
   print(f"Perdisteeeee, el resultado correcto era {resultado_compu}")
else:
     print(f"GANASTEEE! Felicidades! El resultado era {resultado_compu} ")     