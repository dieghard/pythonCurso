"""
    lista_compras = ["Manzanas", "Peras", "Bananas", "Peras", "Bananas", "Peras", "Bananas", "Peras" ]

    while True:
        producto_buscar = input("Ingrese el producto a buscar: ").capitalize()
        if producto_buscar == "Q":
            break
        if producto_buscar in lista_compras:
            print(f"Las {producto_buscar} están en la lista")
            lista_compras.remove(producto_buscar)
            print(lista_compras)
        else:
            print("No estan")
            lista_compras.append(producto_buscar)
            print(lista_compras)

    print("Gracias por usar el programa")

    lista_compras.sort(key=len)
    print(f"Esta es la lista de compras ordenadas por longitud {lista_compras}")

    lista_compras.sort()
    print(f"Esta es la lista de compras ordenadas por abecedario A-Z {lista_compras}")

    lista_compras.sort(reverse=True)
    print(f"Esta es la lista de compras ordenadas por abecedario Z-A {lista_compras}")

    longitud_lista_compras = len(lista_compras)
    print(f"La longitud de la lista de compras es {longitud_lista_compras}")
  
    fruta_buscar = input("Ingrese la fruta a buscar:").capitalize()
    cantidad_fruta = lista_compras.count(fruta_buscar)
    print(f"La cantidad de {fruta_buscar} en la lista es {cantidad_fruta}")
 
    fruta_buscar = input("Ingrese la fruta a buscar por indice:").capitalize()
    indice_fruta = lista_compras.index(fruta_buscar)
    print(f"La cantidad de {fruta_buscar} en la lista es {indice_fruta}")

NOMBRES = 0
EDADES = 1
GENERO = 2
CIUDAD = 3
ESTUDIO = 4

nombres_edades = [["Gaspar",23], ["Diego", 44], ["Fermin", 14, "Hombre", "General Levalle", "Estudiante"], ["Carlos", 48], ["Paula", 45], ["Monica",44]]

print(nombres_edades[3][EDADES])
print(nombres_edades[3][NOMBRES])

edades = [23, 44, 14, 48, 10]

suma_edades = sum(edades)
print(suma_edades)

maxima_edad = max(edades)
print(maxima_edad)

minima_edad = min(edades)
print(minima_edad)
"""