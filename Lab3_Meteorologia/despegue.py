import tkinter as tk

# Funciones
def despegue_cohete(contador=5):
    if contador > 0:
        etiqueta['text'] = contador
        etiqueta.config(fg="green")
        # Llamamos a la función nuevamente después de 1 segundo (1000 ms)
        ventana.after(1000, despegue_cohete, contador - 1)
    else:
        etiqueta['text'] = "Despegue 🚀🚀🚀"
        etiqueta.config(fg="red")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("DESPEGUE")  # Nombre de la ventana
ventana.geometry("500x500")  # Tamaño de la ventana

# Creación de la etiqueta
etiqueta = tk.Label(ventana, text="5", font=("Arial", 50))
etiqueta.place(relx=0.5, rely=0.5, anchor='center')  # Centrado en la ventana

# Creación del botón
boton = tk.Button(ventana, text="INICIO 👩‍🚀👨‍🚀", command=lambda: despegue_cohete(5))
boton.place(relx=0.5, rely=0.7, anchor='center', width=100, height=50)


# Inicio del bucle principal de Tkinter
ventana.mainloop()
