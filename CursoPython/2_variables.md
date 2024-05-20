# 🐍 Variables en Python🐍

---

## 🤔¿QUE ES UNA VARIABLE?: 🤔

> En programación, una variable es un espacio en la memoria de tu computadora que se utiliza para almacenar información de un determinado tipo de dato.
> Las variables se identifican con un nombre único y sus valores pueden cambiar.
> Pueden ser un valor:
>
> - Numerico,
>   - Entero(int): Números sin decimales, como 1, 2, 3, etc.
>   - De punto Flotante(float): Números con decimales, como 1.5, 2,3123, etc.
>   - Complejos (clompex): Números con una parte real y una parte imaginaria, como 1+2j, 3-4j, etc.
> - Texto (string): Por Ejemlo "Hola Mundo", "Curso de Programacion".
> - Booleanos (bool): Valores que solo pueden ser True o False. (Verdadero y Falso)
> - Fecha y Hora.
>
> ### Una vez almacenada se puede utilizar para realizar operaciones, mostrar resultados, etc.
>
> ---

## Veamos un Ejemplo

```python
miVariable = "Hola Mundo, muchaaaaaachos"
print (miVariable) la informacion de la variable se puede pisar.
miVariable = 10 * 10
print (miVariable)
# realice un software que permita mostrar la suma  dos variables

x = 10
y = 2
z = x * y
print (z)
```

---

## Concatenacion de String y Variables

```python
 print ("el valor de x es:", x)
 print ("el valor de y es:", y)
 print ("Resultado es:", z)
```

---

## NOMBRES DE VARIABLES:

> En la mayoría de lenguajes de programación existe el concepto de variables. Las variables permiten asignar nombres coherentes a información para ser reutilizada con facilidad.

---

# Tipos de Asignaciones (=)

## Simples

```python
str_color = 'Red'
num_of_cards = 56
pi_number = 13.1416
```

## Múltiples

> En las siguientes asignaciones se asignan valores a varias variables a la vez.

```python
str_red, str_blue = 'Red', 'Blue'
cards, half_cards = 56, 28
```

---

## Literales y expresiones

### Cuando se hacen asignaciones se pueden utilizar:

- Literales: son datos descritos directamente en el código.
- Es información estática, puede ser simple o usar instancias de clases.
  > La definición clave es que se conoce cuál será el valor asignado analizando el código.

```python
# Literales
a = 1
msg = 'Hello World'
total = 78 + 3.24
is_active = True
```

## Expresiones: son datos asignados tras la evaluación de una o varias sentencias. Suelen ser dinámicos y no se conoce el valor final analizando el código.

```python
# Expressions
a = arg1 + p
msg = 'Hello' + world_msg
position = prev_position + 89
```

---

## Keywords en Python

> En Python hay algunas palabras reservadas en que no pueden ser utilizadas como identificadores válidos. Se pueden encontrar en keyword.kwlist, y son los siguientes.

| Keywords     | en            | Python        |
| ------------ | ------------- | ------------- |
| \* `False`   | \* `assert`   | \* `return`   |
| \* `None`    | \* `break`    | \* `try`      |
| \* `True`    | \* `class`    | \* `while`    |
| \* `elif`    | \* `continue` | \* `with`     |
| \* `else`    | \* `def`      | \* `yield`    |
| \* `except`  | \* `del`      | \* `from`     |
| \* `finally` | \* `for`      | \* `global`   |
| \* `if`      | \* `import`   | \* `in`       |
| \* `is`      | \* `lambda`   | \* `nonlocal` |
| \* `not`     | \* `or`       | \* `pass`     |
| \* `raise`   | \* `try`      | \* `while`    |
| \* `with`    |               |               |

---

# ⚠ Nombres de variables en Python ⚠

> Según la PEP 8 (PEP 8 es una guía de estilo para Python que contiene recomendaciones para escribir código más legible y consistente. La guía abarca desde cómo nombrar variables hasta el número máximo de caracteres que debe tener una línea.)link: [PEP8 ](https://peps.python.org/pep-0008/)

### Los nombres de las variables de Python deben de escribirse en snake_case. 🐍 ejemplo hola_mundo

### ⚠ Además en deben de cumplir las siguientes características: ⚠

- Tienen que empezar por una letra o barra baja.
- El uso de keywords como nombres está prohibido.
- Los nombres deben de ser descriptivos.
- Deben de estar en minúsculas y separando palabras por barras bajas ‘\_’.
- Las constantes se escriben en mayúsculas y SNAKE_CASE.

### Nombres validos: ✔

- cat_color = 'Brown'
- number_of_threads = 8
- phone_number = 78469334212
- ISIN_CODE = 8479362
- CONSTANT_SPEED = 9.8

### Nombres invalidos: ❌

- .cat
- 0number
- `car
- -hello

---

## POSICION DE MEMORIA

### (en que posicion de memoria se guarda el valor de la variable)

```python
#con esto podemos saber la posicion de memoria
x = 10
print(id(x))
#==================================
```

---

## Buenas Practicas con Variables en Python

> Cuando hablamos de buenas practicas, nos referimos a aquellas formas de hacer codigo que pueden ayudarnos a escribirlo de manera más limpia y legible ¡a continuacion voy a destacar algunas que pueden ayudarte con las variables!

1. ### Nombres descriptivos: Usa nombres descriptivos para tus variables. Esto hace que tu código sea más fácil de entender. Por ejemplo, en lugar de x, podrías usar edad si estás almacenando la edad de alguien.

```python
# Mal
x = 25

# Bien
edad = 25
```

2. ### Evita nombres reservados: No uses nombres que ya están reservados por Python. Por ejemplo, no llames a una variable list o str, ya que estos son nombres de tipos de datos incorporados en Python.

```python
# Mal
list = [1, 2, 3]

# Bien
mi_lista = [1, 2, 3]
```

3. ### Convenciones de estilo: Sigue las convenciones de estilo de Python, como PEP 8. Por ejemplo, usa minúsculas para los nombres de las variables y separa las palabras con guiones bajos.

```python
# Mal
miVariable = 42
strMivariable = "HOLA"
intEdad =
# Bien
mi_variable = 42
```

4. ### Evita nombres genéricos: Evita nombres de variables demasiado genéricos que puedan confundir o no transmitir su propósito. Por ejemplo, no uses nombres como dato, valor, resultado, etc., a menos que sea realmente necesario y su significado esté claro en el contexto.

```python
# Mal
dato = 10

# Bien
numero_de_intentos = 10
```

5. ### Usa constantes en mayúsculas: Si tienes variables que son constantes y no van a cambiar, usa nombres en mayúsculas para distinguirlas.

```python
# Mal
pi = 3.14159

# Bien
PI = 3.14159
```

6. ### Inicializa variables cuando sea posible: Siempre que sea posible, inicializa tus variables cuando las declares. Esto hace que tu código sea más explícito y menos propenso a errores.

```python
# Mal
nombre = ""
edad = 0

# Bien
nombre = "Juan"
edad = 30

```

---

# Actividades 💬

## Escribir un programa que imprima un mensaje en la pantalla.

## Escribir un programa que sume dos números.

## Escribir 3 variables para que guarden Apellido y nombre - Email y telefono y mostrarlos en pantalla, con el siguiente mensaje "Hola, Mi nombre es: ..., te paso mi contacto telefonico: ... y mi email: ..."

## Escribe un programa donde una variable llamada contador cambie a lo largo de la ejecucion del programa, que su primer valor sea 0, cambie a 5 y posteriormente a 25 para al finalizar el programa volver a ser 5.

---

[VOLVER](/readme.md)
