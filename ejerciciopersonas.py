#Datos persona 1
nombre_apellido = input("Ingresa el nombre de la primer persona: ")
direccion = input("Ingresa la direccion de la primer persona: ")
edad = int(input("Ingresa la edad de la primer persona:"))


nombre_mayor =  nombre_apellido
direccion_mayor = direccion
edad_mayor = edad
posicion_mayor_cargada = 1

nombre_menor =  nombre_apellido
direccion_menor = direccion
edad_menor = edad
posicion_menor_cargada = 1

#Datos persona 2
nombre_apellido= input("Ingresa el nombre de la segunda persona: ")
direccion = input("Ingresa la direccion de la segunda persona: ")
edad = int(input("Ingresa la edad de la segunda persona:"))
posicion_cargada = 2

if edad > edad_mayor:
    nombre_mayor =  nombre_apellido
    direccion_mayor = direccion
    edad_mayor = edad
    posicion_mayor_cargada = 2
if edad < edad_menor:
    nombre_menor =  nombre_apellido
    direccion_menor = direccion
    edad_menor = edad
    posicion_menor_cargada = 2


#Datos persona 3
nombre_apellido= input("Ingresa el nombre de la tercera persona: ")
direccion = input("Ingresa la direccion de la tercera persona: ")
edad = int(input("Ingresa la edad de la tercera persona:"))

if edad > edad_mayor:
    nombre_mayor =  nombre_apellido
    direccion_mayor = direccion
    edad_mayor = edad
    posicion_mayor_cargada = 3

if edad < edad_menor:
    nombre_menor =  nombre_apellido
    direccion_menor = direccion
    edad_menor = edad
    posicion_menor_cargada = 3


#Datos persona 4
nombre_apellido= input("Ingresa el nombre de la cuarta persona: ")
direccion = input("Ingresa la direccion de la cuarta persona: ")
edad = int(input("Ingresa la edad de la cuarta persona:"))
if edad > edad_mayor:
    nombre_mayor =  nombre_apellido
    direccion_mayor = direccion
    edad_mayor = edad
    posicion_mayor_cargada = 4
if edad < edad_menor:
    nombre_menor =  nombre_apellido
    direccion_menor = direccion
    edad_menor = edad
    posicion_menor_cargada = 4


print(f"La persona con mayor edad es {nombre_mayor}, su direccion es{direccion_mayor} con {edad_mayor} años y fue cargada en la {posicion_mayor_cargada} y la persona de menor edad es {nombre_menor} cuya edad es {edad_menor} y vive en {direccion_menor} y fue cargado en la posición {posicion_menor_cargada}")
