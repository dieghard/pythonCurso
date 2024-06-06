#Realizar un programa que permita ingresar solo texto y los muestre todo en mayuscula
texto = ""
texto = input (" Ingrese un texto")
texto = texto.capitalize()
if texto.isdigit():
    print ("Es un numero, ingreso correctamente un texto")
    exit()
else:
    print (f"{texto}")

## cuando escribo un numero, me devuelve LINEA 6, pero cuando ingreso un texto, me marca error y no me lo convierte, no me doy cuenta donde colocar" texto= texto.capitalize()"
