cuit = input("Ingrese su CUIT para saber si es valido:")
# Validaciones mínimas
if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
    print("CUIT inválido")
else:
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    cuit_sin_guiones = cuit.replace("-", "")  # Remuevo los guiones

    # Calculo el dígito verificador
    aux = 0
    for i in range(10):
        aux += int(cuit_sin_guiones[i]) * base[i]

    aux = 11 - (aux % 11)

    if aux == 11:
        aux = 0
    elif aux == 10:
        aux = 9

    if aux == int(cuit_sin_guiones[10]):
        print("CUIT válido")
    else:
        print("CUIT inválido")