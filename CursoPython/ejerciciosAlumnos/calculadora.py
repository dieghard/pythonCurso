# 3 VALORES
# DOS NUMEROS A UTILIZAR
# UNA OPERACION (S/R/M/D)
# SALIDA: OPERACION REALIZADA CON EXITO, EL RESULTADO DE (LA OPERACION) ES: (RESULTADO)
# NO SE PUEDE DIVIDIR POR 0

numero_1 = input("Ingrese el primer numero:")
numero_2 = input("Ingrese el segundo numero:")
operacion = input("Ingrese la operacion a realizar (S/R/M/D):")

if numero_1.isdigit() and numero_2.isdigit():
    numero_1 = int(numero_1)
    numero_2 = int(numero_2)
else:
    print("No ingresaste un numero")
    exit()

operacion = operacion.upper()

if operacion == "S" or operacion == "R" or operacion == "M" or operacion == "D": #Valida que la operacion este bien!
    if operacion == "S":
        resultado = numero_1 + numero_2
        print(f"OPERACION REALIZADA CON EXITO, EL RESULTADO DE LA SUMA ES: {resultado}")
    elif operacion == "R":
        resultado = numero_1 - numero_2
        print(f"OPERACION REALIZADA CON EXITO, EL RESULTADO DE LA RESTA ES: {resultado}")
    elif operacion == "M":
        resultado = numero_1 * numero_2
        print(f"OPERACION REALIZADA CON EXITO, EL RESULTADO DE LA MULTIPLICACION ES: {resultado}")
    elif operacion == "D":
        if numero_2 == 0:
            print("NO SE PUEDE DIVIDIR POR 0")
            exit()
        resultado = numero_1 / numero_2
        print(f"OPERACION REALIZADA CON EXITO, EL RESULTADO DE LA DIVISION ES: {resultado}")

else:
    print("No ingresaste una operacion valida")
    exit()