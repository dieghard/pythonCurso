#Realizar un programa que permita ingresar solo texto
#variable = ""
#variable = input("Ingrese solo texto: ")

""" # Forma 1 de detectar si es solo texto #(QUITAR LAS COMILLAS TRIPLES PARA QUE ANDE)
if variable.isdigit():
    print("Era solo texto")
    exit()
else:
    print(f"El valor de la variable es {variable}")
"""#(QUITAR LAS COMILLAS TRIPLES PARA QUE ANDE) 

""" # Forma 2 de detectar si es solo texto (Negando el if)#(QUITAR LAS COMILLAS TRIPLES PARA QUE ANDE)
if not variable.isdigit():
    print(f"El valor de la variable es {variable}")
else:
    print("Era solo texto")
"""#(QUITAR LAS COMILLAS TRIPLES PARA QUE ANDE)


texto = "Hola, mundo. Hola, Tierra"
#print(texto)
texto_reemplazado = texto.replace("Hola", "Adiós")
#print(texto_reemplazado)

numero_de_holas = texto_reemplazado.count("Hola")
#print(numero_de_holas)
texto = "Hola, mundo"

texto = "Hola, mundo, mundo, chau mundo Diego, Gonzalo, Javier, Monica, Shirley, Guillermo, Gaspar, Fermin"
palabra_a_buscar = input("Ingrese la palabra a buscar: ")

posicion_texto = texto.find(palabra_a_buscar)
longitud_de_palabra = len(palabra_a_buscar) 
#print(longitud_de_palabra)
#print(posicion_texto)
#print(posicion_ultimo_mundo)
#posicion_ultimo_mundo = texto.rfind("mundo")

if posicion_texto > 0:
    print(f"La variable a cortar es: {texto[posicion_texto : posicion_texto + longitud_de_palabra]} existe en la posicion {posicion_texto} y la longitud es {longitud_de_palabra}")
else:
    print("La palabra que buscas, no existe")

