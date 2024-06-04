# El ciclo for: Una herramienta poderosa para la repetición
# El ciclo for es una estructura de control fundamental en la programación que permite ejecutar un bloque de código de forma repetitiva, conociendo de antemano la cantidad de veces que se desea ejecutar. Es una herramienta poderosa que facilita la escritura de código eficiente y legible, especialmente cuando se trata de tareas repetitivas.

# Un ciclo for se compone de tres partes principales:

# 1. Inicialización: Se define una variable, llamada variable de control, que se utiliza para llevar la cuenta del número de iteraciones. Se le asigna un valor inicial que marca el comienzo del ciclo.

# 2. Condición: Se establece una condición que determina si el ciclo debe continuar ejecutándose o no. La condición se evalúa al inicio de cada iteración. Si la condición es verdadera, se ejecuta el bloque de código. Si la condición es falsa, el ciclo termina.

# 3. Incremento: Se actualiza el valor de la variable de control, generalmente incrementándola en uno. Este paso se realiza al final de cada iteración, antes de volver a evaluar la condición.

# Ejemplo:

# Python
#de 0 a 9
for i in range(10):
  print(i)

#en negativo  (de 10 a 0)

for i in range(10, -1, -1):
  print(i)

# En este ejemplo, el ciclo for se ejecuta 5 veces. La variable de control i se inicializa en 0 y se incrementa en 1 en cada iteración. El bloque de código dentro del ciclo se ejecuta 5 veces, imprimiendo los valores de i desde 0 hasta 4.

# Ventajas del ciclo for:

# Facilidad de uso: La sintaxis del ciclo for es simple y fácil de entender, lo que lo hace ideal para principiantes.
# Eficiencia: El ciclo for permite ejecutar código de forma repetitiva sin necesidad de escribir código redundante.
# Legibilidad: El uso de un ciclo for hace que el código sea más legible y fácil de entender.
# Aplicaciones del ciclo for:

# El ciclo for se puede utilizar para una gran variedad de tareas, como:

# Recorrer una lista o un array.
# Imprimir una serie de números.
# Realizar cálculos repetitivos.
# Simular procesos que se repiten en la vida real.

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

#PALABRA break DENTRO DE LOS CICLOS

for letra in 'HOLANDA':
  if letra =='A':
    print(f'Letra: {letra}')
    break #No llega al else se rompe el ciclo for y no imprime FIN DE PROGRAMA
else:
  print('FIN DEL PROGRAMA')



#  #PRACTICAS
  #1- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS DE 0 A 10
  #2- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS DE 10 A 0
  #3- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS PARES DE 0 A 10
  #4- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS IMPARES DE 0 A 10
  #5- REALIZAR UN PROGRAMA QUE MUESTRE LOS NUMEROS PARES DE 0 A 10 Y LUEGO LOS IMPARES DE 0 A 10
  #6- REALIZAR UN PROGRAMA QUE MUESTRE LA PALABRA ARGENTINA Y POR CADA PALABRA MUESTRE OTRA PALABRA EJEMPLO
  # A rgentina
  # R enacer
  # G loriosa
  # E moción
  # N ación
  # T alento
  # I lusión
  # N ueve
  # A lbiceleste

# PALABRA CONTINUE
# La palabra reservada continue se utiliza para omitir el resto del código dentro de un ciclo for en la iteración actual y pasar a la siguiente iteración. Es decir, cuando se encuentra la palabra continue, el ciclo for salta al siguiente valor de la variable de control y continúa con la siguiente iteración.
#ejemplo :
for letra in 'ARGENTINA':
  if letra =='A':
    continue #No imprime la letra A
  print(f'Letra: {letra}')