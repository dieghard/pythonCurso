#Imprimir mensaje en el borde
#La computadora tiene que tirar un  numero aleatorio
#La persona tiene que adivinarlo
import random

print("")
print("#"*80)
print("#############                                                                            ############")
print("#############                   Bienvenido a ADIVINE EL NÚMERO                           ############")
print("#############   Tendrás 3 oportunidades para adivinar el número que pensé 😏🤭          ############")
print("#############                                                                            ############")
print("#############                                                                            ############")
print("#"*80)
print("")
print("Presione una enter para continuar....")
input() #se utiliza tambien para poder pausar la ejecucion de un programa hasta que el usuario ingrese algo, en este caso usara enter y nada más
print("\n"*50)# Limpiar la pantalla

# Genera el número aleatorio al inicio y lo guarda en una variable
resultado_compu = random.randint(0, 10)

# Primer intento
primer_numero = input("Ingrese el número que cree que es el correcto del 0-10: ")

if primer_numero.isdigit():
    primer_numero = int(primer_numero)
    if primer_numero == resultado_compu:
        print(f"GANASTEEE! Felicidades! El resultado era {resultado_compu}")
        exit()
    else:
        print(f"Vuelve a intentarlo, te quedan 2 intentos")
else:
    print("Pusiste cualquier cosa")

# Segundo intento
segundo_numero = input("Ingrese el número que cree que es el correcto del 0-10: ")

if segundo_numero.isdigit():
    segundo_numero = int(segundo_numero)
    if segundo_numero == resultado_compu:
        print(f"GANASTEEE! Felicidades! El resultado era {resultado_compu}")
        exit()
    else:
        print(f"Vuelve a intentarlo, te queda 1 intento")
else:
    print("Pusiste cualquier cosa")

# Tercer intento
tercer_numero = input("Ingrese el número que cree que es el correcto del 0-10: ")

if tercer_numero.isdigit():
    tercer_numero = int(tercer_numero)
    if tercer_numero == resultado_compu:
        print(f"GANASTEEE! Felicidades! El resultado era {resultado_compu}")
    else:
        print(f"Perdisteeeee, el resultado correcto era {resultado_compu}")
else:
    print("Pusiste cualquier cosa")
