## Ejercicio 1- Crear una lista de nombres y luego:
## Imprimir la longitud de la lista.
#Agregar un nuevo nombre al final de la lista.
#Eliminar el primer nombre de la lista.
#Buscar un nombre en la lista e imprimir si está o no presente.
#Ordenar la lista alfabéticamente.

lista_nombres = ["Roberto", "María",
                 "Pedro", "Juan", 
                 "José", "Gabriel", 
                 "Nicolás", "Isabel", 
                 "Héctor", "Lorenzo", 
                 "Hugo"]

print (f" La longitud de la lista es: {len (lista_nombres)}")

lista_nombres.append("Ismael")
print(lista_nombres)

nombre_borrado = input (" El nombre a eliminar es: ").capitalize()
lista_nombres.remove(nombre_borrado)
print(lista_nombres)

nombre_buscado = input (" Ingrese el nombre a encontar: ").capitalize()
if nombre_buscado in lista_nombres:
    print (" El nombre se encuentra")
else:
    print (" No se ha encontrado, no se encuentra registrado")
    
lista_nombres.sort()
print(lista_nombres)
    
