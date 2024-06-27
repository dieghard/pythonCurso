# realizar un programa que permita ingresar solo texto
entrada = input("Ingrese un texto: ")

if entrada.isalpha() or entrada.isspace():
    print(f"el text ingresado es {entrada}.")
else:
    print("Error: Debe ingresar solo texto (letras o espacios).")