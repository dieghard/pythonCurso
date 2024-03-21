# Respuestas a los ejercicios de listas en Python:
# *1. Crear una lista de nombres y luego:
# Imprimir la longitud de la lista: len(lista_nombres)
# Agregar un nuevo nombre al final de la lista: lista_nombres.append("Nuevo nombre")
# Eliminar el primer nombre de la lista: lista_nombres.pop(0)
# Buscar un nombre en la lista e imprimir si está o no presente: if "Nombre buscado" in lista_nombres: print("El nombre está en la lista") else: print("El nombre no está en la lista")
# Ordenar la lista alfabéticamente: lista_nombres.sort()


#* 2. Crear una lista de números y luego:
# Calcular la suma de todos los números de la lista: suma = sum(lista_numeros)
# Encontrar el número máximo y mínimo de la lista: maximo = max(lista_numeros); minimo = min(lista_numeros)
# Multiplicar cada número de la lista por 2: lista_numeros = [numero * 2 for numero in lista_numeros]
# Imprimir los números pares de la lista: for numero in lista_numeros: if numero % 2 == 0: print(numero)

#* 3. Crear una lista de palabras y luego:
# Contar cuántas veces aparece una palabra específica en la lista: lista_palabras.count("Palabra buscada")
# Invertir el orden de la lista: lista_palabras.reverse()
# Unir dos listas en una sola: lista_conbinada = lista_1 + lista_2
# Dividir una lista en dos sublistas: sublista_1 = lista[:mitad]; sublista_2 = lista[mitad:]
#* 4-

# # Crear una lista de productos
lista_compra = ["Producto 1", "Producto 2", "Producto 3"]
# Agregar un nuevo producto a la lista
lista_compra.append("Nuevo producto")
# Eliminar un producto de la lista
lista_compra.remove("Producto a eliminar")
# Imprimir la lista de productos
for producto in lista_compra:
  print(producto)
