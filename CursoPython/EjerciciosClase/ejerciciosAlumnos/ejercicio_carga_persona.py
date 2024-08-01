# INGRESAR 4 PERSONAS CON NOMBRE Y APELLIDP
# DIRECCION Y EDAD
# Y MUESTRE LOS DATOS DE LAS PERSONAS
#EL DE MAYOR EDAD
# EL DE MENOR EDAD
# Y EN QUE POSICION SE CARGO

edad = input("Ingrese una edad:")
edad_mayor = 0
edad_menor = 0
nombre =  input("Ingrese el nombre completo:")
direccion = input("Ingrese la dirección:")
posicion = 1
nombre_mayor = nombre #aca me guardo el nombre de la persona de mayor edad
direccion_mayor = direccion #aca me guardo la direccion de la persona de mayor edad
nombre_menor = nombre
direccion_menor = direccion
poscion_menor = 1

if edad.isdigit(): #verifico que sea un numero
    edad = int(edad)
    edad_mayor = edad
    edad_menor = edad
    suma_edades = edad # aca sumo las edades
else:
    print("No ingresaste un numero, ultimo intento!")
    edad = input("Ingrese una edad:")
    if edad.isdigit():
        edad = int(edad)
        edad_mayor = edad
        edad_menor = edad
        suma_edades = edad # aca sumo las edades
    else:
        print("Como no ingresaste un numero la edad se pone en 0")
        exit() # si ingrea mal de de nuevo termina el programa

#edad ingresamos la edad 2
edad = input("Ingrese una edad:")
nombre =  input("Ingrese el nombre completo:")
direccion = input("Ingrese la dirección:")

if edad.isdigit():
    edad = int(edad)
else:
    print("Como no ingresaste un numero la edad se pone en 0")
    exit()

suma_edades  +=  edad # aca sumo las edades

if edad >= edad_mayor:
    edad_mayor = edad
    posicion = 2
    nombre_mayor = nombre
    direccion_mayor = direccion

if edad <= edad_menor:
    edad_menor = edad
    posicion_menor = 2
    nombre_menor = nombre
    direccion_menor = direccion
#edad ingresamos la edad 3
edad = input("Ingrese una edad:")
nombre =  input("Ingrese el nombre completo:")
direccion = input("Ingrese la dirección:")

if edad.isdigit():
    edad = int(edad)
else:
    print("Como no ingresaste un numero la edad se pone en 0")
    exit()

suma_edades  +=  edad # aca sumo las edades

if edad >= edad_mayor:
    edad_mayor = edad
    posicion = 3
    nombre_mayor = nombre
    direccion_mayor = direccion

if edad <= edad_menor:
    edad_menor = edad
    posicion_menor = 3
    nombre_menor = nombre
    direccion_menor = direccion
#edad ingresamos la edad 4
edad = input("Ingrese una edad:")
nombre =  input("Ingrese el nombre completo:")
direccion = input("Ingrese la dirección:")

if edad.isdigit():
    edad = int(edad)
else:
    print("Como no ingresaste un numero la edad se pone en 0")
    exit()

suma_edades  +=  edad # aca sumo las edades

if edad >= edad_mayor:
    edad_mayor = edad
    nombre_mayor = nombre
    direccion_mayor = direccion
    posicion = 4
if edad <= edad_menor:
    edad_menor = edad
    posicion_menor = 4
    nombre_menor = nombre
    direccion_menor = direccion

promedio = suma_edades / 4 # aca calculo el promedio

# aca calculo el mayor
print (f"La person de mayor edad es {nombre_mayor} con {edad_mayor} años y vive en {direccion_mayor} en la posición {posicion}")

# aca calculo menor!!!!

print (f"La person de menor edad es {nombre_menor} con {edad_menor} años y vive en {direccion_menor} y fue cargado en la posición {posicion_menor}")

print(f"El promedio de las edades es: {promedio}")