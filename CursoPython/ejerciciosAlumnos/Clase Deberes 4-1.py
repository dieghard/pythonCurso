#Brisa Daga
Nombre = input("Ingrese su nombre, por favor")
print(f"Hola {Nombre} que gusto conocerte")

Nom_Ap=input("Ingrese su nombre y apellido, por favor: ")
Email=input("Ingrese su email, gracias😉 ")
Telefono=input("Puede ingresar su telefono, muy amable ")
print(f"Hola mi nombre es {Nom_Ap}, te pase mi contacto telefonico {Telefono} y mi email {Email}")

Día=input("¿Como estuvo tu día deñ 1-10?")
print(f"Mi día estuvo {Día}")

ED=input("¿Me quieres contar cuantos años tienes?")
Vive=input("¿Donde vives? ")
print(f"Vivo en {Vive} y tengo {ED}")

Com=input("¿Cual es tu comida favorita? ")
Beb=input("¿Cual es tu bebida favorita ")
print(f"Coincido con vos en que {Com}, es lo mejor y tienen buen gusto al elegir {Beb} como favorito")

"""Correcciones:
El nombre de las variables no utiliza buenas practicas:
 -Nombre deberia ser nombre. (La mayuscula al principio se repite en todas)
 -Nom_Ap, Com ,Beb  deberia ser apellido, comida_favorita, bebida_favorita.
La variable de edad en el cuarto ejercicio no utiliza buenas practicas y al colocarla en mayuscula para Python es una constante ED, deberia ser edad o ed.
El resto esta perfecto!
"""