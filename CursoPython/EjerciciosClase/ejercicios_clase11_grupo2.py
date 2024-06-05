# RECORDA BORRAR LAS """ ANTES Y DESPUES DEL CODIGO PARA EJECUTAR EL EJERCICIO QUE QUIERAS VER!!!!!!!!

"""# Ejercicio 1 WHILE

contador = 10
while contador >=0:
    print (contador)
    contador -=1
print("Despegue!")
"""

"""#Ejercicio 2 WHILE

acumulador =  0
numero = 1
while numero != 0:
    numero = input("ingrese un numero:")
    if numero.isdigit():
        numero = int(numero)
        acumulador += numero
        print(f"el numero ingresado es {numero} y el acumulado es {acumulador}")
    else:
        print("ingrese un numero valido")
"""

"""#Ejercicio 3 WHILE
continuar = True
while continuar:
    numero_usuario = input("Ingrese un numero de la tabla de multiplicar:")
    if not numero_usuario.isdigit(): #Si no es numero, termina el programa
        exit("Chau por burrooo")
    numero_usuario = int(numero_usuario)
    contador = 0
    while contador < 10:
        contador += 1
        print(f"{contador} x { numero_usuario} = {numero_usuario*contador}")
    continuar = input("Si desea multiplicar otro numero coloque 1 si no, 0:")
    if continuar == "1":
        continuar = True
    else:
        continuar = input("¿Estas seguro que queres salir? Pone 1 para volver a usar la Multiplicadora:")
    if continuar == "1":
        continuar = True
    else:
        continuar = False
"""