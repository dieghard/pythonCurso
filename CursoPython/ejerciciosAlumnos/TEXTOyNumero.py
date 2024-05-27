#1- Realizar un programa que permita ingresar solo texto y los muestre todo en mayuscula

#var=input("ingrese un texto: ")
#var=var.upper()
#print(f"El texto ingresado es : {var}")

#2- Realizar un programa que permita ingresar solo numeros, si no se cumple este requisito, que me de la hasta
#2 oportunidades más y me muestre la cantidad de veces que lo hice mal.

var=input("Ingrese un valor numerico: ")
oportunidades = 1
cont=False

if not var.isdigit():
    cont=True
if cont:
    var= input(f"La variable ingresada no es un numero, es tu segundo intento de tres, ingresa un NUMERO:")
    oportunidades +=1
cont=False
if not var.isdigit() :
    cont=True
if cont==True :
    var=input("La variable ingresada no es un numero, ULTIMO INMTENTO!!  ")
    oportunidades+=1
cont=False
if not var.isdigit():
    cont=True
if cont:
    print(f"No ingresaste un numero, no vemoooo!")
    exit()

if not cont:
    print(f"El numero ingresado es {var} y fuen en el intento numero {oportunidades}")
    exit()
