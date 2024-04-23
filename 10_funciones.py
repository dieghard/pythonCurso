#Conversion de temperatura
def convertir_temperatura(temperatura, unidad):
    if unidad.upper() == 'C':
        return (temperatura - 32) * 5/9
    elif unidad.upper() == 'F':
        return (temperatura * 9/5) + 32
    else:
        return "Unidad no reconocida"
print(convertir_temperatura(68, 'F'))  # Devuelve: 20.0 (Celsius)
print(convertir_temperatura(30, 'C'))  # Devuelve: 86.0 (Fahrenheit)

##Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # Devuelve: 120

#Fibonacci
def fibonacci(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]

print(fibonacci(10))  # Devuelve: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


##Palindromo
def es_palindromo(cadena):
    cadena = ''.join(c for c in cadena if c.isalnum()).lower()
    return cadena == cadena[::-1]

print(es_palindromo("Anita lava la tina"))  # Devuelve: True
print(es_palindromo("Python"))             # Devuelve: False
