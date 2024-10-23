import tkinter as tk

# Funciones
def click_boton(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, actual + str(valor))

def limpiar_entrada():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora hecha por Gaspar")
ventana.geometry("400x600")
ventana.configure(bg="#282C34")

# Entrada donde se muestran los números y resultados
entrada = tk.Entry(ventana, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, bg="#ABB2BF", justify='right')
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Colores para los botones
color_boton = "#61AFEF"
color_boton_operador = "#E06C75"
color_boton_igual = "#98C379"
color_boton_limpiar = "#E5C07B"
color_fondo = "#282C34"

# Creación de los botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Función para crear los botones
def crear_boton(text, fila, columna, color=color_boton, colspan=1):
    return tk.Button(ventana, text=text, padx=20, pady=20, font=("Arial", 18), 
                     bg=color, fg="white", bd=0, command=lambda: click_boton(text) if text != "=" else calcular()).grid(row=fila, column=columna, columnspan=colspan, padx=5, pady=5, sticky="nsew")

# Crear botones numéricos y de operadores
for (text, row, col) in botones:
    color = color_boton_operador if text in ['/', '*', '-', '+'] else color_boton
    colspan = 2 if text == "=" else 1
    crear_boton(text, row, col, color=color, colspan=colspan)

# Botón de limpiar
tk.Button(ventana, text="C", padx=20, pady=20, font=("Arial", 18), bg=color_boton_limpiar, 
          fg="white", bd=0, command=limpiar_entrada).grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Ajustes para hacer los botones escalables
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# Bucle principal de la aplicación
ventana.mainloop()
