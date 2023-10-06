from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from PIL import Image, ImageTk

class MainWindow:
    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda"+cell.title
        messagebox.showinfo("Información", message)
    def __init__(self,root):
        root.title("MainWindow")
        self.cells = [
            Cell("Emperor Ku","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\Emperor_Ku.jpg"),
            Cell("Emperor Shun","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\EmperorShun.jpg"),
            Cell("Emperor Yao","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\EmperorYao.jpg"),
            Cell("Emperor Zhuanxu","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\EmperorZhuanxu.jpg"),
            Cell("Yellow Emperor","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\Yellowemperor.jpg"),
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))