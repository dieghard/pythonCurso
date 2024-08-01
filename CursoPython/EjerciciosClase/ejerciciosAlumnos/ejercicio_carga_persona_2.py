# ingresar 4 persona con nombre completo, direccion y edad
# mostrar los datos de la persona mayo edad y menor edad
#! en que posicion se cargo
#* el promedio de edades

nombre = input("ingrese el nombre de la persona: ")
edad = input("ingrese la edad de la persona: ")
direccion = input("ingrese direccion de la persona: ")

promedio = 0 #aca voy a calcular el promedio de las edades
posicion_mayor = 0 #aca voy a guardar la posicion de la persona mayor
edad_mayor =  0 #aca voy a guardar la edad mayor
nombre_mayor = "" #aca voy a guardar el nombre de la persona mayor
direccion_mayor = "" #aca voy a guardar la direccion de la persona mayor
#ahora voy a calcular el menor
posicion_menor = 0 #aca voy a guardar la posicion de la persona menor
edad_menor =  0 #aca voy a guardar la edad menor
nombre_menor = "" #aca voy a guardar el nombre de la persona menor
direccion_menor = "" #aca voy a guardar la direccion de la persona menor

suma_de_edades = 0 #aca voy a guardar la suma de las edades


#promedio = edad1 + edad2 + edad3 + edad4 / 4

# if edad_1.isdigit(): #si esto es un numero entero lo cambia
#     edad_1 = int(edad_1) # cambia el numero que estaba en string a integer (numero )
# else:
#     print("pusiste cualquier cosa")
#     exit()#temina el programa

if not edad.isdigit(): #si esto es un numero entero lo cambia
    print("pusiste cualquier cosa ahora vas a tener que empezar de 0")
    exit()#temina el programa

edad = int(edad) # cambia el numero que estaba en string a integer (numero )
nombre_mayor  =  nombre #guardo variable nombre_mayor con el dato que tengo guardado en nombre
nombre_menor = nombre # se guarda el valor pq puede llegar a ser el menor
direccion_mayor = direccion # lo mismo aca
direccion_menor = direccion # lo mismo aca
edad_mayor = edad # aca guardo la edad
edad_menor = edad # aca guardo la edad
posicion_menor = 1
posicion_mayor = 1
suma_de_edades +=  edad #aca guardo la suma de las edades

#voy a ingresar los datos de la persona 2
nombre = input("ingrese el nombre de la segunda persona: ")
edad = input("ingrese la edad de la segunda persona: ")
direccion = input("ingrese direccion de la segunda persona: ")
if not edad.isdigit(): #si esto es un numero entero lo cambia
    print("pusiste cualquier cosa")
    exit()#temina el programa

edad = int(edad) # cambia el numero que estaba en string a integer (numero )
if edad > edad_mayor:
    edad_mayor = edad
    nombre_mayor = nombre
    direccion_mayor = direccion
    posicion_mayor = 2
if edad < edad_menor:
    edad_menor = edad
    nombre_menor = nombre
    direccion_menor = direccion
    posicion_menor = 2

suma_de_edades +=  edad #aca guardo la suma de las edades

#voy a ingresar los datos de la persona 3
nombre = input("ingrese el nombre de la tercera persona: ")
edad = input("ingrese la edad de la tercera persona: ")
direccion = input("ingrese direccion de la tercera persona: ")
if not edad.isdigit(): #si esto es un numero entero lo cambia
    print("pusiste cualquier cosa")
    exit()#temina el programa

edad = int(edad) # cambia el numero que estaba en string a integer (numero )
if edad > edad_mayor:
    edad_mayor = edad
    nombre_mayor = nombre
    direccion_mayor = direccion
    posicion_mayor = 3

if edad < edad_menor:
    edad_menor = edad
    nombre_menor = nombre
    direccion_menor = direccion
    posicion_menor = 3

suma_de_edades +=  edad #aca guardo la suma de las edades

#voy a ingresar los datos de la persona 4
nombre = input("ingrese el nombre de la cuarta persona: ")
edad = input("ingrese la edad de la cuarta persona: ")
direccion = input("ingrese direccion de la cuarta persona: ")
if not edad.isdigit(): #si esto es un numero entero lo cambia
    print("pusiste cualquier cosa")
    exit()#temina el programa

edad = int(edad) # cambia el numero que estaba en string a integer (numero )
if edad > edad_mayor:
    edad_mayor = edad
    nombre_mayor = nombre
    direccion_mayor = direccion
    posicion_mayor = 4

if edad < edad_menor:
    edad_menor = edad
    nombre_menor = nombre
    direccion_menor = direccion
    posicion_menor = 4

suma_de_edades +=  edad #aca guardo la suma de las edades
promedio = suma_de_edades /4
print(f"el promedio de las edad ingresas es: {promedio}")
print(f"la persona de mayor edad es:{nombre_mayor} y tiene {edad_mayor} años y vive en {direccion_mayor} y la posicion es {posicion_mayor}")

print(f"la persona de menor edad es:{nombre_menor} y tiene {edad_menor} años y vive en {direccion_menor} y la posicion es {posicion_menor}")
