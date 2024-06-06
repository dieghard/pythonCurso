# ! Realizar un programa que permita ingresar solo numeros, si no se cumple este requisito, que me de la hasta 2 oportunidades más y me muestre la cantidad de veces que lo hice mal.
continuar = 0
var = input("Ingrese un numero: ")

contador = 0


if var.isdigit():
    print (f" El numero ingresado es: {var} ")
    continuar = False

else:
    continuar = True
    print (f" Ha ingresado una letra")
    print (f" Incorrecto, vuelva a ingresar un numero:  ")
    contador = contador + 1

var = input("Ingrese un numero: ")

if var.isdigit():
    print (f" El numero ingresado es: {var} ")
    continuar = False

else:
    continuar = True
    print (f" Ha ingresado una letra")
    print (f" Ultimo intento, Ingrese un numero:   ")
    contador = contador + 1

var = input("Ingrese un numero: ")

if var.isdigit():
    print (f" El numero ingresado es: {var} ")
    continuar = False

else:
    continuar = True
    print (f" Ha ingresado una letra")
    print (f" Ultimo intento, Ingrese un numero:   ")
    contador = contador + 1

print (f" Cometiste {contador} de errores, a seguir particiapando ")
exit()

