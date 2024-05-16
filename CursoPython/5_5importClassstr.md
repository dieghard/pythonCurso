# COMO RESTRINGIR A SOLO NUMEROS??? 🧐🤯

#### METODOS DE LA CLASE La clase str

Estos métodos te permiten manipular el texto de diferentes maneras, como verificar si contiene letras mayúsculas, minúsculas o números, buscar subcadenas, unir cadenas, convertir mayúsculas a minúsculas y viceversa, etc.

#### La clase str en Python representa cadenas de caracteres. Es uno de los tipos de datos fundamentales del lenguaje y se utiliza para almacenar texto.

#### SOLO NUMEROS

```python
entrada=input("Ingrese un número: ")
print (type(entrada))
if entrada.isdigit():
	print(f"el numero ingresado es {entrada}.")
else:
	print("Error: Debe ingresar un número válido.")
	exit()
```

## SOLO TEXTO 🗒️

entrada=input("Ingrese texto: ")

ifentrada.isalpha() orentrada.isspace():

    print(f"el text ingresado es {entrada}.")

else:

    print("Error: Debe ingresar solo texto (letras o espacios).")

### Algunos ejemplos:

| Método         | Descripción                                                                          | Ejemplo                                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isalpha()`    | Verifica si todos los caracteres son letras.                                         | `texto = "palabra"; es_letra = texto.isalpha(); print(es_letra)`(Salida: True)                                                                           |
| `isdigit()`    | Verifica si todos los caracteres son dígitos.                                        | `texto = "12345"; es_digito = texto.isdigit(); print(es_digito)`(Salida: True)                                                                           |
| `isalnum()`    | Verifica si todos los caracteres son alfanuméricos (letras y números).               | `texto = "texto123"; es_alfanumerico = texto.isalnum(); print(es_alfanumerico)`(Salida: True)                                                            |
| `islower()`    | Verifica si todos los caracteres son minúsculas.                                     | `texto = "palabra en minusculas"; es_minuscula = texto.islower(); print(es_minuscula)`(Salida: True)                                                     |
| `isupper()`    | Verifica si todos los caracteres son mayúsculas.                                     | `texto = "PALABRA EN MAYÚSCULAS"; es_mayuscula = texto.isupper(); print(es_mayuscula)`(Salida: True)                                                     |
| `isspace()`    | Verifica si todos los caracteres son espacios en blanco.                             | `texto = " "; es_espacio = texto.isspace(); print(es_espacio)`(Salida: True)                                                                             |
| `startswith()` | Verifica si la cadena comienza con una subcadena específica.                         | `texto = "Hola mundo"; empieza_con_hola = texto.startswith("Hola"); print(empieza_con_hola)`(Salida: True)                                               |
| `endswith()`   | Verifica si la cadena termina con una subcadena específica.                          | `texto = "Hola, mundo, mundo"; termina_con_mundo = texto.endswith("mundo"); print(termina_con_mundo)`(Salida: True)                                      |
| `find()`       | Busca la primera aparición de una subcadena dentro de la cadena.                     | `texto = "Hola, mundo"; posicion_hola = texto.find("Hola"); print(posicion_hola)`(Salida: 0)                                                             |
| `rfind()`      | Busca la última aparición de una subcadena dentro de la cadena.                      | `texto = "Hola, mundo, mundo"; posicion_ultimo_mundo = texto.rfind("mundo"); print(posicion_ultimo_mundo)`(Salida: 15)                                   |
| `count()`      | Cuenta el número de apariciones de una subcadena dentro de la cadena.                | `texto = "Hola, Hola, mundo"; numero_de_holas = texto.count("Hola"); print(numero_de_holas)`(Salida: 2)                                                  |
| `replace()`    | Reemplaza todas las apariciones de una subcadena por otra subcadena.                 | `texto = "Hola, mundo. Hola, Tierra"; texto_reemplazado = texto.replace("Hola", "Adiós"); print(texto_reemplazado)`(Salida: Adiós, mundo. Adiós, Tierra) |
| `strip()`      | Elimina los espacios en blanco al principio y al final de la cadena.                 | `texto = " Hola mundo "; texto_sin_espacios = texto.strip(); print(texto_sin_espacios)`(Salida: Hola mundo)                                              |
| `lstrip()`     | Elimina los espacios en blanco al principio de la cadena.                            | `texto = " Hola mundo"; texto_sin_espacios_izquierda = texto.lstrip(); print(texto_sin_espacios_izquierda)`(Salida: Hola mundo)                          |
| `rstrip()`     | Elimina los espacios en blanco al final de la cadena.                                | `texto = "Hola mundo "; texto_sin_espacios_derecha = texto.rstrip(); print(texto_sin_espacios_derecha)`(Salida: Hola mundo)                              |
| `upper()`      | Convierte todos los caracteres de la cadena a mayúsculas.                            | `texto = "hola mundo"; texto_mayusculas = texto.upper(); print(texto_mayusculas)`(Salida: HOLA MUNDO)                                                    |
| `lower()`      | Convierte todos los caracteres de la cadena a minúsculas.                            | `texto = "HOLA MUNDO"; texto_minusculas = texto.lower(); print(texto_minusculas)`(Salida: hola mundo)                                                    |
| `capitalize()` | Convierte el primer caracter de la cadena a mayúscula y deja el resto en minúsculas. | `texto = "hola mundo"; texto_capitalizado = texto.capitalize(); print(texto_capitalizado)`(Salida:                                                       |

# Para Numeros INT 🕘

| Método                     | Descripción                                                                                  | Ejemplo                                                                                                                                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isinstance(valor, int)`   | Verifica si el valor es un número entero (int).                                              | `valor = 10; es_entero = isinstance(valor, int); print(es_entero)`(Salida: True)                                                                                                                         |
| `type(valor) is int`       | Verifica si el tipo de dato del valor es int.                                                | `valor = 10; es_entero = type(valor) is int; print(es_entero)`(Salida: True)                                                                                                                             |
| `.isdigit()`               | Verifica si el valor es una cadena que contiene solo dígitos (números).                      | `valor_string = "12345"; es_digito = valor_string.isdigit(); print(es_digito)`(Salida: True)                                                                                                             |
| `int(valor, base)`         | Convierte un valor a un número entero (int), especificando la base numérica si es necesario. | `valor_string = "10"; numero_entero = int(valor_string); print(numero_entero)`(Salida: 10)                                                                                                               |
| `try...except ValueError:` | Intenta convertir un valor a un número entero (int) y maneja el error si no es posible.      | `valor_string = "hola"; try: numero_entero = int(valor_string); print(numero_entero) except ValueError: print("Error: El valor no es un número entero")`(Salida: Error: El valor no es un número entero) |

