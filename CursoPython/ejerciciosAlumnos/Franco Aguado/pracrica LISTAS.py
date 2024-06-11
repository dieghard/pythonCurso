#Crea un programa que genere una lista de 30 números aleatorios entre 1 y 100. y que pueda modificar el rango de números aleatorios editando los valores de minimo y maximo
#Que el usuario pueda poner la cantidad de datos aleatorios que necesta en la lista.
import random

minimo = 1
maximo = 99
cant_numeros = "a"
contador = 0
error_numero = "Tenes que poner un valor numerico!"
ingrese_valor = "Ingrese la cantidad de datos aleatorios que desea tener en la lista : "
ingrese_valor_borrar = "Ingrese el numero que desea borrar de la lista : "
while not cant_numeros.isdigit():
    cant_numeros = input(ingrese_valor)
    print(error_numero)
cant_numeros = int(cant_numeros)
lista_aleatorios = [] #declaramos la lista donde van a ir los numeros aleatorios

while not contador == cant_numeros :
    num_aleatorios= random.randint(minimo,maximo)
    contador += 1
    lista_aleatorios.append(num_aleatorios) #agrega los datos random uno a uno a la lista declarada
print(lista_aleatorios)

#Ordenamos los valores de menor a mayor
lista_aleatorios.sort()
print(lista_aleatorios)

#Ordenar de menor a mayor
lista_aleatorios.sort(reverse=True)
print(lista_aleatorios)

#Quitar elementos y darme la cantidad de elementos de la lista
elemento_borrar = input(ingrese_valor_borrar)
while not elemento_borrar.isdigit():
    print(error_numero)
    elemento_borrar = input(ingrese_valor_borrar)
elemento_borrar = int(elemento_borrar)
if elemento_borrar in lista_aleatorios:
    #lista_aleatorios.remove(elemento_borrar) ######ACAAAAAAAAAAAAAAAAAAAAA!!!!!!!!!!!!!!!
    del lista_aleatorios[elemento_borrar]
    print("El numero se ah eliminado de la lista")
else:
    print("El numero no se encuentra en la lista")

print(lista_aleatorios)
print(f"L cantidad de datos en la lists es de {len(lista_aleatorios)}")

#Calcular el promedio
promedio = sum(lista_aleatorios)/len(lista_aleatorios)
print(f"El promedio es {promedio}")