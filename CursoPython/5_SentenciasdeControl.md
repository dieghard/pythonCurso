# Sentencias De Control 🤯

### Repasando : Las sentencias de control son estructuras en programación que permiten modificar el flujo de ejecución de un programa. Estas sentencias permiten tomar decisiones, ejecutar bloques de código de manera condicional o repetir ciertas operaciones mientras se cumpla una condición. En Python, las principales sentencias de control son if, else, elif y while:

- ## if:

> La sentencia if se utiliza para ejecutar un bloque de código si una condición es verdadera. Si la condición es falsa, el bloque no se ejecuta.

```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")
```

- ## if-else:

  > Uso: Se utiliza para tomar decisiones en el código, ejecutando un bloque de código si una condición es verdadera, y otro bloque si la condición es falsa.
  > Ejemplo: Puedes usarlo para verificar si un usuario tiene la edad suficiente para acceder a ciertas funciones de tu programa.

- otro ejemplo :

```python
edad = 15
if edad >= 18:
print("Eres mayor de edad.")
else:
print("Eres menor de edad.")
```

- ## _elif_:

> Uso: Se utiliza para evaluar múltiples condiciones en orden. Si la condición del if es falsa, se verifica la siguiente condición en elif.
> Ejemplo: Puedes usarlo para asignar una calificación a un estudiante basándote en su puntuación.

```python
nota = 75
if nota >= 90:
  print("Excelente")
elif 80 <= nota < 90:
  print("Buen trabajo")
else:
  print("Necesitas mejorar")
```

> crear un programa que pase de numeros a texto : 1 = Uno, 2 = Dos, 3 = Tres

```python
numero = int(input("Escribe un numero entre 1 y 3: "))
if numero ==1:
  numeroTexto = "Uno"
elif numero ==2:
  numeroTexto = "Dos"
elif numero ==3:
  numeroTexto = "Tres"
else:
  numeroTexto = "No reconocido"

print(f"Tu numero es: {numero} en texto es: {numeroTexto}")
```

- ## _!IF ELSE_

```python
condicion = "ddd"
if condicion :
  print("La condicion es verdadera")
else :
  print("La condicion es falsa")

if condicion == True :
  print("La condicion es verdadera")
elif condicion == False:
  print("La condicion es falsa")
else :
  print("La condicion No reconocida!😮")
```

## Simplificacion de Else IF en una sola sentencia

### Se puede simplificar la estructura de un if else if else en una sola sentencia utilizando el operador ternario

### Ejemplo:

```python
condicion = True
if condicion :
  print("La condicion es verdadera")
else :
  print("La condicion es falsa")

print('condicion verdadera') if condicion else print('condicion falsa') #operacion ternaria
```

## ⚠Solo si el codigo es chico se recomienda el operador ternario.

Otro ejemplo :

```python
numero = int(input("Ingresa un número: "))
resultado = "Par" if numero % 2 == 0 else "Impar"
print(f"El número {numero} es {resultado}.")
# Otro ejemplo :
edad = int(input("Ingresa tu edad: "))
grupo = "Adulto" if edad >= 18 else "Menor de edad"
print(f"Tú eres {grupo}.")
```

---

# Actividades 💬

## CREAR UN PROGRAMA QUE PERMITE Calificación de estudiantes, el programa debera pedir la materia y la nota y mostrar la calificación correspondiente >= 9 excelente , >= 7 Aprobado , >= 5 regular, < 5 insuficiente -

## Realice un programa funciona como una calculadora básica que permite al usuario realizar operaciones simples.

- el programa debera pedir el numero 1 , el operador y el numero 2 y realizar la operacion correspondiente
- el programa debera mostrar el resultado de la operacion
- el programa debera mostrar un mensaje de error si el operador no es valido

## Realice un programa que ingrese el numero del mes (del 1 al 12 y muestre la estacion correspondiente)

```python
mes = int(input("Ingresa el número del mes (1-12): "))

if 1 <= mes <= 12:
   if 3 <= mes <= 5:
     estacion = "Primavera"
   elif 6 <= mes <= 8:
     estacion = "Verano"
   elif 9 <= mes <= 11:
     estacion = "Otoño"
  else:
     estacion = "Invierno"

  print(f"El mes {mes} corresponde a la estación del año: {estacion}")
 else:
   print("Número de mes no válido. Ingresa un número del 1 al 12.")
```

---

[VOLVER](/readme.md)
