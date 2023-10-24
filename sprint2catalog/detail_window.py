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
        label3 = ttk.Label(root, text=cell.description, wraplength=160)
        label1.pack(side="top")
        label2.pack()
        label3.pack()
        width=int(160)
        height=int(300)
        #Sets the window size
        root.geometry(str(width)+"x"+str(height))
        #Positions the window in the middle of the screen
        x=(root.winfo_screenwidth() - width)/2
        y=(root.winfo_screenheight() - height)/2
        root.geometry(f"+{int(x)}+{int(y)}")