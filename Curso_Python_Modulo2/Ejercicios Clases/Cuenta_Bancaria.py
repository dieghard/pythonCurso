#Implementar una clase CuentaBancaria 
#Permita a los usuarios realizar operaciones bancarias básicas como:
#depositar, retirar y consultar el saldo.

import funciones as f 
import funciones_mias as fm

class CuentaBancaria:
    def __init__(self):
        titular = input("Ingrese su nombre para que podamos ingresar a su CUNTA: ")
        saldo = f.ingresar_numero("Ingrese su saldo inicial: $")
        self.titular = titular
        self.saldo = saldo  
        pass
    def depositar (self)-> int:
        """
        Este metodo devuelve el deposito en formato int
        """
        deposito = f.ingresar_numero("Cuanto desea depositar: $")
        self.saldo = (self.saldo + deposito)
        print(f"{self.titular} tu deposito es de ${deposito}")
        self.consultar_saldo()
        return deposito
    
    def retirar(self)-> int:
        """
        Este metodo devuelve el retiro en formato int
        """
        retiro = f.ingresar_numero("Cuanto desea retirar?: $")
        if retiro <= self.saldo and retiro > 0: 
            self.saldo = (self.saldo - retiro)
            print(f"{self.titular} a retirado ${retiro}.")
            self.consultar_saldo()
            return retiro
        else:
            print("No tenes plata flaco")
            
    
    def consultar_saldo (self)-> int:  
        print(f"{self.titular} su saldo es de ${self.saldo}")         

cuentas_bancarias = CuentaBancaria()
while True:
    opcion = input("EliJe la opcion que quieres realizar:\n-Depositar (D) \n-Retirar(R)\n-Mostrar Saldo (S)\n-Si quieres finalizar sesion (F) \n-Opcion:").upper()
    if opcion == "D" or opcion == "R" or opcion == "S" or opcion == "F":
        if opcion == "D":
            cuentas_bancarias.depositar()
        if opcion == "R":
            cuentas_bancarias.retirar()
        if opcion == "S":
            cuentas_bancarias.consultar_saldo()
        if opcion == "F":
            cuentas_bancarias.consultar_saldo()
            fm.terminar()
    else:
        print("Ingresaste una opcion incorrecta (D,R,S,F)")
        print("\n"*10)

