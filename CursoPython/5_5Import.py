
##* SOLO NUMEROS
entrada = input("Ingrese un número: ")
print (type(entrada))
print (entrada.isdigit())

if  entrada.isdigit()  :
    print(f"el numero ingresado es {entrada}.")
else:
    print(f"Error: Debe ingresar un número válido. fijate lo que pusiste!{
        entrada}")
    exit


entrada = input("Ingrese un texto: ")
print (type(entrada))
print (entrada.isdigit())

if not  entrada.isdigit()  :
    print(f"el text ingresado es {entrada}.")
else:
    print(f"Error: Debe ingresar un texto válido. fijate lo que pusiste!{
        entrada}")
    exit

  ## SOLO TEXTO
entrada = input("Ingrese texto: ")
if entrada.isalpha() or entrada.isspace():
    print(f"el text ingresado es {entrada}.")
else:
    print("Error: Debe ingresar solo texto (letras o espacios).")

# METODOS DE LA CLASE La clase str
#  Estos métodos te permiten manipular el texto de diferentes maneras, como verificar si contiene letras mayúsculas, minúsculas o números, buscar subcadenas, unir cadenas, convertir mayúsculas a minúsculas y viceversa, etc.

# La clase str en Python representa cadenas de caracteres. Es uno de los tipos de datos fundamentales del lenguaje y se utiliza para almacenar texto.

# algunos ejemplos de cómo se usan estos métodos:
# capitalize(): Convierte el primer caracter de la cadena a mayúscula y deja el resto en minúsculas.
texto = "hola mundo"
texto_capitalizado = texto.capitalize()
print(texto_capitalizado)  # Salida: Hola mundo

# upper(): Convierte todos los caracteres de la cadena a mayúsculas.
texto = input("ingrese un texto:")
print(texto.upper())  # Salida: HOLA MUNDO

#lower(): Convierte todos los caracteres de la cadena a minúsculas.
texto = "HOLA MUNDO"
texto_minusculas = texto.lower()
print(texto_minusculas)  # Salida: hola mundo

#isalnum(): Verifica si todos los caracteres de la cadena son alfanuméricos (letras y números).
texto = "texto123"
es_alfanumerico = texto.isalnum()
print(es_alfanumerico)  # Salida: True

texto = "texto con espacios"
es_alfanumerico = texto.isalnum()
print(es_alfanumerico)  # Salida: False

#isalpha(): Verifica si todos los caracteres de la cadena son letras.
texto = "palabra"
es_letra = texto.isalpha()
print(es_letra)  # Salida: True

texto = "palabra123"
es_letra = texto.isalpha()
print(es_letra)  # Salida: False

#isdigit(): Verifica si todos los caracteres de la cadena son dígitos (números).
texto = "12345"
es_digito = texto.isdigit()
print(es_digito)  # Salida: True

texto = "texto con seis"
es_digito = texto.isdigit()
print(es_digito)  # Salida: False

# mas data : https://docs.python.org/es/3/library/string.html

valor = 10

if isinstance(valor, int):
    print(f"El valor {valor} es un número entero.")
else:
    print(f"El valor {valor} no es un número entero.")


valor = 10

if type(valor) is int:
    print(f"El valor {valor} es un número entero.")
else:
    print(f"El valor {valor} no es un número entero.")


valor_string = "12345"
if valor_string.isdigit():
    print(f"La cadena '{valor_string}' contiene solo dígitos.")
else:
    print(f"La cadena '{valor_string}' no contiene solo dígitos.")

#OBTENER LA FECHA DEL DIA DE HOY
import datetime
# Obtener la fecha actual
fecha_actual = datetime.date.today()
# Formatear la fecha en dd/mm/yyyy
fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
print(f"Fecha actual en dd/mm/yyyy: {fecha_formateada}")


# Usando la biblioteca time:
#La biblioteca time en Python también ofrece funciones para manejar fechas y horas.
import time
# Obtener la fecha actual como timestamp
tiempo_actual = time.time()
# Convertir el timestamp a una estructura de fecha
estructura_fecha = time.localtime(tiempo_actual)
# Formatear la fecha en dd/mm/yyyy
fecha_formateada = time.strftime("%d/%m/%Y", estructura_fecha)
print(f"Fecha actual en dd/mm/yyyy: {fecha_formateada}")

#El módulo random en Python proporciona funciones para generar números aleatorios. Aquí te muestro algunos ejemplos de uso:
import random
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")


# CALCULO DE CUMPLEAÑOS
from datetime import date, datetime

# Calcular edad
fecha_nacimiento = date(1980, 5, 16)  # Año, mes, día
hoy = date.today()
edad = hoy.year - fecha_nacimiento.year
if hoy.month < fecha_nacimiento.month or (hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day):
    edad -= 1
print(f"Edad: {edad} años")

# Calcular próximo cumpleaños
proximo_cumple = datetime(hoy.year, fecha_nacimiento.month, fecha_nacimiento.day)
if proximo_cumple < datetime.now():
    proximo_cumple = proximo_cumple.replace(year=hoy.year + 1)
diferencia = proximo_cumple - datetime.now()
print(f"Próximo cumpleaños en: {diferencia.days} días")