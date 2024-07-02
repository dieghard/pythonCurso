# Ejercicio 1- Crear una lista de nombres y luego:
# Imprimir la longitud de la lista.
# Agregar un nuevo nombre al final de la lista.
# Eliminar el primer nombre de la lista.
# Buscar un nombre en la lista e imprimir si está o no presente.
# Ordenar la lista alfabéticamente

lista_nombre = ['Juan', 'Pedro', 'Maria', 'Roberto', 'Ana', 'Nicolás']
print("listado de nombres")
print(lista_nombre) # salida = ['Juan', 'Pedro', 'Maria', 'Roberto', 'Ana', 'Nicolás']
print("\n")

# Imprimir la longitud de la lista.
print("longitud de la lista")
print(len(lista_nombre)) # salida = 6
print("\n")

# Agregar un nuevo nombre al final de la lista.
nombre_a_agregar = input('Ingrese un nombre: ')
lista_nombre.append(nombre_a_agregar) # si ponemos Diego
print("Lista de nombres con  el nuevo nombre")
print(lista_nombre) # salida = ['Juan', 'Pedro', 'Maria', 'Roberto', 'Ana', 'Nicolás', 'Diego']
print("\n")


# Eliminar el primer nombre de la lista.
lista_nombre.pop(0)
print("Lista de nombres sin el primer nombre")
print(lista_nombre) # salida = ['Pedro', 'Maria', 'Roberto', 'Ana', 'Nicolás', 'Diego']
print("\n")

# Buscar un nombre en la lista e imprimir si está o no presente.
nombre_a_buscar = input('Ingrese un nombre: ')
if nombre_a_buscar in lista_nombre:
    print(f'El nombre {nombre_a_buscar} está en la lista')
else:
    print(f'El nombre {nombre_a_buscar} no está en la lista')

print("\n")

# Ordenar la lista alfabéticamente
lista_nombre.sort()
print("Lista de nombres ordenada alfabéticamente")
print(lista_nombre) # salida = ['Ana', 'Diego', 'Juan', 'Maria', 'Nicolás', 'Pedro', 'Roberto']
print("\n")