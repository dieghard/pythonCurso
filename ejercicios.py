"""#Realiza un programa que permita ingresar solo texto
ingresar = input("Ingresa el texto a mostrar: ")
if ingresar.isalpha():
    print(f"El texto ingresado es: {ingresar}")
else:
    print(f"El texto ingresado no es solo texto, ingresaste: {ingresar}")
#Realizar un programa que permita ingresar solo texto y muestre todo en mayuscula
ingresar_mayuscula = input("Ingresa el texto a mostrar y cambiar a mayusculas: ")
if ingresar.isalpha():
    print(f"El texto ingresado es: {ingresar_mayuscula.upper()}")
else:
    print(f"El texto ingresado no es solo texto, ingresaste: {ingresar_mayuscula}")
#Que permita ingresar solo numeros, si no se cumplke este requisito que me 
#de hasta 2 oportunidades mas y me muestre la cantidad de veces que lo hice mal
contador = 3
ingresar3 = input("Ingresa el texto a mostrar: ")
if not ingresar3.isalpha():
    contador -= 1
    print(f"Entrada incorrecta te quedan {contador} oportunidades")
    ingresar3 = input("Ingresa el texto a mostrar: ")
    if not ingresar3.isalpha():
        contador -= 1
        print(f"Entrada incorrecta te quedan {contador} oportunidades")
        ingresar3 = input("Ingresa el texto a mostrar: ")
        if not ingresar3.isalpha():
            contador -= 1
            print(f"Entrada incorrecta te quedan {contador} oportunidades")            
        else:
            print(f"Bien pibe, ingresaste un texto y te sobraron {contador} oportunidades")
    else: 
        print(f"Bien pibe, ingresaste un texto y te sobraron {contador} oportunidades")
else:
    print(f"Bien pibe, ingresaste un texto y te sobraron {contador} oportunidades")

#Calculadora
valor1 = int(input("Ingrese el primer valor:"))
valor2 = int(input(f"Ingrese el segundo valor:"))
operacion = input("Ingrese la operacion(S/R/M/D) que desea realizar:")

if operacion == "S":
    resultado = valor1 + valor2
    print(f"Operacion Realizada con exito, el resultado de la Suma es {resultado}")
elif operacion == "R":
    resultado = valor1 - valor2
    print(f"Operacion Realizada con exito, el resultado de la Resta es {resultado}")
elif operacion == "M":
    resultado = valor1 * valor2
    print(f"Operacion Realizada con exito, el resultado de la Multiplicacion es {resultado}")
elif operacion == "D" and valor2 != 0:
    resultado = valor1 / valor2
    print(f"Operacion Realizada con exito, el resultado de la Division es {resultado}")
else:
    print("Operacion no valida")"""
#Realizar un programa que permita el ingreso de 4 personas con su nombre y apellido, direccion y edad y muestre en
#pantalla cual es la persona con mayor edad y la de menor edad, con la posicion en que se cargo
#Datos persona 1
nombre_apellido1= input("Ingresa el nombre de la primer persona: ")
direccion1 = input("Ingresa la direccion de la primer persona: ")
edad1 = int(input("Ingresa la edad de la primer persona:"))
#Datos persona 2
nombre_apellido2= input("Ingresa el nombre de la segunda persona: ")
direccion2 = input("Ingresa la direccion de la segunda persona: ")
edad2 = int(input("Ingresa la edad de la segunda persona:"))
#Datos persona 3
nombre_apellido3= input("Ingresa el nombre de la tercera persona: ")
direccion3 = input("Ingresa la direccion de la tercera persona: ")
edad3 = int(input("Ingresa la edad de la tercera persona:"))
#Datos persona 4
nombre_apellido4= input("Ingresa el nombre de la cuarta persona: ")
direccion4 = input("Ingresa la direccion de la cuarta persona: ")
edad4 = int(input("Ingresa la edad de la cuarta persona:"))

edad_mayor = edad1
nombre_apellido_mayor = nombre_apellido1
direccion_mayor = direccion1
edad_menor = edad1
nombre_apellido_menor = nombre_apellido1
direccion_menor = direccion1
#Detectar el de mayor edad:

if edad2 > edad_mayor:
    edad_mayor = edad2
    nombre_apellido_mayor = nombre_apellido2
    direccion_mayor = direccion2
    print(f"La persona con mayor edad es {nombre_apellido_mayor}, su direccion es{direccion_mayor} con {edad_mayor} años y fue cargada en la posicion 2")
elif edad3 > edad_mayor:
    edad_mayor = edad3
    nombre_apellido_mayor = nombre_apellido3
    direccion_mayor = direccion3
    print(f"La persona con mayor edad es {nombre_apellido_mayor}, su direccion es{direccion_mayor} con {edad_mayor} años y fue cargada en la posicion 3")
elif edad4 > edad_mayor:
    edad_mayor = edad4
    nombre_apellido_mayor = nombre_apellido4
    direccion_mayor = direccion4
    print(f"La persona con mayor edad es {nombre_apellido_mayor}, su direccion es{direccion_mayor} con {edad_mayor} años y fue cargada en la posicion 4")
else:
    print(f"La persona con mayor edad es {nombre_apellido_mayor}, su direccion es{direccion_mayor} con {edad_mayor} años y fue cargada en la posicion 1")

# Detectar la menor edad:
if edad2 < edad_menor:
    edad_menor = edad2
    nombre_apellido_menor = nombre_apellido2
    direccion_menor = direccion2
    print(f"La persona con menor edad es {nombre_apellido_menor}, su dirección es {direccion_menor} con {edad_menor} años y fue cargada en la posición 2")
elif edad3 < edad_menor:
    edad_menor = edad3
    nombre_apellido_menor = nombre_apellido3
    direccion_menor = direccion3
    print(f"La persona con menor edad es {nombre_apellido_menor}, su dirección es {direccion_menor} con {edad_menor} años y fue cargada en la posición 3")
elif edad4 < edad_menor:
    edad_menor = edad4
    nombre_apellido_menor = nombre_apellido4
    direccion_menor = direccion4
    print(f"La persona con menor edad es {nombre_apellido_menor}, su dirección es {direccion_menor} con {edad_menor} años y fue cargada en la posición 4")
else:
    print(f"La persona con menor edad es {nombre_apellido_menor}, su dirección es {direccion_menor} con {edad_menor} años y fue cargada en la posición 1")