- Las funciones `isinstance()` y `type()` son más confiables para verificar si un valor es un número entero, ya que no dependen de la representación como cadena.
- La función `.isdigit()` es útil para validar cadenas de texto que contienen solo dígitos.
- La función `int()` se puede usar para convertir valores a números enteros, pero es importante manejar posibles errores de conversión.

# import 👨‍🚀👩‍🚀🚀

En Python, la palabra clave import se utiliza para hacer que el código de un módulo esté disponible en otro.

Esto es importante para estructurar el código de manera efectiva, ya que permite reutilizar código y mantener los proyectos organizados.

### ¿Qué es un módulo?

Un módulo es un archivo que contiene código Python. Puede definir funciones, clases y variables, y también puede incluir código ejecutable. Los módulos se utilizan para agrupar código relacionado y para hacer que el código sea más fácil de reutilizar.

### ¿Cómo importar un módulo?

Para importar un módulo, se utiliza la siguiente sintaxis:

import nombre_del_módulo

¿Por qué utilizar import?

Reutilización de código: Permite reutilizar código que ya se ha escrito, lo que ahorra tiempo y esfuerzo.

Modularidad: Ayuda a modularizar el código, lo que lo hace más fácil de entender y mantener.

Acceso a funciones y variables predefinidas: Proporciona acceso a funciones y variables predefinidas en la biblioteca estándar de Python y en otros módulos de terceros.

OBTENER LA FECHA DEL DIA DE HOY

> ```python
> import datetime
>
> # Obtener la fecha actual
> fecha_actual = datetime.date.today()
>
> # Formatear la fecha en dd/mm/yyyy
> fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
>
> print(f"Fecha actual en dd/mm/yyyy: {fecha_formateada}")
> ```

### Obtener la hora actual :

```python
import datetime

hora_actual = datetime.datetime.now()

print(hora_actual)


```

- Se importa el módulo `datetime` utilizando la instrucción `import`.
- Se llama a la función `datetime.datetime.now()` para obtener la fecha y hora actuales. Esto devuelve un objeto `datetime`.
- Se asigna el objeto `datetime` a una variable llamada `hora_actual`.
- Se imprime la variable `hora_actual` utilizando la función `print()`.
- **Formatear la hora:**

