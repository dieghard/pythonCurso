#Objetivo: Crear una clase llamada Producto 
# que tenga tres atributos: nombre, precio y cantidad. 
# Y tenga 3 metodos, Actualizar Precio, Actualizar Cantidad y Calcular valor total, 
#el primero modificara el precio del producto,
# el segundo la cantidad 
# y el ultimo debera multiplicar la cantidad por el precio del producto seleccionado para saber el valor total del inventario. 
import funciones as fs 

class Producto:
    def __init__(self, nombre: str, precio: int, cantidad: int, ) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        pass
    def actualizar_precio(self, precio_nuevo: int):
        self.precio= precio_nuevo
        return
    def actualizar_cantidad(self, cantidad_actualizada: int):
        self.cantidad=cantidad_actualizada
        return
    def calcular_valor_total(self): 
        """Tuve que poner ->int para que me devuelva un entero xk sino me devolvia NONE y cuando ejecuta, la variable de la linea 40, me lo marca

        """
        return self.precio * cantidad
        
nombre = fs.validar_texto("Ingrese el nombre del producto: ")
cantidad = fs.ingresar_numero("Ingrese la cantidad: ")
precio = int(input("Ingrese el precio $ "))
mi_producto = Producto(nombre, precio, cantidad)
cantidad_nueva = int(input("Ingrese la cantidad a actualizar: "))
mi_producto.actualizar_cantidad(cantidad_nueva)
precio_nuevo = int(input ("Ingrese el precio nuevo en $ "))
mi_producto.actualizar_precio(precio_nuevo)
valor_actualizado = mi_producto.calcular_valor_total()
print(f"El producto {mi_producto.nombre} tiene un valor total en $ de {valor_actualizado} ")