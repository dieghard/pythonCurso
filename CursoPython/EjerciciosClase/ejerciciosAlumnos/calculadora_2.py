#3 VALORES
# 2 NUMEROS A UTILIZAR
# TERCER VARIABLE ES LA OPERACION A REALIZAR(S/R/M/D)
# SALIDA ESPERADA: OPERACION REALIZADA CON EXITO EL RESULTADO DE (OPERACION) ES (RESULTADO)
# NO SE PUEDE DIVIDIR POR CERO

valor_1 = input("ingrese el primer valor: ")
valor_2 = input("ingrese el segundo valor: ")
operacion = input("ingrese la operacion a realizar (S/R/M/D): ")
nombre_operacion = "Pusiste mal el nombre de la operacion"
resultado = 0

if valor_1.isdigit() and valor_2.isdigit():
    valor_1 = int(valor_1)
    valor_2 = int(valor_2)
else:
    print("pusiste cualquier cosa")
    exit()

operacion = operacion.upper()
if operacion == "S":
        resultado = valor_1 + valor_2
        nombre_operacion = "Suma"
elif operacion == "R":
        resultado = valor_1 - valor_2
        nombre_operacion = "Resta"
elif operacion == "M":
        resultado = valor_1 * valor_2
        nombre_operacion = "Multiplicacion"
elif operacion == "D":
        if valor_2 == 0:
            print("Recuerde que nada es divisible por cero")
            exit()
        resultado = valor_1 / valor_2
        nombre_operacion = "Division"
else:
    print("Operacion invalida")
print(f" OPERACION REALIZADA CON EXITO EL RESULTADO DE {nombre_operacion} ES {resultado}")