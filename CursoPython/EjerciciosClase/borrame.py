desplazamiento = 3

# Solicitar al usuario que ingrese su nombre de usuario y contraseña
username = "Diego"
password = "Diego123"

# Cifrado de la contraseña
password_cifrada = ""
for caracter in password:
    if caracter.isalpha():  # Verificamos si el carácter es una letra
        letra_base = ord('a') if caracter.islower() else ord('A')  # Determinamos la base (a o A)
        # Calculamos el nuevo carácter desplazado y lo agregamos al mensaje cifrado
        caracterORD = ord(caracter)
        caracterCHR = chr(caracter)
        caracter_cifrado = chr((ord(caracter) - letra_base + desplazamiento) % 26 + letra_base)
        password_cifrada += caracter_cifrado
    else:
        password_cifrada += caracter  # Si no es letra, lo dejamos igual

print(password_cifrada)
nueva= .join(",",password_cifrada)