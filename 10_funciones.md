# Funciones en Python (⚙)
## Las funciones en python son bloques de codigo reutilizables que se ejecutan cuando son llamadas. Ayudan a organizar el codigo, lo hacen mas legible y ¡permiten reutilizar código!

## 🛑Las Funciones tienen las siguientes ventajas: 🛑

- ### Reutilizacion de Código: Las funciones permiten escribir una vez y usar en cualquier lugar. Puedes definir una función una vez y llamarla en diferentes partes de tu programa. *Esto evita duplicación de código y facilita el mantenimiento.*
- ### Organizacion y Legibilidad: *Las funciones ayudan a organizar el código en bloques lógicos.* Al dar nombres descriptivos a las funciones, el código se vuelve más legible y comprensible.
- ### Abstraccion: Las funciones ocultan los detalles de implementacion.
- ### Modularidad: *Divide un problema grande en problemas más pequeños.* 
## 🚫Las tuplas tienen las siguientes desventajas: 🚫 

- ### Llamar a una funcion tiene un pequeño costo en terminos de tiempo de ejecución. 
- ### Demasiadas funciones pueden dificultad la comprension del flujo general del programa.
- ### *Si no se maneja correctamente*, las funciones pueden acceder a variables globales y modificar su estado, causando efectos secundarios inesperados.
> En resumen, las funciones son una herramienta poderosa en Python. Úsalas con moderación y de manera inteligente para aprovechar sus beneficios mientras evitas sus desventajas.
---
# Sintaxis de una Función

```python
def nombre_de_la_funcion(parametros):
    #codigo de la función
    return valor_de_retorno
```
- def: es la *palabra clave* que indica la definicion de una función.
- nombre_de_la_funcion: es el identificador *único* que usamos para llamar a la funcion.
- parametros: son variables opcionales que pasamos a la función.
- return: es la *palabra clave* que devuelve valor desde la funcion al llamador.

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
  ### Las funciones son herramientas esenciales que te permiten escribir código más modular y mantenible.
---
# Funcion Lambda
### Las funciones lambda son una forma de crear funciones anónimas en una sola línea. Son utiles cuando necesitas una funcion por corto periodo de tiempo y no queres definirla con *def*
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
## Funcion de conversion de Temperatura. (Facil)
Escribe una funcion que convierta la temperatura de Celsius a Fahrenheit y viceversa. La funcion debe aceptar dos argumentos: *el valor de la temperatura y una cadena* que indique si se está conviritendo a Celsius('C') o a Fahrenheit('F').
>Una ayuda practica ¡se necesita usar if, elif y else!
## Funcion de Calculo Factorial. (Facil)
Escribe una funcion que calcule el factorial de un numero dado.
>El factorial de un número entero positivo se define como el producto de todos los enteros positivos menores o iguales al número, Ejemplo: Factorial de 4 = 24(4 x 3 x 2 x 1)
## Funcion de Secuencia Fibonacci (Medio)
Desarrolla una funcion que genere una lista con los primeros 'n' numeros de la secuencia de Fibonacci, donde cada numero es la suma de los dos anteriores comenzando con 0 y 1.
>Ejemplo el decimo número de la secuencia es: 34
## Funcion de Verificacion de Palíndromo. (Dificil)
Cree una funcion que verifique si una palabra o frase es un palindromo(se lee igual hacia adelante que hacia atrás)

[VOLVER](readme.md)