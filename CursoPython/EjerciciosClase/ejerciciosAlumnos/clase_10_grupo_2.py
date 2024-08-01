#Escribe un programa que me permita ingresar valores y que corte cuando el usuario envie A. Quiero saber cuantas veces se ingreso un valor.
#DEBUGGER
#BUG'S
seguir = True
contador = 0
while seguir == True:
    ingresa_valor = input("Ingresa un valor: ")
    ingresa_valor = ingresa_valor.upper()
    contador += 1
    if ingresa_valor  == "A":
        seguir = False

print(f"Se ejecuto correctamente. la cantidad de veces ingresadas fue: { contador}")