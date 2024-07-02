# Ejercicio 3. Crear una lista de palabras y luego:
# Contar cuántas veces aparece una palabra específica en la lista.
# Invertir el orden de la lista.
# Dividir una lista en dos sublistas.
# Unir dos listas en una sola.

lista_palabras = ["perro", "pan", "bicicleta", "chocolate", "armadura", "examen", "chocolate"]
print(f"El listado de palabras es: {lista_palabras}") # salida = El listado de palabras es: ['perro', 'pan', 'bicicleta', 'chocolate', 'armadura', 'examen', 'chocolate']
print("\n")

# Contar cuántas veces aparece "chocolate" en la lista.
print(f"El número de veces que aparece 'chocolate' en la lista es: {lista_palabras.count('chocolate')}") # salida = El número de veces que aparece 'chocolate' en la lista es: 2
print("\n")

# Invertir el orden de la lista.
lista_palabras.reverse()
print(f"La lista invertida es: {lista_palabras}") # salida = La lista invertida es: ['chocolate', 'examen', 'armadura', 'chocolate', 'bicicleta', 'pan', 'perro']
print("\n")

# Dividir una lista en dos sublistas.
sublista1 = lista_palabras[0:2]
sublista2 = lista_palabras[2:5]

print(f"La primer sublistas es: {sublista1} y la segunda es: {sublista2}") # salida = La primer sublistas es: ['chocolate', 'examen'] y la segunda es: ['armadura', 'chocolate', 'bicicleta']
print("\n")

# Unir dos listas en una sola.
print(f"La lista unida es: {sublista2 + sublista1}") # salida = La lista unida es: La lista unida es: ['armadura', 'chocolate', 'bicicleta', 'chocolate', 'examen']
print("\n")