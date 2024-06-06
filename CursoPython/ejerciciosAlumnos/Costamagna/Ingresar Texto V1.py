#Realizar un programa que permita ingresar solo texto y los muestre todo en mayuscula
# Imprimir el borde superior
print("")
print("#"*80)
print("######                                                                    ######")
print("######                 Bienvenido                                         ###### ")
print("######                                                                    ######")
print("######      En este juego usted ingresara un texto en minuscula  🧐🚀     ###### ")
print("######      y nosotros lo pasaremos a mayuscula  🧐🚀                     ###### ")
print("######      El texto no debe incluir numero o caracteres 😛🚀             ###### ")
print("######      y no debe tener mas de 20 caracteres                          ######")
print("######                                                                    ######")
print("#"*80)
print("")
texto = ""
texto = input("Ingrese el texto: ")
cantidad_caracteres = int(len(texto))
print("\n"*50) #limpio la pantalla para la nueva presentacion
if texto.isalpha and texto.islower() and cantidad_caracteres <20:
    texto = texto.upper() #transformo la frase a Mayuscula"
    espacios = (" "*(51- cantidad_caracteres))
    print("")
    print("#"*80)
    print("######                                                                    ######")
    print("######      Su texto a sido trascripto a mayuscula                        ###### ")
    print("######                                                                    ######")
    print(f"######          {texto}  🧐🚀 {espacios}######")
    print("######                                                                    ######")
    print("#"*80)
else:
    print("")
    print("#"*80)
    print("######                                                                    ######")
    print("######   Debe ingresar solo texto (letras o espacios) en minuscula        ###### ")
    print("######   Debe ingresar un maximo de 20 caracteres                         ######")
    print("######                                                                    ######")
    print("#"*80)
    print("")
    print("")