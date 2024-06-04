
#DICCIONARIOS
# Un diccionario es una estructura de datos que permite almacenar pares de clave-valor. En este caso, las claves son 'Alice', 'Bob' y 'Charlie', y los valores son 25, 30 y 35, respectivamente. Esto podría interpretarse como que Alice tiene 25 años, Bob tiene 30 años y Charlie tiene 35 años.
#recorrer Diccionarios
edades = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
# Podes acceder a los valores de un diccionario utilizando sus claves. Por ejemplo, edades['Alice'] devolvería 25.
for nombre in edades:
    print(nombre)
    print(edades[nombre])
#otro ejemplo con diccionarios
#Iterar a través de un diccionario: Puedes iterar a través de las claves y valores de un diccionario al mismo tiempo usando el método items().

personas = {
    'Alice': {'edad': 25, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'},
    'Bob': {'edad': 30, 'ciudad': 'Barcelona', 'ocupacion': 'Doctor'},
    'Charlie': {'edad': 35, 'ciudad': 'Valencia', 'ocupacion': 'Profesor'}
}

for nombre, detalles in personas.items():
    print(f'{nombre} vive en {detalles["ciudad"]}.')


for nombre, datos in personas.items():
    print(nombre)
    print('Edad:', datos['edad'])
    print('Ciudad:', datos['ciudad'])
    print('Ocupación:', datos['ocupacion'])
    print()

## CARGAR UN DICCIONARIO
personas = {}
for i in range(3):
    nombre = input('Introduce el nombre de la persona: ')
    edad = int(input('Introduce la edad de la persona: '))
    ciudad = input('Introduce la ciudad de la persona: ')
    ocupacion = input('Introduce la ocupación de la persona: ')
    personas[nombre] = {'edad': edad, 'ciudad': ciudad, 'ocupacion': ocupacion}
print(personas)


# Comprobar si un diccionario está vacío: Puedes comprobar
# si un diccionario está vacío simplemente comparándolo con un
# diccionario vacío {} o comprobando su longitud con len().
if personas == {}:
    print('El diccionario está vacío.')
if len(personas) == 0:
    print('El diccionario está vacío.')

#Eliminando un item del diccionario :
personas = {
    'Alice': {'edad': 25, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'},
    'Bob': {'edad': 30, 'ciudad': 'Barcelona', 'ocupacion': 'Doctor'},
    'Charlie': {'edad': 35, 'ciudad': 'Valencia', 'ocupacion': 'Profesor'}
}
# Para eliminar a Bob del diccionario, puedes hacer lo siguiente:
del personas['Bob']
print(personas)
#Otra manera
bob = personas.pop('Bob')  # Elimina 'Bob' del diccionario y devuelve su valor

#Eliminar todos los items
# Supongamos que este es tu diccionario
personas = {
    'Alice': {'edad': 25, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'},
    'Bob': {'edad': 30, 'ciudad': 'Barcelona', 'ocupacion': 'Doctor'},
    'Charlie': {'edad': 35, 'ciudad': 'Valencia', 'ocupacion': 'Profesor'}
}
# Para eliminar todos los elementos del diccionario, puedes hacer lo siguiente:
personas.clear()
print(personas)  # Esto imprimirá un diccionario vacío: {}

#Buscar dentro de un diccionario : # Supongamos que este es tu diccionario
personas = {
    'Alice': {'edad': 25, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'},
    'Bob': {'edad': 30, 'ciudad': 'Barcelona', 'ocupacion': 'Doctor'},
    'Charlie': {'edad': 35, 'ciudad': 'Valencia', 'ocupacion': 'Profesor'}
}

# Para verificar si 'Alice' está en el diccionario, puedes hacer lo siguiente:
if 'Alice' in personas:
    print('Alice está en el diccionario.')
else:
    print('Alice no está en el diccionario.')

#Buscar un item en particular

# Supongamos que este es tu diccionario
personas = {
    'Alice': {'edad': 25, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'},
    'Bob': {'edad': 30, 'ciudad': 'Barcelona', 'ocupacion': 'Doctor'},
    'Charlie': {'edad': 35, 'ciudad': 'Valencia', 'ocupacion': 'Profesor'}
}

# Para verificar si 'Madrid' es la ciudad de alguna persona, puedes hacer lo siguiente:
for nombre, datos in personas.items():
    if datos['ciudad'] == 'Madrid':
        print(f'{nombre} vive en Madrid.')

# ORDENAR DICCIONARIOS!!!!!!

edades = {'Alice': 25, 'Bob': 30, 'Charlie': 35}

edades_ordenadas = dict(sorted(edades.items()))

print(edades_ordenadas)  # Imprime: {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# Combinar diccionarios: Puedes combinar dos diccionarios usando el método update().
personas['David'] = {'edad': 40, 'ciudad': 'Sevilla', 'ocupacion': 'Abogado'}

otros = {'Eva': {'edad': 28, 'ciudad': 'Bilbao', 'ocupacion': 'Diseñadora'}}
personas.update(otros)


#Obtener todas las claves o valores: Puedes obtener una lista de todas las claves o valores de un diccionario usando los métodos keys() y values(), respectivamente.
nombres = personas.keys()
detalles = personas.values()

#Obtener el valor de una clave: Puedes obtener el valor de una clave usando el método get(). Este método también te permite especificar un valor predeterminado en caso de que la clave no exista en el diccionario.
ciudad = personas.get('Alice', {}).get('ciudad', 'Desconocida')

#Copiar un diccionario: Puedes hacer una copia de un diccionario usando el método copy().
# Esto es útil si quieres trabajar con el diccionario pero no quieres modificar el original.
copia_personas = personas.copy()

#Crear un diccionario a partir de claves y valores existentes: Puedes usar la función zip() para crear un diccionario a partir de dos listas: una para las claves y otra para los valores
nombres = ['Alice', 'Bob', 'Charlie']
edades = [25, 30, 35]
personas = dict(zip(nombres, edades))
#Crear un diccionario con las mismas claves y valores por defecto: Puedes usar el método fromkeys() para crear un nuevo diccionario con las claves de una lista y un valor por defecto para todas ellas.
nombres = ['Alice', 'Bob', 'Charlie']
personas = dict.fromkeys(nombres, {'edad': 0, 'ciudad': '', 'ocupacion': ''})

#Filtrado de datos
#Esto se hace generalmente utilizando una comprensión de diccionario, que es una forma concisa de crear un nuevo diccionario a partir de un diccionario existente.
personas = {
    'Alice': {'edad': 25, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'},
    'Bob': {'edad': 30, 'ciudad': 'Barcelona', 'ocupacion': 'Doctor'},
    'Charlie': {'edad': 35, 'ciudad': 'Valencia', 'ocupacion': 'Profesor'}
}

personas_madrid = {nombre: detalles for nombre, detalles in personas.items() if detalles['ciudad'] == 'Madrid'}

print(personas_madrid)  # Imprime: {'Alice': {'edad': 25, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'}}

#Para guardar el diccionario en un archivo:
import json
personas = {
    'Alice': {'edad': 25, 'ciudad': 'Madrid', 'ocupacion': 'Ingeniera'},
    'Bob': {'edad': 30, 'ciudad': 'Barcelona', 'ocupacion': 'Doctor'},
    'Charlie': {'edad': 35, 'ciudad': 'Valencia', 'ocupacion': 'Profesor'}
}

# Guardar el diccionario en un archivo
with open('personas.json', 'w') as f:
    json.dump(personas, f)

#Para recuperar el diccionario desde un archivo:
import json

# Recuperar el diccionario desde un archivo
with open('personas.json', 'r') as f:
    personas = json.load(f)

print(personas)  # Imprime el diccionario recuperado

