##Realizar un juego donde la computadora seleccione un numero aleatorio del 1 al 10
import random
contador = 0
var = random.randint(1,10)                    
num = int(input(" Elige tu numero: "))
print (f"El numero elegido es:  {num}")

if num == var and contador == 0:
    print(f" Felicitaciones, brillante tu capacidad de intuicion, en la primera😎🏆🏅")
    exit()
else:
    print (f" Elige de nuevo, piensa bien y lo acertaras 🙄🙄 ")
    contador=+1

num = int(input(" Elige tu numero: "))
print (f"El numero elegido es:  {num}")

if num==var and contador == 1:
    print(f" Felicitaciones, brillante tu capacidad de intuicion, 😎🏆🏅")
    exit()

else:
    print (f" Esta fue tu segunda opcion, piensa ☹☹😖  ")
    contador=+1

num = int(input(" Elige tu numero: "))
print (f"El numero elegido es:  {num}")

if num==var and contador == 2:
    print(f" Felicitaciones, brillante tu capacidad de intuicion 😎🏆🏅")
    exit()
else:
    print (f" Esta fue tu ultima chance, otra vez sera 😥😤😭  ")
    contador=+1


print (f" Fallaste en {contador + 2} posibilidades 😂🤣🤣😂😂")
print (f" el Numero seleccionado era : {var}, estuviste muy cerca")
exit

