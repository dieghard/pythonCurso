#RECORDA BORRAR LAS TRIPLES COMILLAS PARA QUE FUNCIONE(LINEA 3 Y 26)

"""#Solucion de GUILLE:
desplazamiento = 1

decision_usuario = input("Que accion desea realizar? Desencriptar o Encriptar (D/E)").upper()

if decision_usuario == "E":
    palabra_a_encriptar = input("Escriba para encriptar en formato cesar:")
else:
    palabra_a_encriptar = input("Escriba para desencriptar en formato cesar:")
# Le pedimos al usuario la palabra a encriptar
#Declaramos listas utiles para nuestro programa
lista_abecedario = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r", "s", "t", "u", "v", "w", "x", "y", "z"] #Lista completa del abecedario
lista_palabra = list(palabra_a_encriptar) #Convierte en lista la palabra a encriptar, separando en str cada letra.
print(lista_palabra) #Imprime la palabra encriptada transformada en lista

#Variables auxiliares
lista_indices = [] 
indice = 0
palabra_encriptada = []
palabra_desencriptada = []


#Comienzan los ciclos FOR:
for palabra in lista_palabra:
    indice =lista_abecedario.index(palabra) #obtiene el indice de cada letra
    if decision_usuario == "E":
        lista_indices.append(indice+desplazamiento) #Agrega a la lista_indices los indices + el desplazamiento declarado al principio del programa.
    else: 
        lista_indices.append(indice-desplazamiento) #Agrega a la lista_indices los indices + el desplazamiento declarado al principio del programa.
for numero in lista_indices:
    palabra_encriptada.append(lista_abecedario[numero]) #Agrega las letras modificadas a la lista de palabra_encriptada con el metodo append         
salida_encriptada ="".join(palabra_encriptada) #Convierte la lista a una palabra
print(salida_encriptada)
"""