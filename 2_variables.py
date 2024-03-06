#Variables en Python
#¿QUE ES UNA VARIABLE?:En programación, una variable es un espacio en la memoria de tu computadora
# que se utiliza para almacenar información de un determinado tipo de dato.
# Las variables se identifican con un nombre único y sus valores pueden cambiar
#Pude ser un valor numerico, fecha o un texto (string).
#una vez almacenada se puede utilizar para realizar operaciones, mostrar resultados, etc.
#ejemplo:
miVariable = "Hola Mundo, muchaaaaaachos"
print (miVariable)
#la informacion de la variable se puede pisar.
miVariable = 10 * 10
print (miVariable)
#sumar el valor de dos variables
x = 10
y = 2
z = x * y
print (z)
#Concatenacion de string y variables
# print ("el valor de x es:", x)
# print ("el valor de y es:", y)
# print ("Resultado es:", z)
#NOMBRES DE VARIABLES:
# En la mayoría de lenguajes de programación existe el concepto de variables. Las variables permiten asignar nombres coherentes a información para ser reutilizada con facilidad.
# Asignaciones simples
str_color = 'Red'
num_of_cards = 56
pi_number = 13.1416
# Asignaciones múltiples
# En las siguientes asignaciones se asignan valores a varias variables a la vez.
str_red, str_blue = 'Red', 'Blue'
cards, half_cards = 56, 28

# Literales y expresiones
# Cuando se hacen asignaciones se pueden utilizar:
# Literales: son datos descritos directamente en el código.
# Es información estática, puede ser simple o usar instancias de clases.
# La definición clave es que se conoce cuál será el valor asignado analizando el código.
# Literals
a = 1
msg = 'Hello World'
total = 78 + 3.24
is_active = True

# Expresiones: son datos asignados tras la evaluación de una o varias sentencias. Suelen ser dinámicos y no se conoce el valor final analizando el código.
# Expressions
# a = arg1 + p
# msg = 'Hello' + world_msg
# position = prev_position + 89

# Keywords en Python
# En Python hay algunas palabras reservadas en que no pueden ser utilizadas como identificadores válidos. Se pueden encontrar en keyword.kwlist, y son los siguientes.

# Keywods in Python
# False    None    True    and    as    assert    async
# await    break    class    continue    def    del    elif
# else    except    finally    for    from    global    if
# import    in    is    lambda    nonlocal    not    or
# pass    raise    return    try    while   with    yield

# Nombres de variables en Python
# Según la PEP 8 (PEP 8 es una guía de estilo para Python que contiene recomendaciones para escribir código
# más legible y consistente. La guía abarca desde cómo nombrar variables hasta el número máximo de caracteres
# que debe tener una línea. )
# los nombres de las variables de Python deben de escribirse en snake_case.
# Además en deben de cumplir las siguientes características:
# Tienen que empezar por una letra o barra baja.
# El uso de keywords como nombres está prohibido.
# Los nombres deben de ser descriptivos.
# Deben de estar en minúsculas y separando palabras por barras bajas ‘_’.
# Las constantes se escriben en mayúsculas y SNAKE_CASE.
# Valid names
# cat_color = 'Brown'
# number_of_threads = 8
# phone_number = 78469334212
# ISIN_CODE = 8479362
# CONSTANT_SPEED = 9.8
# Invalid Names
# .cat
# 0number
# `car
# -hello
# POSION DE MEMORIA (en que posicion de memoria se guarda el valor de la variable)
x = 10
print(id(x))
#==================================
# # Actividades prácticas:
#==================================
# Escribir un programa que imprima un mensaje en la pantalla.
# Escribir un programa que sume dos números.
# Escribir un programa que calcule el promedio de dos notas.
# Escribir 3 variables para que guarden Apellido y nombre - Email y telefono y mostrarlos en pantalla
