#Crear una lista con los productos que se van a comprar.
#Agregar un nuevo producto a la lista.
#Eliminar un producto de la lista.
#Imprimir la lista

lista_de_compra= ["Legumbres secas", "choclos amarillos", "Miel" , "mermeladas", "Frutos secos", "Chocolate negro", "leche en polvo", "café", "Sal", "azúcar"]

art_agregado = input ("El articulo que necesitamos es:  ")
lista_de_compra.append(art_agregado)
print(f" Los articulos que necesitamos son: {lista_de_compra}")

art_no_comprado = input (" El nombre a eliminar es: ")
if art_no_comprado in lista_de_compra:
    lista_de_compra.remove(art_no_comprado)
else:
    print (f" Ese producto no esta en la lista, revise nuevamente su eleccion  ☹☹ {lista_de_compra}")
print(f" Los articulos que necesitamos son: {lista_de_compra}")


