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