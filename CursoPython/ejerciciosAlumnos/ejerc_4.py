#Sofia Dutto

#Escribir un programa que pida al usuario su nombre y lo salude por su nombre.
nombre = input("Por favor introduce tu nombre: ")
print(f"Hola, {nombre}, me alegro verte por acá")
#Escribir 3 variables para que guarden Apellido y nombre - Email y telefono y
#mostrarlos en pantalla, con el siguiente mensaje "Hola, Mi nombre es: ..., te paso
#mi contacto telefonico: ... y mi email: ..."
apellido_nombre = "Dutto María Sofía"
telefono = "2914380451"
email = "msofia.dutto@gmail.com" 
print(f"Hola, mi nombre es {apellido_nombre}, te paso mi contacto telefónico: {telefono} y mi mail: {email}")
#Pedirle al usuario que ponga como estuvo su dia (del 1 al 10) y luego mostrar el
#texto "Mi dia estuivo de:" y el valor ingresado
valoracion_dia = input ("Por favor ingrese la valoración de su día del 1 al 10, siendo 10 a pleno: ")
print(f"Mi día estuvo de: {valoracion_dia}")
#Pedir al usuario que ingrese su edad y su ciudad de residencia, y luego mostrar
#estos datos en una frase.
edad = input("Por favor ingrese su edad: ") 
residencia = input("Por favor ingrese su lugar de residencia: ")         
print(f"Tengo {edad} años y vivo en {residencia}")
#Solicitar al usuario que ingrese su comida favorita y su bebida favorita, luego
#mostrar un mensaje que contenga ambas respuestas
comida_favor = input("Por favor ingrese su comida favorita: ")
bebida_favor = input("Por favor ingrese su bebida favorita: ")
print(f"Me gusta comer {comida_favor} y tomar {bebida_favor}, yeah")


"""Correcciones
En el segundo ejercicio no uso el metodo Input
Se puede mejorar el nombre de algunas variables(último ejercicio)
"""