#Calcular la suma de todos los números de la lista.
#Encontrar el número máximo y mínimo de la lista.
#Multiplicar cada número de la lista por 2.
#Imprimir los números pares de la lista.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                  19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
suma_numeros = sum(lista_numeros)
print (f" El valor de la suma de la lista es: {suma_numeros} ")

num_maximo = max(lista_numeros)
num_minimo = min(lista_numeros)
print (f" El numero maximo es: {num_maximo} y el numero minimo es: {num_minimo}")

for num in lista_numeros: #tuve que subirlo y no respetar el orden de pedido porque me seleccionaba los multiplos de 2 de la lista que multiplico x 2
    if  num % 2 == 0:
        print (num)
        

lista_numeros = [ numero * 2 for numero in lista_numeros]
print (f" Los numeros multiplicados son: {lista_numeros}")
