#Contador Regresivo:
contador = 10
while contador > 0:
    print(contador)
    contador -= 1

print("¡Despegue! 🚀👨🏻‍🚀🫂")







#Adivina el Número:

#Podemos usar:
#import random
#numero_secreto = random.randint(1, 10)
numero_secreto = 9
intentos = 0
print (f"numero_secreto: {numero_secreto}")
while True:
    intento = int(input("Adivina el número: "))

    if intento == numero_secreto:
        print(f" SUERTUDO  Lo adivinaste en {intentos + 1} intentos.")
        break
    else:
        print("Ese numero no es: Intenta nuevamente.")
        intentos += 1




#SUMADORA :
suma = 0
while True:
    numero = int(input("Ingresa un número (0 para salir): "))

    if numero == 0:
        break
    else:
        suma += numero

print(f"La suma total es: {suma}")


#Tabla de multiplicar:
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
