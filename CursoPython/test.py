#No suma, concatena
def calculadora(num1, num2, operacion):
    if operacion == "+":
      resultado = num1 + num2
    elif operacion == "-":
      resultado = num1 - num2
    elif operacion == "*":
      resultado = num1 * num2
    elif operacion == "/":
      resultado = num1 / num2
    elif operacion == "%":
      resultado == num1 % num2
    return resultado
num1 = input("Ingrese el primer numero:" )
num2 = input("Ingrese el segundo numero:")
operacion = input("Ingrese que tipo de operacion quieres realizar(+,-,*,/, %): ")
print(calculadora(num1, num2, operacion))


"""def calculadora_que_anda(num1, num2, operacion):
    if operacion == "+":
      resultado = num1 + num2
    elif operacion == "-":
      resultado = num1 - num2
    elif operacion == "*":
      resultado = num1 * num2
    elif operacion == "/":
      resultado = num1 / num2
    elif operacion == "%":
      resultado == num1 % num2
    return resultado
num1 = int(input("Ingrese el primer numero:" ))
num2 = int(input("Ingrese el segundo numero:"))
operacion = input("Ingrese que tipo de operacion quieres realizar(+,-,*,/, %): ")
print(calculadora_que_anda(num1, num2, operacion))"""
