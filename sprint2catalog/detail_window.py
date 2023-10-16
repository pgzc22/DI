from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from PIL import Image, ImageTk

class DetailWindow:
    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda: "+cell.title
        messagebox.showinfo("Información", message)
    # send the cell again as argument instead of creating a new instance
    def __init__(self, cell):
        root = tk.Toplevel()
        root.title("DetailWindow")
        label1 = ttk.Label(root, text=cell.title)
        label2 = ttk.Label(root, image=cell.image_tk)
        label3 = ttk.Label(root, text=cell.description)
        label1.pack(side="top")
        label2.pack()
        label3.pack(side="bottom")