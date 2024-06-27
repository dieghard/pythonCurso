# - Realizar un programa que permita ingresar solo texto y los muestre todo en mayuscula
entrada = input("Ingrese un texto: ")
if entrada.isalpha() or entrada.isspace():
    entrada_mayuscula = entrada.upper()
    print(f"el text ingresado es {entrada_mayuscula}.")
else:
    print("Error: Debe ingresar solo texto (letras o espacios).")