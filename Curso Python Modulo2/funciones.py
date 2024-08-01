#Nuestas funciones

def numero (texto_input:str|None= "Ingrese un numero:")-> int:
    """
    Funcion para ingresar y validar un numero, 
    texto_input muestra el mensaje por consola
    """
    while True:
        numero_1 = input (texto_input)
        if numero_1.isdigit():
            numero_1 = int(numero_1)
            if numero_1 > 0:
                break
            else:
                print("El valor ingresado debe ser mayor a 0")
        else:
            print("El valor ingresado no es un Nro")
    return numero_1

#Ejemplo 1: Una funcion que salude, teniendo en cuenta que puede tener doble nombre y doble apellido:

def saludo(nombre:str, apellido:str | None = " ")->str:
    print(f"Hola {nombre}{apellido}")
    return 
saludo("Eugenia", " de Escobar")


#Ejemplo 2: Calcular el área de un cuadrado:

def area (lado:int | None = 0)->int:
    return  lado**2

calculo = numero()
resultado = area(calculo)
print(f" El area del cuadrado es: {resultado}")