#Desarrollar un sistema que permita cargar productos en una lista con precio, nombre y cantidad, 
#poder actualizar la cantidad y el precio del mismo.
#Desarrollar un menu para ejecutar el programa de manera más sencilla.
#Desarrollar un menu para elegir entre vender o comprar.
#Agregar los articulos comprados a un carrito de compra e imprimir el total del mismo.

#OBJETIVO DEL EJERCICIO: Arreglar el siguiente codigo que tiene errores.
#Salida esperada:

class Producto:
    def __init__(self, nombre, precio, cantidad) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
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

def ingresar_numero (texto_input:str|None= "Ingrese un numero:")-> int:
    """
    Funcion para ingresar y validar un numero, \n
    texto_input muestra el mensaje por consola
    """
    while True:
        numero_1 = input (texto_input)
        if numero_1.isdigit():
            numero_1 = int(numero_1)
            return numero_1
        else:
            print("El valor ingresado no es un Nro")
            return

def validar_texto(texto_input:str | None="Ingrese un texto: ", validar_vacio : bool| None=False, dato_a_validar :str |None="dato")->str:
    """
    Valida si es un texto. Se puede validar que no quede el dato vacio 
    \n y se puede pasar que dato valida para mostrar al usuario
    """
    while True:
        texto = input(texto_input)
        if validar_vacio: 
            if texto =="":
                print (f"El {dato_a_validar} no debe quedar vacio!")       
            elif texto.isalpha():
                break
            else:
                print("El dato no corresponde a lo solicitado.")
        else:
            break
    return texto

def seleccionar_producto(texto_input:str | None = "Seleccione un producto: ") -> str:
    """
    Funcion para seleccionar un producto de una lista de nombres.
    """
    lista_productos = [producto_1,producto_2,producto_3,producto_4,producto_5]
    lista_nombres_productos = [producto_1.nombre,producto_2.nombre,producto_3.nombre,producto_4.nombre,producto_5.nombre]
    print(f"Productos disponibles {lista_nombres_productos}")
    producto_seleccionado = validar_texto(texto_input).capitalize()
    for producto in lista_productos:
        if producto.nombre == producto_seleccionado:
            return producto
        
    print("Producto no encontrado. Por favor seleccione un producto válido.")

    
producto_1 = Producto("Tomate", 150, 10)
producto_2 = Producto("Lechuga", 75, 5)
producto_3 =Producto("Huevos", 10, 36)
producto_4 =Producto("Carne", 250, 7)
producto_5 = Producto("Pan", 60, 15)

#MENU
while True:
    opcion_primaria = input("Hola! Bienvenido al sistema de compra/venta. Selecciona que tipo de usuario quieres ingresar: \n Vendedor (V), \n Comprador(C). \n Si quieres finalizar el sistema(F) \n Opcion: ").upper()
    if opcion_primaria == "V" or opcion_primaria == "C" or opcion_primaria == "F":
        if opcion_primaria == "V":
            while True:
                print("Opcion seleccionada: Vendedor")
                opcion_secundaria = input("Hola Vendedor!. \n ¿Que deseas realizar?\n Actualizar Precio (P) \n Actualizar Cantidad (C)\n Finalizar Sesion Vendedor(F)\n Opcion:").upper()
                if opcion_secundaria == "P" or opcion_secundaria == "C" or opcion_secundaria == "F":
                    if opcion_secundaria == "P":
                        producto_seleccionado = seleccionar_producto("Selecciona el producto a actualizarle el precio:")
                        if producto_seleccionado:
                            print(f"Producto seleccionado: {producto_seleccionado.nombre}, \nsu precio actual es de {producto_seleccionado.precio}.")
                            nuevo_precio = ingresar_numero("Ingrese el nuevo precio: ")
                            producto_seleccionado.actualizar_precio(nuevo_precio)
                            print(f"Precio actualizado correctamente, su precio actual es de {producto_seleccionado.precio}. \n")
                    if opcion_secundaria == "C":
                        producto_seleccionado = seleccionar_producto("Selecciona el producto a actualizarle la cantidad:")
                        if producto_seleccionado:
                            print(f"Producto seleccionado: {producto_seleccionado.nombre}, \nsu cantidad actual es de {producto_seleccionado.cantidad}.")
                            nueva_cantidad = ingresar_numero("Ingrese el nuevo precio: ")
                            producto_seleccionado.actualizar_cantidad(nueva_cantidad)
                            print(f"Precio actualizado correctamente, su precio actual es de {producto_seleccionado.cantidad}. \n")
                    if opcion_secundaria == "F":
                        print("Opcion seleccionada: Finalizar Sesion")
                        break
        if opcion_primaria == "C":
            print("Opcion seleccionada: Comprador")
        if opcion_primaria == "F":
            print("Opcion seleccionada: Finalizar Sesion")
            break
