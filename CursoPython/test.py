texto1 = "Hola "
texto2 = "Mundo "

resultado = texto1 + texto2
print(f"El resultado de concatenar texto1 y texto2 es: {resultado}")
resultado = texto1 + texto2 * 5
print(f"El resultado de multiplicar texto1 y texto2 * 5 es: {resultado}") 
#Tene en cuenta que como en matematica existen terminos y en el 
#caso de la multiplicacion anterior solamente afecto a la variable texto2,
#si queremos que se muestre la concatenacion de texto1 y texto2 5 veces 
#tenemos que hacer lo siguiente:
resultado = (texto1 + texto2) * 5
print(f"El resultado de multiplicar texto1 y texto2 * 5 es: {resultado}") 