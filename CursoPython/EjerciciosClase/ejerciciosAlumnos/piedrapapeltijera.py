import random 

opciones = ("tijera", "papel", "piedra")
usuario = input("elige:")
computudora = random.choice(opciones)
if usuario not in opciones:
    print("error")
    quit()
if usuario == computudora:
    print("empate") 
elif usuario == "tijera" and computudora == "piedra" or usuario == "piedra" and computudora == "papel" or usuario == "papel" and computudora == "tijera":
    print("perdiste crack")
else:
    print("ganaste animal")
