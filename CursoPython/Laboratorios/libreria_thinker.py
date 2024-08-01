import tkinter as tk

def salir():
  ventana.destroy()  # Cerrar la ventana

ventana = tk.Tk()
ventana.title("Ejemplo de interfaz gráfica")

etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack()

ventana.mainloop()

#2. Obtener entrada de usuario con un cuadro de texto:

import tkinter as tk
def mostrar_texto():
  texto_ingresado = entry.get()
  print(f"Texto ingresado: {texto_ingresado}")

ventana = tk.Tk()
ventana.title("Entrada de texto")

etiqueta = tk.Label(ventana, text="Ingrese un texto:")
etiqueta.pack()

entry = tk.Entry(ventana)
entry.pack()

boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton_mostrar.pack()

ventana.mainloop()

#3. Cambiar el color de fondo al hacer clic en un botón:

import tkinter as tk

def cambiar_color():
  if ventana.config("bg") == "white":
    ventana.config(bg="lightblue")
  else:
    ventana.config(bg="white")

ventana = tk.Tk()
ventana.title("Cambiar color de fondo")

boton = tk.Button(ventana, text="Cambiar color", command=cambiar_color)
boton.pack()

ventana.mainloop()

#4. Crear una interfaz gráfica con pestañas:

import tkinter as tk
from tkinter import ttk

def pestaña1():
  print("Estoy en la pestaña 1")

def pestaña2():
  print("Estoy en la pestaña 2")

ventana = tk.Tk()
ventana.title("Pestañas")

control_pestañas = ttk.Notebook(ventana)

pestaña1_frame = ttk.Frame(control_pestañas)
pestaña2_frame = ttk.Frame(control_pestañas)

control_pestañas.add(pestaña1_frame, text="Pestaña 1")
control_pestañas.add(pestaña2_frame, text="Pestaña 2")

boton_pestaña1 = ttk.Button(pestaña1_frame, text="Acción pestaña 1", command=pestaña1)
boton_pestaña1.pack()

boton_pestaña2 = ttk.Button(pestaña2_frame, text="Acción pestaña 2", command=pestaña2)
boton_pestaña2.pack()

control_pestañas.pack(expand=True, fill="both")

ventana.mainloop()


#5. Crear un menú desplegable:

import tkinter as tk

def opcion_seleccionada(opcion):
  print(f"Opción seleccionada: {opcion}")

ventana = tk.Tk()
ventana.title("Menú desplegable")

defunciones_menu = tk.Menu(ventana)
ventana.config(menu=defunciones_menu)

menu_archivo = tk.Menu(defunciones_menu, tearoff=0)
defunciones_menu.add_cascade(label="Archivo", menu=menu_archivo)

menu_archivo.add_command(label="Nuevo", command=lambda: opcion_seleccionada("Nuevo"))
menu_archivo.add_command(label="Abrir", command=lambda: opcion_seleccionada("Abrir"))
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

ventana.mainloop()

#En Tkinter, puedes manejar el tamaño de los widgets Label, Entry (para formularios) y Button utilizando las opciones width y height. Aquí te dejo un ejemplo:
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de tamaño de widgets")

# Crear un Label de 20 caracteres de ancho y 2 de alto
label = tk.Label(ventana, text="Etiqueta", width=20, height=2)
label.pack()

# Crear un Entry (formulario) de 30 caracteres de ancho
entry = tk.Entry(ventana, width=30)
entry.pack()

# Crear un Button de 15 caracteres de ancho y 2 de alto
button = tk.Button(ventana, text="Botón", width=15, height=2)
button.pack()

ventana.mainloop()