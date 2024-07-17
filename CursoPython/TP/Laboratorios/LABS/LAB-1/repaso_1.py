VARIABLE = "Hola"

constante = "Chau"

Lista = ["Hola", "chau", constante, "Hola"]
Lista.remove("Hola")
#print(Lista)
Lista = ["Hola", "chau", constante]
elemento_eliminado = Lista.pop()
#print(f"Este es el elemento eliminado {elemento_eliminado}")
#print(Lista.pop())

tuplas = ("Hola", "chau", constante)
conjuntos = {"Hola", "chau", constante}
diccionario = {"Clave":"Valor", "Diego": 27, "Guillermo": 29,  "Paula": 17}
lista_nombre_edad = [["Gaspar", 23],["Diego", 27]]

#print(lista_nombre_edad[0][1])
#print(diccionario["Gaspar"])
print("Esto imprime el for:")
for i in range(10):
    print(i)
    if i == 5:
       break

print("Esto imprime el while:")
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 6:
        break
