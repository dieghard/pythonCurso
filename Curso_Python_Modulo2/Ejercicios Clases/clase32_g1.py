import funciones as fp

class Contador:
    """
    Clase Contador:
    
    Metodos:
    \n incrementa(): Al llamarlo suma uno a la variable interna cuenta.
    \n decrementar(): Al llamarlo resta uno a la variable interna cuenta.
    \n mostrar_contador(): Al llamarlo imprime por consola el valor actual del contador.
    \n reiniciar(): Al llamarlo vuelve el valor de la variable interna cuenta a 0.
    """
    def __init__(self) -> None:
        self.cuenta = 0 
        
    def incrementar (self):
        self.cuenta += 1
        return
    
    def decrementar (self):
        if self.cuenta > 0:
            self.cuenta -= 1
        else:
            print (f"  ERROR!!!! El contador esta {self.cuenta} ")
        return
    
    def mostrar_contador (self):
        print (f" El valor de contador es: {self.cuenta}")
        return
    
    def reiniciar (self):
        self.cuenta = 0
        return

#Objetivo: Crear una clase llamada Producto 
# que tenga tres atributos: nombre, precio y cantidad. 
# Y tenga 3 metodos, Actualizar Precio, Actualizar Cantidad y Calcular valor total, 
#el primero modificara el precio del producto,
# el segundo la cantidad 
# y el ultimo debera multiplicar la cantidad por el precio del producto seleccionado para saber el valor total del inventario. 
class Producto:
    def __init__(self, nombre, precio, cantidad) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        pass
    def actualizar_precio(self):
        return
    def actualizar_cantidad(self):
        return
    def calcular_valor_total(self):
        return
    
