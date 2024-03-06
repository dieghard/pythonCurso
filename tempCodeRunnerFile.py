valor = int(input("Ingrese un numero: "))
valorMinimo = 0
valorMaximo = 10
rango = (valor >= valorMinimo) and (valor <= valorMaximo)

if rango:
    print(f"El valor: {valor} se encuentra entre 0 y 10")
else:
    print(f"El valor: {valor} no se encuentra entre 0 y 10")
