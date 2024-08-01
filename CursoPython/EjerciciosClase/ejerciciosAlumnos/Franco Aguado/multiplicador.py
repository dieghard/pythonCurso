#❎Tabla de Multiplicar❎ Realizar un programa que muestre la tabla de multiplicar de un número ingresado por el usuario.

print("""███    ███ ██    ██ ██      ████████ ██ ██████  ██      ██  ██████  █████  ██████   ██████  ██████   █████
████  ████ ██    ██ ██         ██    ██ ██   ██ ██      ██ ██      ██   ██ ██   ██ ██    ██ ██   ██ ██   ██
██ ████ ██ ██    ██ ██         ██    ██ ██████  ██      ██ ██      ███████ ██   ██ ██    ██ ██████  ███████
██  ██  ██ ██    ██ ██         ██    ██ ██      ██      ██ ██      ██   ██ ██   ██ ██    ██ ██   ██ ██   ██
██      ██  ██████  ███████    ██    ██ ██      ███████ ██  ██████ ██   ██ ██████   ██████  ██   ██ ██   ██

    """)
print("ESTE PROGRAMA MUESTRA LA TABLA DE MULTILICAR DEL NUMERO QUE INGRESES")
print()
multiplicadora=input("Ingrese el numero que quiere ver la tabla : ")
print()
if multiplicadora.isdigit() :
    multiplicadora=int(multiplicadora)
else:
    print("No ingresaste un numero, no puedo mostrar nada")
    exit()
contador=0
while contador != 10:
    contador+=1
    multiplica = multiplicadora*contador
    print (f"{contador} x {multiplicadora} = {multiplica}")


print("puto")