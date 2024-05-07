# Funciones en Python 🐍 (⚙)

## Las funciones en python son bloques de codigo reutilizables que se ejecutan cuando son llamadas. Ayudan a organizar el codigo, lo hacen mas legible y ¡permiten reutilizar código!

## 🛑Las Funciones tienen las siguientes ventajas: 🛑

- Reutilizacion de Código: Las funciones permiten escribir una vez y se pueden usar en cualquier parte del codigo.Esto evita duplicación de código y facilita el mantenimiento.
- Organizacion y Legibilidad: Las funciones ayudan a organizar el código en bloques lógicos.\_ Al dar nombres descriptivos a las funciones, el código se vuelve más legible y comprensible.
- Abstraccion: Las funciones ocultan los detalles de implementacion.
- Modularidad: Divide un problema grande en problemas más pequeños.

  > En resumen, las funciones son una herramienta poderosa en Python. Usalas con moderación y de manera inteligente para aprovechar sus beneficios mientras evitas sus desventajas.

---

# Sintaxis de una Función

```python
def nombre_de_la_funcion(parametros):
    #codigo de la función
    return valor_de_retorno
```

- def: es la **_palabra clave_** que indica la definicion de una función.
- nombre\*de_la_funcion: es el identificador \*\*\*único\_\*\* que usamos para llamar a la funcion.
  `En Python, la convención para nombrar funciones es usar letras minúsculas con palabras separadas por guiones bajos. Esto se conoce como snake_case.`
- parametros: son variables opcionales que pasamos a la función.
- return: es la **_palabra clave_** que devuelve valor desde la funcion al llamador.

---

## Ejemplos de Uso

Una simple funcion que suma dos números:

```python
def sumar(a, b):
    return a + b
 resultado = sumar(5,3)
 print(resultado) #Devuelve: 8
```

---

# Buenas Practicas con Funciones

- ## Nombres Descriptivos: Recuerda elegir nombres que describan claramente lo que hace la funcion.
- ## Documentacion: Usa documentos o comentarios para explicar que hace la funcion y que parametros espera(te será de ayuda dias despues de programar algo)
- ## Codigo limpio: Manten las funciones enfocadas en una sola accion o proposito.
- ## Las funciones son herramientas esenciales que te permiten escribir código más modular y mantenible.
- ## Recorda que los nombres van en snake_case (ej: mi_funcion)

---

# Funcion Lambda

### Las funciones lambda son una forma de crear funciones anónimas en una sola línea. Son utiles cuando necesitas una funcion por corto periodo de tiempo y no queres definirla con _def_

## Su Sintaxis es:

```python
lambda parametros: expresion
```

Para ver la diferencia con una funcion normal, volveremos a usar la que ya vimos "sumar" con lambda se veria asi:

```python
sumar = lambda a,b : a + b
print(sumar(5,3)) #Devuelve: 8
```

## 🛑Ventajas de las funciones Lambda🛑

- Son útiles para funciones simples y temporales.
- Se pueden usar en expresiones como argumentos de otras funciones.
- Reducen la necesidad de declarar funciones completas.

## 🚫Desventajas de las funciones Lambda🚫

- Son limitadas en funcionalidad(solo una expresión)
- No son tan legibles como las funciones regulares.
- No tienen nombres descriptivos.

---

# Actividades 💬

## Crear una prama que pasandole el nombre nos salude:

```python
def saludar(nombre):
  #Función que saluda a una persona por su nombre
  print(f"¡Hola {nombre}!")
# Ejemplo de uso
saludar("Juan")  # Imprime: ¡Hola Juan!
saludar("María")  # Imprime: ¡Hola María!
```

```
Explicación:
- La función saludar recibe un parámetro llamado nombre.
- El código dentro de la función imprime un mensaje de saludo personalizado utilizando el nombre pasado como parámetro.
- La función se llama dos veces, pasando diferentes nombres como argumentos.
```

## Ejemplo 2: Calcular el área de un cuadrado

```python
def calcular_area_cuadrado(lado):
  """Función que calcula el área de un cuadrado."""
  area = lado * lado
  return area

# Ejemplo de uso
lado = 5
area = calcular_area_cuadrado(lado)
print(f"El área del cuadrado es: {area}")  # Imprime: El área del cuadrado es: 25
```

```
Explicación:

- La función calcular_area_cuadrado recibe un parámetro llamado lado.
- El código dentro de la función calcula el área del cuadrado elevando el lado al cuadrado.
- La función utiliza la palabra clave return para devolver el valor del área calculada.
- La función se llama una vez, pasando el valor del lado como argumento.
- El valor devuelto por la función se almacena en la variable area.
 -Se imprime un mensaje con el valor del área calculada.
```

## Ordenar una lista de palabras:

```py
def ordenar_palabras(lista_palabras):
#Función que ordena una lista de palabras alfabéticamente.
lista_palabras.sort()
return lista_palabras

lista_palabras = input("Ingrese las palabras separadas por comas: ").split(",")
lista_palabras_ordenadas = ordenar_palabras(lista_palabras)
print(f"Lista de palabras ordenadas alfabéticamente: {lista_palabras_ordenadas}")
```

## Función Verificar si un número es par o impar

- Realice un programa que verifique si el numero ingresado por ⌨️ es par o impar.

## Función de Calcular el perimetro de un rectangulo 👶

- Realice un programa que ingresando la base , la altura calcule el perimetro de un rectangulo. (recuerde que la formula es Perimetro = 2 \* (base + altura)
  y tambien devuelva el area.

## Función de conversión de Temperatura. (Facil) 👶

Escribe una función que convierta la temperatura de Celsius a Fahrenheit y viceversa. La función debe aceptar dos argumentos: _el valor de la temperatura y una cadena_ que indique si se está convirtiendo a Celsius('C') o a Fahrenheit('F').

> Una ayuda practica ¡se necesita usar if, elif y else!
> formula celsius (temperatura - 32) \* 5/9
> formula Fahrenheit = temperatura \* 9/5 + 32

## Funcion de Calculo Factorial. (Facil) 👶

Escribe una funcion que calcule el factorial de un numero dado.

> El factorial de un número entero positivo se define como el producto de todos los enteros positivos menores o iguales al número, Ejemplo: Factorial de 4 = 24(4 x 3 x 2 x 1)

## Funcion de Secuencia Fibonacci (Medio)😐

Desarrolla una funcion que genere una lista con los primeros 'n' numeros de la secuencia de Fibonacci, donde cada numero es la suma de los dos anteriores comenzando con 0 y 1.

> Ejemplo el decimo número de la secuencia es: 34

## Funcion de encontrar el maximo entre 3 numeros

cree una funcion que permita ingresar 3 números y nos muestre cual es el mayor

## Generar una lista de números aleatorios:

Generar un programa que permita el ingreso de la cantidad de numeros aleatorios a generar y los muestre.

el numero minimo y el numero maximo
[VOLVER](/pythonCurso/readme.md)
