import datetime
import random

# fecha_actual = datetime.date.today()
# fecha_formateada = fecha_actual.strftime ("%d/%m/%y")
# hora_actual = datetime.datetime.now()
# hora_formateada = hora_actual.strftime ("%H:%M")
# print (f"Comencemos el juego a las: {hora_formateada} hs. del dia: {fecha_formateada} ")

contador = 0
#numero_ingresado = 0
numero_aleatorio = random.randint (1, 10)

numero_ingresado = input ("Ingrese un numero entre el 1 y el 10: ")
contador += 1

if numero_ingresado.isdigit():
   numero_ingresado = int(numero_ingresado)
else:
   print ("Error No ingreso un numero, que fuera del JUEGO")
   exit()

if numero_ingresado == 0 or numero_ingresado >= 11:
    print ("No ingreso un numero entre el 1 y el 10, que fuera del JUEGO")
    exit()

if numero_aleatorio == numero_ingresado:
    print ("Felicitaciones usted a ganado")
    exit ()
if numero_aleatorio != numero_ingresado:
   numero_ingresado = input ("El numero ingresado no es correcto, igrese su segundo intento: ")
   contador +=1

if numero_ingresado.isdigit():
   numero_ingresado = int(numero_ingresado)
else:
   print ("Error No ingreso un numero, que fuera del JUEGO")
   exit()

if numero_ingresado == 0 or numero_ingresado >= 11:
    print ("No ingreso un numero entre el 1 y el 10, que fuera del JUEGO")
    exit()

if numero_aleatorio == numero_ingresado:
    print ("Felicitaciones usted a ganado")
    exit ()
if numero_aleatorio != numero_ingresado:
   numero_ingresado = input ("El numero ingresado no es correcto, igrese su tercer intento: ")
   contador +=1
if numero_ingresado.isdigit():
   numero_ingresado = int(numero_ingresado)
else:
   print ("Error No ingreso un numero, que fuera del JUEGO")
   exit()

if numero_ingresado == 0 or numero_ingresado >= 11:
    print ("No ingreso un numero entre el 1 y el 10, que fuera del JUEGO")
    exit()
if numero_aleatorio == numero_ingresado:
    print ("Felicitaciones usted a ganado")
    exit ()
if numero_aleatorio != numero_ingresado:
   print (f"El numero ingresado no es correcto, A PERDIDO!!!!")
   print (f"El numero aleatoreo era, {numero_aleatorio}")