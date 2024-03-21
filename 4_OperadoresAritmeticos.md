# Lista de operadores Aritmeticos

- Suma = +
- Resta = -
- Multiplicacion = \_
- Division = /
- Modulo = % (Resto de la division)
- Exponenciacion = \*\*
- Division Entera = // (Solo la parte entera de la division)

```
operador_1 = 10
operador_2 = 3
suma = operador_1 + operador_2
print ("el resultado de la suma es: ", suma)
print(f"el resultado de la suma es: {suma}") #Otra manera de
```

### concatenar con la F y el resultado entre llaves. - esto se llama Interpolacion de cadenas

```
operador_1 = 10
operador_2 = 3
resta = operador_1 - operador_2
print (f"el resultado de la resta es: {resta}")
```

### Multiplicacion

```
operador_1 = 10
operador_2 = 3
multiplica = operador_1 _ operador_2
print (f"el resultado de la resta es: {multiplica}")
```

###? Division

```
operador_1 = 10
operador_2 = 3
divide = operador_1 / operador_2
print (f"el resultado de la division es: {divide}")
```

### Division sin punto flotante (solo parte entera)

```
operador_1 = 10
operador_2 = 3
divide = operador_1 // operador_2
print (f"el resultado de la division es: {divide}")
```

### Modulo = % (Resto o residuo de la division)

```
operador_1 = 10
operador_2 = 2
restodivision = operador_1 % operador_2
print (f"el resultado del resto de la division es : {restodivision}")
```

### Exponenciacion = \*\*

```
operador_1 = 10
operador_2 = 2
exponenciacion = operador_1 ** operador_2
print (f"el resultado de la exponenciacion es : {exponenciacion}")
```

### """ Nueva forma de comentar muchos renglones (tripe comillas)

# Ejercicios Propuestos

> 1-Se solicita realizar un programa para mostrar el resultado de la division de dos números enteros

> 2-Se solicita realizar un programa para calcular el residuo de la division de dos números enteros

> 3-Se solicita realizar un programa para calcular el area y el perimetro de un rectangulo, para ello

- debera crear las siguiente variables:
- Alto (int)
- Ancho (int)
  > El usuario debera proporcionar los valores de largo y ancho y despues imprimiro el resultado del area y el perimetro:
  > _Recuerde la formula Area = largo _ ancho // Perimetro = (largo + ancho) \* 2
  > se cierra con triple comilla"""

### OPERADORES DE ASIGNACION

(-) = Asignacion (el igual es el operador de asignacion)
? += Incremento
ejemplo

- miVariable = 10
- miVariable = miVariable + 1 #Incremento
  ó miVariable += 1 #Incremento

! -= Decremento

```
miVariable = miVariable - 1 #Decremento
miVariable -= 1 #Decremento
```

\_= Multiplicacion

```
miVariable = miVariable _ 2 #Multiplicacion
miVariable _= _ 2 #Multiplicacion
```

- /= Division
  miVariable = miVariable / 2 #division
  miVariable /= 2 #division
- %= Modulo
- \*\*= Exponenciacion
- //= Division Entera

## OPERADORES DE COMPARACION

### Nos permite saber si los valores son igual o distintos

# Las sentencias de control son estructuras en programación que permiten modificar el flujo de ejecución de un programa. Estas sentencias permiten tomar decisiones, ejecutar bloques de código de manera condicional o repetir ciertas operaciones mientras se cumpla una condición.

```
a = 4
b = 2
resultado = (a == b) #Igualdad
print (f"el resultado es: {resultado}")
resultado = (a != b) #Distintos
print (f"el resultado es: {resultado}")

resultado = (a > b) #Mayor que
print (f"el resultado es: {resultado}")

resultado = (a < b) #Menor que
print (f"el resultado es: {resultado}")

resultado = (a >= b) #Mayor o igual que
print (f"el resultado es: {resultado}")

resultado = (a <= b) #Menor o igual que
print (f"el resultado es: {resultado}")
```

# utlizando if

```
a = 1
b = 2
if a > b:
  print ("a es mayor que b")
else:
  print ("a no es mayor que b")
```

# Ejercicios Propuestos

> 1-Se solicita realizar un programa para mostrar su el numero ingresado es par o impar (Usando operadores logicos)
> #recuerde utilizar el % para saber si es par o impar

> 2-Se solicita realizar un programa para mostrar el resultado de la division de dos números enteros

> 3-Se solicita realizar un programa para mostrar si el numero es positivo o negativo

> 4-Se solicita realizar un programa que pida la edad de una persona y determine si es mayor o menor de edad (18)

## OPERADORES LOGICOS

- AND (y) devuelve true si ambos valores son verdaderos
- OR (o) devuelve true si al menos uno de los valores es verdadero
- NOT (no) devuelve true si el valor es falso
- XOR (o exclusivo) devuelve true si solo uno de los valores es verdadero

```
#Ejemplo de AND
a = True
b = True
resultado = (a and b)
print (f"el resultado es: {resultado}")
#Ejemplo de OR
a = True
b = False
resultado = (a or b)
print (f"el resultado es: {resultado}")
#Ejemplo de NOT
a = True
resultado = (not a)
print (f"el resultado es: {resultado}")
#Ejemplo de XOR
a = True
b = False
resultado = (a ^ b)
print (f"el resultado es: {resultado}")
#Ejemplo de NOT
a = True
resultado = (not a)
print (f"el resultado es: {resultado}")
```

# Ejercicio Propuesto

- Dado un numero determine si es se encuentra entre 0 y 10

```
valor = int(input("Ingrese un numero: "))
valorMinimo = 0
valorMaximo = 10
rango = (valor >= valorMinimo) and (valor <= valorMaximo)

if rango:
  print(f"El valor: {valor} se encuentra entre 0 y 10")
else:
  print(f"El valor: {valor} no se encuentra entre 0 y 10")
```

# Ejemplo de OR

> Crear un programa que permita saber si un padre puede ir a ver como juega su hijo dependiendo si es un dia de descanso o si esta de vacaciones (usar operadores logicos)- de lo contrario no puede ir.

> Ejemplo NOT (mismo ejercicio pero invierta el resultado)

> Crear un programa que permita al usuario ingresar su edad y determine si esta entre los 20 (de 20 a 30 años) y los 40 años(de 40 a 50 años) .

> crear un progrmaa que permita que usuario ingrese dos numeros enteeros y nos imprima cual es el mayor de los dos numeros ingresados
> (#ver DEBUGGER)

> TIENDA DE LIBROS: Crear un programa que permita ingresar un libro y su autor, muestre el precio (float) y deje escribir si el envio es gratis(true o false)

# para imprimir toda la info utilizar el print

```
print (f'''
Hola mundo, aca se puede imprimir
respetando los enter y los tabluladores.
''')
libro = input('Ingrese el nombre del libro:')
autor = input('Ingrese el nombre del autor:')
precio = float(input('Ingrese el precio:'))
envioGratis = input('¿El envio es gratis?/("SI") o ("NO")')

if envioGratis != "SI" and envioGratis != "NO":
   envioGratis="SI"
  print (f'''
  Libro : {libro}
  Auto : {autor}
  Precio : {precio}
  envio es gratis: {envioGratis}
''')
```

[VOLVER](readme.md)
