#Cuenten cuantas veces se ingreso texto.
contador = 0
seguir = True

while seguir == True: #Cuando es Booleano no hace falta poner ==
    valor_usuario = input("Ingrese un valor o ingrese A para finalizar:")
    contador +=1
    valor_usuario = valor_usuario.upper()
    if valor_usuario == "A":
        seguir = False
print(f"Se ejecuto correctamente {contador} veces!")