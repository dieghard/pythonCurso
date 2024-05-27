""" programa que solo ingrese palabras con 3 intentos (QUITAR LAS COMILLAS TRIPLES PARA QUE ANDE)
print(f"la variable continuar tiene el valor:{continuar}")
var = input("Ingrese una palabra:")

if var.isdigit():
    print("Error : ESTE ES TU PRIMER ERROR!!!!! Es un numero")
    continuar = True
    print(f"la variable continuar tiene el valor:{continuar}")
else:
    continuar = False
    print(f"la variable continuar tiene el valor:{continuar}")

    print(f"la variable continuar tiene el valor:{continuar}")


if  continuar : #Recuerden que al usar un booleano en if no hace falta una condicion ya que se tomará el valor de él para la condición(en este caso si es True, ejecuta el codigo)
    var = input("Ingrese por segunda vez una palabra:")

if var.isdigit():
    print("Error : SEGUNDA VEZ ERROR!!!!! DALEEEEEEEEEEEEEEEEEE")
    continuar = True
    print(f"la variable continuar tiene el valor:{continuar}")

else:
    continuar = False
    print(f"la variable continuar tiene el valor:{continuar}")

if  continuar :
    var = input("Ingrese por tercera vez una palabra:")
    print(f"la variable continuar tiene el valor:{continuar}")

if var.isdigit():
    print("ALPISTE TU TERCER ERROR:Fue tu ultima oportunidad!!!!!")
    exit()

print (f"la palabra o letra que ingresaste es:{var}")
""" #(QUITAR LAS COMILLAS TRIPLES PARA QUE ANDE)



texto = "Hola, mundo como te va, Diego, Gaspar, Marcelo, Salvador, Brisa, Franco, Pia, Camila, Silvia, Sofia"
texto_a_buscar = input("Ingrese el texto a buscar: ")
posicion_texto = texto.find(texto_a_buscar) #Buscamos la posicion donde comienza la palabra ingresada por el usuario
contar_letras = len(texto_a_buscar) #Contamos la cantidad de letras que tiene la palabra ingresada por el usuario



#print(posicion_texto)

if posicion_texto == -1:  #Si la palabra no existe find muestra -1
    print("No se encontro la palabra")
    exit()
else: #Si la palabra existe
    print(f"Se encontro la palabra {texto[posicion_texto : posicion_texto + contar_letras]} en la posicion {posicion_texto} y tiene {contar_letras} caracteres")