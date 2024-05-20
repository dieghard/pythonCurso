#Datos persona 1
contador = 0
nombre_apellido1 = input("Ingresa el nombre de la primer persona: ")
direccion1 = input("Ingresa la direccion de la primer persona: ")
edad1 = int(input("Ingresa la edad de la primer persona:"))


nombre_mayor =  nombre_apellido1
direccion_mayor = direccion1
edad_mayor = edad1
posicion_mayor_cargada = 1

nombre_menor =  nombre_apellido1
direccion_menor = direccion1
edad_menor = edad1
posicion_menor_cargada = 1

#Datos persona 2
nombre_apellido2= input("Ingresa el nombre de la segunda persona: ")
direccion2 = input("Ingresa la direccion de la segunda persona: ")
edad2 = int(input("Ingresa la edad de la segunda persona:"))
posicion_cargada = 2

if edad2 > edad_mayor:
    nombre_mayor =  nombre_apellido2
    direccion_mayor = direccion2
    edad_mayor = edad2
    posicion_mayor_cargada = 2
if edad2 < edad_menor:
    nombre_menor =  nombre_apellido2
    direccion_menor = direccion2
    edad_menor = edad2
    posicion_menor_cargada = 2


#Datos persona 3
nombre_apellido3= input("Ingresa el nombre de la tercera persona: ")
direccion3 = input("Ingresa la direccion de la tercera persona: ")
edad3 = int(input("Ingresa la edad de la tercera persona:"))

if edad3 > edad_mayor:
    nombre_mayor =  nombre_apellido3
    direccion_mayor = direccion3
    edad_mayor = edad3
    posicion_mayor_cargada = 3

if edad3 < edad_menor:
    nombre_menor =  nombre_apellido3
    direccion_menor = direccion3
    edad_menor = edad3
    posicion_menor_cargada = 3


#Datos persona 4
nombre_apellido4= input("Ingresa el nombre de la cuarta persona: ")
direccion4 = input("Ingresa la direccion de la cuarta persona: ")
edad4 = int(input("Ingresa la edad de la cuarta persona:"))
if edad4 > edad_mayor:
    nombre_mayor =  nombre_apellido4
    direccion_mayor = direccion4
    edad_mayor = edad4
    posicion_mayor_cargada = 4
if edad4 < edad_menor:
    nombre_menor =  nombre_apellido4
    direccion_menor = direccion4
    edad_menor = edad4
    posicion_menor_cargada = 4


print(f"La persona con mayor edad es {nombre_mayor}, su direccion es{direccion_mayor} con {edad_mayor} años y fue cargada en la {posicion_mayor_cargada} y la persona de menor edad es {nombre_menor} cuya edad es {edad_menor} y vive en {direccion_menor} y fue cargado en la posición {posicion_menor_cargada}")
