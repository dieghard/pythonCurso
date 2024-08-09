# Funciones de ejemplo para el curso de Python

def sumar(numero_1:int,numero_2:int)->int:
    '''
    Esta funcion recibe dos numeros y los suma
    '''
    return numero_1 + numero_2 #El return me devuelve los dos valores sumados

def restar(numero_1:int,numero_2:int)->int:
    '''
    Esta funcion recibe dos numeros y los resta
    '''
    return numero_1 - numero_2 #El return me devuelve los dos valores sumados

def multiplicar(numero_1:int,numero_2:int)->int:
    '''
    Esta funcion recibe dos numeros y los multiplica
    '''
    return numero_1 * numero_2 #El return me devuelve los dos valores sumados

def division(numero_1:int,numero_2:int)->int:
    '''
    Esta funcion recibe dos numeros y los divide
    '''
    return numero_1 * numero_2 #El return me devuelve los dos valores sumados

def numero ()->int:
    '''
    Esta funcion recibe un numero y verifica que sea un numero, y solo corta cuando el ingreso sea un numero
    '''
    while True:
        numeros = input("Ingrese un numero:")
        if numeros.isdigit():
            numeros = int(numeros)
            break
        else:
            print("Ingrese un numero valido")

    return numeros


