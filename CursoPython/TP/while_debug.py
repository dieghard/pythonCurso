
contador = 0
seguir = True

while seguir:
    contador +=1
    valor_usuario = input("Ingrese un valor o la letra A para finalizar la ejecucion del programa: ")
    valor_usuario = valor_usuario.upper()
    if valor_usuario == "A":
        seguir = False 


print(f"El programa se ejecuto correctamente {contador} veces!")
