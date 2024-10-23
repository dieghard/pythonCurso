import tkinter as tk
from tkinter import ttk, colorchooser
from tkinter import messagebox

class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint en Python")
        
        # Variables
        self.current_color = "black"
        self.brush_size = 2
        
        # Crear el canvas principal
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        
        # Crear frame para herramientas
        self.tools_frame = ttk.Frame(self.root)
        self.tools_frame.pack(side=tk.TOP, fill=tk.X)
        
        # Botones de herramientas
        self.color_button = ttk.Button(self.tools_frame, text="Color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=5)
        
        # Selector de tamaño
        ttk.Label(self.tools_frame, text="Tamaño:").pack(side=tk.LEFT, padx=5)
        self.size_scale = ttk.Scale(self.tools_frame, from_=1, to=50, orient=tk.HORIZONTAL,
                                  command=self.change_size)
        self.size_scale.set(2)  # tamaño inicial
        self.size_scale.pack(side=tk.LEFT, padx=5)
        
        # Botón para limpiar
        self.clear_button = ttk.Button(self.tools_frame, text="Limpiar", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        # Paleta de colores rápidos
        self.create_color_palette()
        
        # Eventos del mouse
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        
        self.old_x = None
        self.old_y = None

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                  width=self.brush_size, fill=self.current_color,
                                  capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def choose_color(self):
        color = colorchooser.askcolor(title="Elige un color")[1]
        if color:
            self.current_color = color

    def change_size(self, event):
        self.brush_size = self.size_scale.get()

    def clear_canvas(self):
        self.canvas.delete("all")
        
    def create_color_palette(self):
        colors = ['black', 'gray', 'brown', 'red', 'orange', 'yellow', 
                 'green', 'blue', 'purple', 'white']
        self.color_frame = ttk.Frame(self.tools_frame)
        self.color_frame.pack(side=tk.LEFT, padx=5)
        
        for color in colors:
            btn = tk.Button(self.color_frame, bg=color, width=2, height=1,
                          command=lambda c=color: self.set_color(c))
            btn.pack(side=tk.LEFT, padx=1)
            
    def set_color(self, color):
        self.current_color = color

if __name__ == "__main__":
    root = tk.Tk()
    Paint(root)
    root.mainloop()