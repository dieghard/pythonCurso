# Ciclo While

---

## El ciclo while en programación se utiliza para ejecutar repetidamente un bloque de código mientras una condición específica sea verdadera. Esto es especialmente útil cuando no sabés de antemano cuántas veces necesitas repetir una tarea y quieres seguir ejecutando el código hasta que se cumpla una condición de salida.

# while condicion:

# # Bloque de código a ejecutar mientras la condición sea verdadera

# Flujo de ejecución:

# La condición se evalúa antes de cada iteración del bucle.

# Si la condición es verdadera, el bloque de código dentro del while se ejecuta.

# Después de la ejecución del bloque de código, la condición se vuelve a evaluar.

# Si la condición sigue siendo verdadera, el ciclo se repite; de lo contrario, el programa continúa con la siguiente instrucción después del while.

# Ejemplo sencillo:

contador = 0
while contador < 5:
print(f"Iteración {contador}")
contador += 1

# En este ejemplo, el bloque de código dentro del while se ejecutará cinco veces, ya que contador se incrementa en cada iteración y la condición contador < 5 eventualmente se vuelve falsa.

# Uso típico:

# Procesamiento de datos mientras se cumpla cierta condición.

# Interacción con el usuario hasta que se ingrese un valor específico.

# Implementación de bucles controlados por eventos.

# Es importante tener cuidado al usar ciclos while para evitar caer en bucles infinitos. Asegúrate de que la condición se modifique en algún punto dentro del bloque de código o de lo contrario, el bucle continuará ejecutándose indefinidamente.

```
while True: # Bloque de código
clave = input("ingrese la clave para acceder:")
if clave == "1234":
print("Al fin lo conseguiste... sos un HACKER")
True
break
else:
print("clave incorrecta")
```

#Realiza el programa para la nasa que cuente regresviamente de 10 a 0 y luego muestre un mensaje de despegue
#ejemplo : 10 9 8 7 6 5 4 3 2 1 0 Despegue

## Adivina el Número:

#realizar un programa que adivine un numero con 3 intentos para adivinar el numero secreto entre 1 y 10

##SUMADORA
#Realizar un programa que permita sumar numeros hasta que se ingrese un 0

# Tabla de Multiplicar:

#Realizar un programa que muestre la tabla de multiplicar de un número ingresado por el usuario.
