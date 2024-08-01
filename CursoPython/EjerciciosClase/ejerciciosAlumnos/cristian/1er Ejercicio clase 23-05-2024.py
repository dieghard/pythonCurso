texto = ""
texto = input (" Ingrese un texto: ")
texto = texto.capitalize()
if texto.isdigit():
    print ("Es un numero, ingreso correctamente un texto")
    exit()
else:
    print (f"{texto}")
