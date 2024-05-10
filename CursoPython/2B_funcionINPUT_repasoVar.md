# 👨‍💻 Funcion INPUT en Python 👨‍💻
---
### La función input() en Python se usa para recibir datos del usuario mientras el programa se está ejecutando. 
- El programa le pide al usuario que ingrese algo: Cuando el programa alcanza la línea de código que contiene input(), se detiene y muestra un mensaje (si lo incluyes entre comillas dentro de los paréntesis), esperando que el usuario escriba algo.
- El usuario ingresa un valor: El usuario escribe lo que quiera y luego presiona la tecla "Enter" o "Intro".
- El programa recibe y guarda lo que el usuario escribió: Lo que el usuario escribió se guarda como una cadena de texto (o string) y el programa lo puede utilizar más adelante.

### Por ejemplo:
```python
nombre = input("Por favor, introduce tu nombre: ")
print(f"Hola, {nombre}")
#En este programa, python nos pregunta nuestro nombre con la funcion input y despues nos lo imprime por consola con la funcion print.
```

### ¡No solo se puede usar uno en nuestro codigo, podemos usar y almacenar la cantidad que necesitemos! 😲
```python
nombre = input("Por favor, introduce tu nombre: ")
apellido = input("Por favor, introduce tu apellido: ")
#Aqui lo que hará python es primero preguntarnos el nombre, al tocar Enter pasara a la siguiente linea y nos preguntará el apellido y lo guardará dentro de cada variable.
print(f"El nombre que me compartiste es {nombre} y tu apellido es {apellido}")
```
---
# Repasando variables
## ¿Te acordas que es una variable?
>En programación, una variable es un espacio en la memoria de tu computadora que se utiliza para almacenar información de un determinado tipo de dato. ¡La sintaxis de una variable es muy simple!

```python
mi_variable = "Hola Mundo"
print(f"Mi variable imprime: {mi_variable}")
```
### Recordá
Las variables pueden almacenar cualquier tipo de dato, ya sea:
- Una cadena de texto(string): ***mi_variable = "Hola Mundo"***, recordá que el texto que nuestra variable va a almacenar siempre tiene que estar entre comillas "TEXTO".
- Números enteros (Int): ***mi_variable = 150***
- Números decimales (Float): ***mi_variable = 5.5***
- Números imaginarios (Complex): ***mi_variable = 5j***
- Valores Booleanos (Boolean): ***mi_variable = True*** o ***mi_variable = False***, recordá que estos valores son Palabras claves de python y deben estar escritos con la primer letra mayuscula, sino python no entenderá que es un booleano.
### ¡Podemos usar variables en operaciones matematicas!
```python
numero1 = 140
numero2 = 20

resultado = numero1 + numero2
print(f"El resultado de sumar numero1 y numero2 es: {resultado}")
resultado = numero1 - numero2
print(f"El resultado de restar numero1 y numero2 es: {resultado}")
resultado = numero1 * numero2
print(f"El resultado de multiplicar numero1 y numero2 es: {resultado}")
resultado = numero1 / numero2
print(f"El resultado de dividir numero1 y numero2 es: {resultado}")
```
## ¿Y con cadenas de texto?
>Con cadena de texto se puede usar el simbolo ***+*** para concatenar palabras y el simbolo ***\**** nos permité multiplicar el texto.
```python
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

```
---
# Actividades 💬
### Es hora de usar el metodo input para resolver ejercicios! 
---
- ####  Escribir 3 variables para que guarden Apellido y nombre - Email y telefono y mostrarlos en pantalla, con el siguiente mensaje "Hola, Mi nombre es: ..., te paso mi contacto telefonico: ... y mi email: ..."
- #### Pedirle al usuario que ponga como estuvo su dia (del 1 al 10) y luego mostrar el texto "Mi dia estuivo de:" y el valor ingresado
- #### Pedir al usuario que ingrese su edad y su ciudad de residencia, y luego mostrar estos datos en una frase.
- #### Solicitar al usuario que ingrese su comida favorita y su bebida favorita, luego mostrar un mensaje que contenga ambas respuestas.


