#Realizar un programa que permita ingresar solo texto

#variable = ""
#variable = input("Ingrese solo texto: ")

""" # Forma 1 de detectar si es solo texto
if variable.isdigit():
    print("Era solo texto")
    exit()
else:
    print(f"El valor de la variable es {variable}")
"""
""" # Forma 2 de detectar si es solo texto (Negando el if)
if not variable.isdigit():
    print(f"El valor de la variable es {variable}")
else:
    print("Era solo texto")
"""
texto = "Hola, mundo. Hola, Tierra"
#print(texto)
texto_reemplazado = texto.replace("Hola", "Adiós")
#print(texto_reemplazado)

numero_de_holas = texto_reemplazado.count("Hola")
#print(numero_de_holas)
texto = "Hola, mundo"

texto = "Hola, mundo, mundo, chau mundo Diego, Gonzalo, Javier, Monica, Shirley, Guillermo, Gaspar, Fermin"
palabra_a_buscar = input("Ingrese la palabra a buscar: ")

posicion_primer_mundo = texto.find(palabra_a_buscar)
longitud_de_palabra = len(palabra_a_buscar) #! AGREGAR A LA TEORIA
#print(longitud_de_palabra)
#print(posicion_primer_mundo)
#print(posicion_ultimo_mundo)
#posicion_ultimo_mundo = texto.rfind("mundo")

if posicion_primer_mundo > 0:
    print(f"La variable a cortar es: {texto[posicion_primer_mundo : posicion_primer_mundo + longitud_de_palabra]} existe en la posicion {posicion_primer_mundo} y la longitud es {longitud_de_palabra}")
else:
    print("La palabra que buscas, no existe")



# Realizar un programa que permita ingresar solo texto y los muestre todo en mayuscula
# Realizar un programa que permita ingresar solo numeros, si no se cumple este requisito, que me de la hasta 2 oportunidades mas y me muestre la cantidad de veces que lo hice mal.