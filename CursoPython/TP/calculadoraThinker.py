import tkinter as tk

def calcular(operacion):
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplica':
        resultado = num1 * num2
    elif operacion == 'divide':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = 'Error: División por cero'
    label_resultado.config(text = "Resultado: " + str(resultado))

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x200") # Establecer el tamaño de la ventana a 300x200
ventana.resizable(True,True) # Hacer que la ventana  sea redimensionable
ventana.configure(background='white') # Cambiar el color de fondo de la ventana a blanco
#ventana.iconbitmap('ruta/a/tu/icono.ico') # Cambiar el ícono de la ventana


entry1 = tk.Entry(ventana)
entry1.pack()

entry2 = tk.Entry(ventana)
entry2.pack()

label_resultado = tk.Label(ventana, text = "Resultado: ")
label_resultado.pack()

boton_suma = tk.Button(ventana, text = "Sumar", command = lambda: calcular('suma'), bg='green')
boton_suma.pack()
# # Crear un botón con un ancho de 20 caracteres, una altura de 2 líneas y el texto "Mi Botón"
# boton = tk.Button(ventana, text="Mi Botón", width=20, height=2)
# boton.pack()

boton_resta = tk.Button(ventana, text = "Restar", command = lambda: calcular('resta'), bg='red')
boton_resta.pack()

boton_multiplica = tk.Button(ventana, text = "Multiplicar", command = lambda: calcular('multiplica'))
boton_multiplica.pack()

boton_divide = tk.Button(ventana, text = "Dividir", command = lambda: calcular('divide'))
boton_divide.pack()

ventana.mainloop()
