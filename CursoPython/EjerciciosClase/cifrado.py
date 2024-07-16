# Definimos la clave de cifrado (desplazamiento)
desplazamiento = 3

# Solicitar al usuario que ingrese su nombre de usuario y contraseña
username = input("Ingrese nombre de usuario para registrar: ")
password = input("Ingrese contraseña: ")

# Cifrado de la contraseña
password_cifrada = ""
for caracter in password:
    if caracter.isalpha():  # Verificamos si el carácter es una letra
        letra_base = ord('a') if caracter.islower() else ord('A')  # Determinamos la base (a o A)
        # Calculamos el nuevo carácter desplazado y lo agregamos al mensaje cifrado
        caracter_cifrado = chr((ord(caracter) - letra_base + desplazamiento) % 26 + letra_base)
        password_cifrada += caracter_cifrado
    else:
        password_cifrada += caracter  # Si no es letra, lo dejamos igual

# Simulación de una base de datos de usuarios
users_db = {}
users_db[username] = password_cifrada
print("Usuario registrado exitosamente!")

# Solicitar al usuario que ingrese su nombre de usuario y contraseña para iniciar sesión
login_username = input("Ingrese nombre de usuario para iniciar sesión: ")
login_password = input("Ingrese contraseña: ")

# Cifrar la contraseña ingresada para comparar
login_password_cifrada = ""
for caracter in login_password:
    if caracter.isalpha():  # Verificamos si el carácter es una letra
        letra_base = ord('a') if caracter.islower() else ord('A')  # Determinamos la base (a o A)
        # Calculamos el nuevo carácter desplazado y lo agregamos al mensaje cifrado
        caracter_cifrado = chr((ord(caracter) - letra_base + desplazamiento) % 26 + letra_base)
        login_password_cifrada += caracter_cifrado
    else:
        login_password_cifrada += caracter  # Si no es letra, lo dejamos igual

# Verificar las credenciales
if login_username in users_db:
    stored_password_cifrada = users_db[login_username]
    if login_password_cifrada == stored_password_cifrada:
        print("Inicio de sesión exitoso!")
    else:
        print("Contraseña incorrecta.")
else:
    print("El usuario no existe.")
