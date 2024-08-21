#Objetivo: Implementar una clase CuentaBancaria 
#que permita a los usuarios realizar operaciones bancarias básicas 
#como depositar, retirar y consultar el saldo.
import funciones as fp
class CuentaBancaria:
    def __init__(self,saldo:int | None = 0 , titular:str | None = "") -> None:
        self.saldo = saldo
        self.titular = titular
        pass
    def mostrar_saldo(self):
        print("\n"*2)
        print(f"{self.titular} su saldo actual es {self.saldo}")
        return
    def depositar(self):
        print("\n"*2)
        deposito = fp.ingresar_numero("Ingrese el valor a depositar: ")
        if deposito > 0: 
            self.saldo = self.saldo + deposito
            print("Operación realizada con exito")
            self.mostrar_saldo()
            return self.saldo
    def retirar(self):
        print("\n"*2)
        retiro = fp.ingresar_numero("Ingrese el valor a retirar: ")
        if self.saldo >= retiro and retiro > 0: 
            self.saldo = self.saldo - retiro
            print("Operación realizada con exito")
            self.mostrar_saldo()
            return self.saldo
        else:
            print("\n"*2)
            print("Saldo Insuficiente. Ingrese Más Dinero")
            self.mostrar_saldo()
   
   
   
   
            
titular = input("Ingrese el nombre del titular:")
cuenta_bancaria = CuentaBancaria(0,titular)
while True:
    opcion = input("Elije la opcion que quieres realizar:\n-Depositar (D) \n-Retirar(R)\n-Mostrar Saldo (S)\n-Si quieres finalizar sesion (F) \n-Opcion:").upper()
    if opcion == "D" or opcion == "R" or opcion == "S" or opcion == "F":
        if opcion == "D":
            cuenta_bancaria.depositar()
        if opcion == "R":
            cuenta_bancaria.retirar()
        if opcion == "S":
            cuenta_bancaria.mostrar_saldo()
        if opcion == "F":
            cuenta_bancaria.mostrar_saldo()
            exit("Finalizando Sesion con Exito")
    else:
        print("Ingresaste una opcion incorrecta (D,R,S,F)")
        print("\n"*10)
            
    