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
ventana.title("Calculadora")
ventana.geometry("400x600")

# Entrada donde se muestran los númer<os y resultados
entrada = tk.Entry(ventana, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entrada.grid(row=0, column=0, columnspan=4)

# Creación de los botones
botones = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

# Posicionamos los botones en la cuadrícula
fila = 1
columna = 0
for boton in botones:
    if boton == "=":
        tk.Button(ventana, text=boton, padx=40, pady=20, font=("Arial", 18),
                  command=calcular).grid(row=fila, column=columna, columnspan=2)
        columna += 2
    else:
        tk.Button(ventana, text=boton, padx=40, pady=20, font=("Arial", 18),
                  command=lambda b=boton: click_boton(b)).grid(row=fila, column=columna)
        columna += 1
        if columna > 3:
            columna = 0
            fila += 1

# Botón para limpiar la entrada
tk.Button(ventana, text="C", padx=40, pady=20, font=("Arial", 18), command=limpiar_entrada).grid(row=fila, column=0, columnspan=4)

# Bucle principal de la aplicación
ventana.mainloop()
