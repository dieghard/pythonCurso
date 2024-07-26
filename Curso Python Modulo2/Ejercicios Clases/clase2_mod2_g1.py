#ingresando 3 numeros indicar cual es mayor
def ingrese_un_numero ():
    while True:
        numero = input ("Ingrese un numero: ")
        if numero.isdigit ():
            numero = int (numero)
            if numero > 0: 
                break
            else:
                print ("Ingrese un numero mayor a 0")
        else:
            print("El numero ingresado no es valido")
    return numero

mayor = 0
menor = 0
suma = 0
for contador in range (3):
    numero = ingrese_un_numero ()
    print (f"El {contador+1}° N° ingresado es: {numero}")
    if numero > mayor:
        mayor = numero
    if numero < menor or menor == 0:
        menor = numero
    suma = suma + numero

print (f"El numero mayor es {mayor}")
print (f"El numero menor es {menor}")
print (f"El promedio es igual: {suma/3}")