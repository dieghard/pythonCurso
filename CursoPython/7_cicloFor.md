# El Ciclo For 🛂
## 🔻 Una herramienta poderosa para la repetición. 🔻
### El ciclo for es una estructura de control fundamental en la programación que permite ejecutar un bloque de código de forma repetitiva, conociendo de antemano la cantidad de veces que se desea ejecutar. Es una herramienta poderosa que facilita la escritura de código eficiente y legible, especialmente cuando se trata de tareas repetitivas.

# Un ciclo for se compone de tres partes principales:
## 1. Inicialización: Se define una variable, llamada variable de control, que se utiliza para llevar la cuenta del número de iteraciones. Se le asigna un valor inicial que marca el comienzo del ciclo.
## 2. Condición: Se establece una condición que determina si el ciclo debe continuar ejecutándose o no. La condición se evalúa al inicio de cada iteración. Si la condición es verdadera, se ejecuta el bloque de código. Si la condición es falsa, el ciclo termina.
## 3. Incremento: Se actualiza el valor de la variable de control, generalmente incrementándola en uno. Este paso se realiza al final de cada iteración, antes de volver a evaluar la condición.

# Ejemplo:

```python
#de 0 a 9
for i in range(10):
  print(i)

#en negativo  (de 10 a 0)

for i in range(10, -1, -1):
  print(i)
```
---
# La funcion range()
### La funcion range() devuelve una secuencia de numeros empezando en 0 (por defecto), incrementando 1 (por defecto) y terminando en un numero especificado, por ejemplo:

```python
for i in range(10): #Contará del 0 al 9(10 numeros), de 1 en 1 y parará en la decima iteracion.
  print(i)
```
## La sintaxis completa de la funcion es ***range(Inicio, Fin, Incremento)***, siendo la primera y la ultima opcionales.
---

# 🛑 Ventajas del ciclo for: 🛑

- ## Facilidad de uso: La sintaxis del ciclo for es simple y fácil de entender, lo que lo hace ideal para principiantes.
- ## Eficiencia: El ciclo for permite ejecutar código de forma repetitiva sin necesidad de escribir código redundante.
- ## Legibilidad: El uso de un ciclo for hace que el código sea más legible y fácil de entender.
# 💥 Aplicaciones del ciclo for: 💥
### El ciclo for se puede utilizar para una gran variedad de tareas, como:
- ## Recorrer una lista o un array.
- ## Imprimir una serie de números.
- ## Realizar cálculos repetitivos.
- ## Simular procesos que se repiten en la vida real.
- 
```python
cadena = "Hola" #arreglo de caracteres
for caracter in cadena:
    print(caracter)

cadena = "Hola" #arreglo de caracteres --- verlo con debugger
for caracter in cadena:
    print(caracter)
    if(caracter=="H"):
      print('LA HACHE DE HOLA')
else:
    print('FIN DEL PROGRAMA')
```

# Palabra BREAK 
## Dentro de los ciclos la palabra break rompe el ciclo for haciendo que no llegue al else, en este caso no imprime FIN DE PROGRAMA
```python
for letra in 'HOLANDA':
  if letra =='A':
    print(f'Letra: {letra}')
    break 
else:
  print('FIN DEL PROGRAMA')

```
# Palabra CONTINUE
### La palabra reservada continue se utiliza para omitir el resto del código dentro de un ciclo for en la iteración actual y pasar a la siguiente iteración. Es decir, cuando se encuentra la palabra continue, el ciclo for salta al siguiente valor de la variable de control y continúa con la siguiente iteración.

```python
for letra in 'ARGENTINA':
  if letra =='A':
    continue #No imprime la letra A
  print(f'Letra: {letra}')
  ```
---
# Actividades 💬

- Realizar un programa que muestre los numeros de 0 a 10.
- Realizar un programa que muestre los numeros de 10 a 0.
- Realizar un programa que muestre los numeros pares de 0 a 10.
- Realizar un programa que muestre los numeros impares de 0 a 10.
- Realizar un programa que muestre los numeros pares de 0 a 10 y luego los impares de 0 a 10.
- Realizar un programa que muestre la palabra argentina y por cada palabra muestre otra palabra ejemplo.
- Realiza un programa que imprima los numeros del 1 al 150, pero cuando el numero sea multiplo de 3, imprima: "el (NUMERO) es multiplo de 3" y cuando sea multiplo de 5, imprima: "el (NUMERO) es multiplo de 5".
- Realizar un programa que muestre la tabla de multiplicar(hasta la del 20) de un numero dado por el usuario.
  

---
[VOLVER](/readme.md)
