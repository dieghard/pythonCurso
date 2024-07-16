#pip install bcrypt
import bcrypt

# Simulación de una base de datos de usuarios
users_db = {}

# Registro de usuario
username = input("Ingrese nombre de usuario para registrar: ")
password = input("Ingrese contraseña: ")

salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode(), salt)

users_db[username] = hashed_password
print("Usuario registrado exitosamente!")

# Inicio de sesión
login_username = input("Ingrese nombre de usuario para iniciar sesión: ")
login_password = input("Ingrese contraseña: ")

if login_username in users_db:
    stored_hashed_password = users_db[login_username]
    if bcrypt.checkpw(login_password.encode(), stored_hashed_password):
        print("Inicio de sesión exitoso!")
    else:
        print("Contraseña incorrecta.")
else:
    print("El usuario no existe.")
