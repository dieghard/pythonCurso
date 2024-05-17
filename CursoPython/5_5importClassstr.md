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

# CALCULAR LA FECHA DEL CUMPLEAÑOS

```python
from datetime import date, datetime

# Calcular edad
fecha_nacimiento = date(1990, 5, 25)  # Año, mes, día
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
