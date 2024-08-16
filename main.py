import tkinter as tk
from tkinter import canvas



class Paintapp:
    def __init__(self,root):
        self.root=root
        self.root.title("Ms-Paint Clone")

        self.pen_button=tk.Button(self.root,text="Pen",bg="white", command=self.use_pen)
        self.pen_button.pack(side=tk.LEFT)
        self.brush_button = tk.Button(self.root, text="Brush", bg="white", command=self.use_brush)
        self.brush_button.pack(side=tk.LEFT)
        self.color_button = tk.Button(self.root, text="Color", bg="white", command=self.use_color)
        self.size_button = tk.Button(self.root, text="Size", bg="white", command=self.use_color)

window=tk.Tk()
window.title("Ms-paint")
