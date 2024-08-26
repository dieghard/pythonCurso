import funciones as fp

class Producto:
    def __init__(self, nombre, precio, cantidad) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        lista_productos.append(self) #Cada vez que se crea un nuevo producto se guarda en la lista productos_creados
        pass
    def actualizar_precio(self,nuevo_precio):
        self.precio = nuevo_precio
        return 
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        return
    def calcular_valor_total(self):
        valor_total =  self.cantidad * self.precio
        return valor_total

def seleccionar_producto(texto_input:str | None = "Seleccione un producto: ", mostrar_precio :bool | None = False) -> str:
    """
    Funcion para seleccionar un producto de una lista de nombres.

    args:
    texto_input: nos permite pasar el texto a mostrar por consola.
    mostrar_precio: por defecto en falso, si se pone en True muestra tanto el nombre como el precio de los productos disponibles.
    """
    lista_productos = [producto_1,producto_2,producto_3,producto_4,producto_5] #Aca se agregan los productos previamente creados a partir de la clase Producto
    if mostrar_precio == False:
        print(F"Estos son los productos disponibles:")
        for producto in lista_productos:
            print(f"Nombre: {producto.nombre}")
    else:
        print(F"Estos son los productos disponibles:")
        for producto in lista_productos:
            print(f"Nombre: {producto.nombre}, Precio: ${producto.precio}")

    producto_seleccionado = fp.validar_texto(texto_input).capitalize()
    for producto in lista_productos:
        if producto.nombre == producto_seleccionado:
            return producto
        
    print("Producto no encontrado. Por favor seleccione un producto válido.")

def imprimir_todos_los_productos():
    """
    Funcion para imprimir todos los productos creados a partir de la clase Producto
    """
    if not lista_productos:
        print("No se han creado productos.")
    for producto in lista_productos:
        print(f"Nombre: {producto.nombre}, Precio: ${producto.precio}, Hay actualmente: {producto.cantidad}")

def agregar_a_lista_de_compras():
    """
    Función para agregar un producto seleccionado y la cantidad a la lista de compras.
    """
    producto = seleccionar_producto(mostrar_precio=True)
    if producto:
        while True:
                cantidad = fp.ingresar_numero(f"Ingrese la cantidad de {producto.nombre} que desea agregar: ")
                if cantidad > 0:
                    if cantidad <= producto.cantidad:
                        # Verificar si el producto ya está en la lista de compras
                        for item in lista_compras:
                            if item["producto"].nombre == producto.nombre:
                                item["cantidad"] += cantidad
                                print(f"La cantidad de {producto.nombre} en la lista de compras ha sido actualizada a {item['cantidad']} unidades.")
                                producto.cantidad -= cantidad
                                return
                        # Si el producto no está en la lista, agregarlo
                        lista_compras.append({"producto": producto, "cantidad": cantidad})
                        producto.cantidad -= cantidad
                        print(f"{cantidad} unidades de {producto.nombre} han sido agregadas a la lista de compras.")
                        break
                    else:
                        print(f"Solo hay {producto.cantidad} unidades disponibles. Intente nuevamente.")
                else:
                    print("La cantidad debe ser mayor que 0. Intente nuevamente.")
def mostrar_lista_de_compras():
    """
    Función para mostrar todos los productos en la lista de compras con sus cantidades.
    """
    if not lista_compras:
        print("La lista de compras está vacía.")
    else:
        total_compra = 0
        print("Lista de compras:")
        for item in lista_compras:
            producto = item["producto"]
            cantidad = item["cantidad"]
            precio_total = producto.precio * cantidad
            total_compra += precio_total 
            print(f"Nombre: {producto.nombre}, Cantidad: {cantidad}, Precio por unidad: ${producto.precio}, Precio total: ${precio_total}")
        print(f"\nTotal de la compra: ${total_compra}")

lista_compras = []
lista_productos = []
producto_1 = Producto("Tomate", 150, 10)
producto_2 = Producto("Lechuga", 75, 5)
producto_3 = Producto("Huevos", 10, 36)
producto_4 = Producto("Carne", 250, 7)
producto_5 = Producto("Pan", 60, 15)


#MENU
while True:
    opcion_primaria = input("Hola! Bienvenido al sistema de compra/venta. Selecciona que tipo de usuario quieres ingresar: \n Vendedor (V), \n Comprador(C). \n Si quieres finalizar el sistema(F) \n Opcion: ").upper()
    if opcion_primaria == "V" or opcion_primaria == "C" or opcion_primaria == "F":
        if opcion_primaria == "V":
            print("Opcion seleccionada: Vendedor🤑")
            while True:
                opcion_secundaria = input("Hola Vendedor!. \n ¿Que deseas realizar?\n Actualizar Precio (P) \n Actualizar Cantidad (C)\n Finalizar Sesion Vendedor(F)\n Opcion:").upper()
                if opcion_secundaria == "P" or opcion_secundaria == "C" or opcion_secundaria == "F":
                    if opcion_secundaria == "P":
                        producto_seleccionado = seleccionar_producto("Selecciona el producto a actualizarle el precio:")
                        if producto_seleccionado:
                            print(f"Producto seleccionado: {producto_seleccionado.nombre}, \nsu precio actual es de ${producto_seleccionado.precio}.")
                            nuevo_precio = fp.ingresar_numero("Ingrese el nuevo precio: ")
                            producto_seleccionado.actualizar_precio(nuevo_precio)
                            print(f"Precio actualizado correctamente, su precio actual es de ${producto_seleccionado.precio}. \n")
                    if opcion_secundaria == "C":
                        producto_seleccionado = seleccionar_producto("Selecciona el producto a actualizarle la cantidad:")
                        if producto_seleccionado:
                            print(f"Producto seleccionado: {producto_seleccionado.nombre}, \nsu cantidad actual es de {producto_seleccionado.cantidad}.")
                            nueva_cantidad = fp.ingresar_numero("Ingrese el nuevo precio: ")
                            producto_seleccionado.actualizar_cantidad(nueva_cantidad)
                            print(f"Precio actualizado correctamente, su precio actual es de {producto_seleccionado.cantidad}. \n")
                    if opcion_secundaria == "F":
                        print("Opcion seleccionada: Finalizar Sesion")
                        break
        if opcion_primaria == "C":
            print("Opcion seleccionada: Comprador😲")
            while True:
                opcion_secundaria = input("Hola Comprador!. \n ¿Que deseas realizar?\n Ver Productos (P) \n Comprar Algo (C)\n Ver el Carrito(T) \n Finalizar Compra(F)\n Opcion:").upper()
                if opcion_secundaria == "P" or opcion_secundaria == "C" or opcion_secundaria == "T" or opcion_secundaria == "F":
                    if opcion_secundaria == "P":
                        print("Opcion seleccionada: Ver Productos")
                        imprimir_todos_los_productos()
                    if opcion_secundaria == "C":
                        print("Opcion seleccionada: Comprar Algo")
                        agregar_a_lista_de_compras()
                    if opcion_secundaria == "T":
                        print("Opcion seleccionada: Ver Carrito")
                        mostrar_lista_de_compras()
                    if opcion_secundaria == "F":
                        print("Opcion seleccionada: Finalizar Sesion")
                        break
        if opcion_primaria == "F":
            print("Opcion seleccionada: Finalizar Sesion")
            break
