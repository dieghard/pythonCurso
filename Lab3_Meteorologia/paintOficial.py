import tkinter as tk
from PIL import ImageGrab #pip install pillow
from tkinter import filedialog

def borrar_canvas():
    lienzo.delete("all")
    
    
def cambiar_color_pincel(color):
    print(color)
    color_pincel.set(color)

def seleccionar_color_negro():
    cambiar_color_pincel("Negro")


x_anterior = None
y_anterior = None

def dibujar_inicio(event):
    global x_anterior, y_anterior
    x_anterior = event.x
    y_anterior = event.y
    

def dibujar(event):
    global x_anterior, y_anterior
    lienzo.create_line(x_anterior, y_anterior, event.x, event.y, fill = color_pincel.get())
    x_anterior = event.x
    y_anterior = event.y
    

def guardar_dibujo():
    x0 = lienzo.winfo_rootx()
    y0 = lienzo.winfo_rooty()
    
    x1 = x0 + lienzo.winfo_width()
    y1 = y0 + lienzo.winfo_height()
    
    img = ImageGrab.grab(bbox = (x0, y0, x1, y1))
    archivo = filedialog.asksaveasfilename(defaultextension = ".png")
    if archivo:
        img.save(archivo)


ventana = tk.Tk()
ventana.title("Pain Oficial de Python Team Levalle🐍")
ventana.geometry("500x500")




color_pincel = tk.StringVar()
color_pincel.set("black")

lienzo = tk.Canvas(ventana, width = 400, height = 400, background= "grey")
lienzo.pack()


lienzo.bind("<B1-Motion>", dibujar)
lienzo.bind("<Button-1>", dibujar_inicio)

menu_bar = tk.Menu(ventana)

options_menu = tk.Menu(menu_bar, tearoff = 0)
options_menu.add_command(label="Borrar Dibujo", command=borrar_canvas)
options_menu.add_command(label="Guardar Dibujo", command=guardar_dibujo)
menu_bar.add_cascade(label="Opciones", menu=options_menu)


color_menu = tk.Menu(menu_bar, tearoff = 0)

colores = ["red","green","blue","black","white","yellow","orange","purple","pink","brown","grey","cyan","magenta","teal","coral","turquoise","lavender","silver","gold"]

for color in colores:
    color_menu.add_command(label=color,                          command= lambda c=color: cambiar_color_pincel(c))

menu_bar.add_cascade(label="Color", menu=color_menu)
ventana.config(menu=menu_bar)

ventana.mainloop()

