from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox

class MainWindow:
    def on_button_clicked(self, cell):
        message = "Has hecho click en la celda"+cell.title
        messagebox.showinfo("Información", message)
    def __init__(self,root):
        root.title("MainWindow")
        self.cells = [
            Cell("Emperor Ku","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\Emperor_Ku.png"),
            Cell("Emperor Shun","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\EmperorShun.png"),
            Cell("Emperor Yao","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\EmperorYao.png"),
            Cell("Emperor Zhuanxu","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\EmperorZhuanxu.png"),
            Cell("Yellow Emperor","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\edited\\Yellowemperor.png"),
        ]
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))