Puedes formatear la hora actual a un formato específico utilizando el método `strftime()` del objeto `datetime`. Este método toma una cadena de formato como argumento y devuelve una cadena formateada.

**Ejemplo:**

```Python
import datetime

hora_actual = datetime.datetime.now().time()

hora_formateada = hora_actual.strftime('%H:%M:%S')

print(hora_formateada)
```

**Para obtener la hora actual en Python,** se utiliza la función `now()` del módulo `datetime`. Esta función devuelve un objeto `datetime` que representa la fecha y hora actuales, con una precisión de milisegundos.

**Ejemplo:**

Python

```python
import datetime

hora_actual = datetime.datetime.now()

print(hora_actual)
```

Este código imprimirá la siguiente salida:

```
2024-05-16 11:53:00.000000
```

**Explicación:**

1. Se importa el módulo `datetime` utilizando la instrucción `import`.
2. Se llama a la función `datetime.datetime.now()` para obtener la fecha y hora actuales. Esto devuelve un objeto `datetime`.
3. Se asigna el objeto `datetime` a una variable llamada `hora_actual`.
4. Se imprime la variable `hora_actual` utilizando la función `print()`.

**Obtener solo la hora:**

Si solo necesitas obtener la hora actual, puedes usar el método `time()` del objeto `datetime`. Este método devuelve un objeto `time` que representa la hora actual.

**Ejemplo:**

Python

```python
import datetime

hora_actual = datetime.datetime.now().time()

print(hora_actual)
```

Este código imprimirá la siguiente salida:

```
11:53:00.000000
```

**Formatear la hora:**

Puedes formatear la hora actual a un formato específico utilizando el método `strftime()` del objeto `datetime`. Este método toma una cadena de formato como argumento y devuelve una cadena formateada.

**Ejemplo:**

```python
import datetime

hora_actual = datetime.datetime.now().time()

hora_formateada = hora_actual.strftime('%H:%M:%S')

print(hora_formateada)

```

En este ejemplo, la cadena de formato `'%H:%M:%S'` indica que queremos formatear la hora con el formato "HH:MM:SS", donde:

- `%H` representa la hora en formato de 24 horas.
- `%M` representa los minutos.
- `%S` representa los segundos.

**Zona horaria:**

La función `now()` utiliza la zona horaria local por defecto. Si necesitas obtener la hora en una zona horaria diferente, puedes especificar la zona horaria como argumento de la función.

```python
import datetime

zona_horaria = datetime.timezone(datetime.timedelta(hours=-3))

hora_actual_en_nueva_york = datetime.datetime.now(zona_horaria)

print(hora_actual_en_nueva_york)
```

# ejercicio de diferencias horarias

```python
import datetime

# Zona horaria actual (-3)
zona_horaria_actual = datetime.timezone(datetime.timedelta(hours=-3))

# Zona horaria de Nueva York (-5)
zona_horaria_nueva_york = datetime.timezone(datetime.timedelta(hours=-5))

# Obtener hora actual en tu zona horaria
hora_actual = datetime.datetime.now(zona_horaria_actual)

# Obtener hora actual en Nueva York
hora_nueva_york = datetime.datetime.now(zona_horaria_nueva_york)

# Calcular la diferencia de horas
diferencia_horas = hora_actual - hora_nueva_york

# Formatear las horas para mostrarlas
hora_actual_formateada = hora_actual.strftime('%H:%M:%S')
hora_nueva_york_formateada = hora_nueva_york.strftime('%H:%M:%S')

# Imprimir resultados
print(f"Hora actual en tu zona horaria (-3): {hora_actual_formateada}")
print(f"Hora actual en Nueva York (-5): {hora_nueva_york_formateada}")
print(f"Diferencia de horas: {diferencia_horas}")
```

# El módulo random en Python proporciona funciones para generar números aleatorios. ejemplo:

```python
import random

numero_aleatorio = random.randint(1, 10)

print(f"Número aleatorio entre 1 y 10: {numero_aleatorio}")
```

**Generar un número aleatorio con decimales entre 0 y 1:**

```python
import random

decimal_aleatorio = random.random()

print(f"Número aleatorio decimal entre 0 y 1: {decimal_aleatorio}")
```

La función `random.random()` genera un número aleatorio con decimales entre 0.0 (inclusive) y 1.0 (exclusive).

**Elegir un elemento aleatorio de una lista:**

```python
import random

frutas = ["🍎", "🍐", "🍊", "🍍"]

fruta_elegida = random.choice(frutas)

print(f"Fruta elegida aleatoriamente: {fruta_elegida}")
```
