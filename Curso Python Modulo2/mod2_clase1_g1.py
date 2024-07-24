#Modulo 2- Funciones
def calculadora_de_operaciones(numero_1:int ,numero_2:int, operacion:str ):

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
    #print(resultado)
    return resultado
print(calculadora_de_operaciones(25,5,"%"))
print(calculadora_de_operaciones(25,5,"+"))

input_1 = int(input("Ingrese un numero para sumar:"))
input_2 = int(input("Ingrese un numero para sumar:"))
input_operacion = input("Ingrese la operacion a realizar(+,-,*,/,\%\ o suma ,resta ,multiplicacion , division, modulo):")

resultado = calculadora_de_operaciones(input_1,input_2, input_operacion)
#resultado_2 = calculadora_de_operaciones(15,20,"-")




#ACTIVIDAD: HACER UNA FUNCION QUE RECIBA UN STRING Y LO IMPRIMA POR CONSOLA

def imprimir_algo(parametro:str):
    print(parametro)
    return #Si no tiene return es un procedimiento
#imprimir_algo("hola mundo")
#imprimir_algo("Chau mundo")

#for contador in range(10):
 #   imprimir_algo(f"Hola {contador}")
