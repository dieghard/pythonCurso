import funciones as f

def operacion():
    numero_1 = int(input("Ingrese el numero a utilizar:"))
    numero_2 = int(input("Ingrese el numero a utilizar:"))
    operacion = input("Ingrese la operacion a realizar(+,-,*,/,\%\ o suma , resta,multiplicacion , division, modulo)")

    if operacion == "+" or operacion == "suma":
        resultado = numero_1 + numero_2
    elif operacion == "-" or operacion == "resta":
        resultado = numero_1 - numero_2
    elif operacion == "*" or operacion == "multiplicacion":
        resultado = numero_1 * numero_2
    elif operacion == "/" or operacion == "division":
        resultado = numero_1 / numero_2
    elif operacion == "%" or operacion == "modulo":
        resultado = numero_1 % numero_2    
    else:
        print("Escribiste cualquier cosa, menos una operacion")
    return resultado

#Funcion para imprimir un texto:


def imprimir(parametro):
    print(parametro)
    return

imprimir(f.validar_texto("Ingresa un HOLA MUNDO:"))
imprimir(f.validar_texto())