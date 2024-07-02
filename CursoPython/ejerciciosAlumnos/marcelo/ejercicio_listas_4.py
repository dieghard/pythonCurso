# Ejercicio 4. Simular una cesta de la compra:
# Crear una lista con los productos que se van a comprar.
# Agregar un nuevo producto a la lista.
# Eliminar un producto de la lista.
# Imprimir la lista

listado_de_compras = ["tomates", "harina", "aceite", "leche", "pan", "sal", "cebolla", "queso", "vinagre"]
print(f"La lista de productos a comprar es: {listado_de_compras}") # salida = La lista de productos a comprar es: ['tomates', 'harina', 'aceite', 'leche', 'pan', 'sal', 'cebolla', 'queso', 'vinagre']
print("\n")

# Agregar un nuevo producto a la lista.
listado_de_compras.append("galetitas")
print(f"La nueva lista de productos a comprar es: {listado_de_compras}") # salida = La nueva lista de productos a comprar es: ['tomates', 'harina', 'aceite', 'leche', 'pan', 'sal', 'cebolla', 'queso', 'vinagre', 'galetitas']
print("\n")

# Eliminar un producto de la lista.
listado_de_compras.remove("aceite")
print(f"La lista de productos a comprar con producto eliminado es: {listado_de_compras}") # salida = La lista de productos a comprar con producto eliminado es: ['tomates', 'harina', 'leche', 'pan', 'sal', 'cebolla', 'queso', 'vinagre', 'galetitas']
print("\n")

# Imprimir la lista.
print(f"La lista de productos a comprar es: {listado_de_compras}") # salida = La lista de productos a comprar es: ['tomates', 'harina', 'leche', 'pan', 'sal', 'cebolla', 'queso', 'vinagre', 'galetitas']