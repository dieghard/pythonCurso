"""
lista_compras = ["Manzanas", "Manzanas", "Manzanas", "Manzanas", "Manzanas","Bananas", "Peras", "Pan", "Huevos"]
print(lista_compras)

while True:
    
    alimento_ingresado = input("Ingresa un alimento, para guardarlo en la lista:").capitalize()
    if alimento_ingresado == "Q":
        break
    lista_compras.append(alimento_ingresado)
    alimento_borrar = input("Ingrese un alimento para eliminar de la lista:").capitalize()
    
    if alimento_borrar in lista_compras:
        lista_compras.remove(alimento_borrar)
        print("El alimento se ha eliminado de la lista")
    else:
        print("El alimento no se encuentra en la lista")
print(lista_compras)
lista_compras.reverse()
print(f"Esta es la lista de compras invertida {lista_compras}")
lista_compras.sort()
print(f"La lista de compras ordenadas por cantidad de letras es: {lista_compras}")


print(f"El tamaño de la lista de compras es: {len(lista_compras)}")

print(f"La lista de compras tiene {lista_compras.count('Manzanas')} manzanas")

print(f"El primer indice que tiene las peras es: {lista_compras.index('Peras')}")
"""
"""
lista_numerica = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

print(f" Esta es la lista de numeros original {lista_numerica}")
numero_menor = min(lista_numerica)
print(numero_menor)
numero_mayor = max(lista_numerica)
print(numero_mayor)
suma = sum(lista_numerica)
print(suma)
numero_promedio = suma/len(lista_numerica)
print(numero_promedio)
"""
nombres_alumnos_eugenia = ["Diego", "Gaspar", "Eugenia"]
notas_alumnos_eugenia = [10, 9, 8]


NOMBRE = 0
NOTA_1 = 1
NOTA_2 = 2
NOTA_3 = 3

alumnos_eugenia = [["Diego", [10, 4, 6]], ["Gaspar", [9, 8, 7]], ["Eugenia", 8, 7, 9]]

notas_alumnos = alumnos_eugenia[1][1] 
print(f"El promedio de {alumnos_eugenia[1][0]} es {notas_alumnos} y su nota mas alta es {max(notas_alumnos)}")


