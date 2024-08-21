lista_1 = ["Hola", "Chau", "Nos vemos"]

lista_2 = lista_1

lista_1.append("Mundo")

print(len(lista_2))
print(lista_2)

lista_2.append("Los vemo")
print(lista_1)
print(id(lista_1))
print(id(lista_2))

