## Juego

import random


print("")
print("#"*80)

print("######                                                                    ######")
print("######                 Bienvenido a ADIVINE UN NÚMERO                     ###### ")
print("######                                                                    ######")
print("###### Tendrá 3 oportuniades para adivinar el numero que pense 🧐🚀       ######")
print("######                                                                    ######")
print("######                                                                    ######")
print("#"*80)
print("")
print("Presione una tecla para continuar...")
input() # Esperar a que el usuario presione una tecla
# Limpiar la pantalla
print("\n"*50)


var = random.randint(1,4)                    
num = int(input("Ingrese el numero con el que Jugaras: "))
print (f"El numero elegido es:  {num}")
if num <= (var - 4):
    print (f"Frio, frio, piensa mejor")
    print (f"El numero elegido es:  {num}")
elif num <= (var - 1):
    print (f" Caliente, casi lo adivinas")
    print (f"El numero elegido es:  {num}")
elif num >= (var + 4):
    print (f"Frio, frio, te pasaste")
    print (f"El numero elegido es:  {num}")
else:
    print (f" Correcto, Congratulations")
exit()
    
    
    