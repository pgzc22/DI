from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import DetailWindow

class MainWindow:
    def on_button_clicked(self, cell):
        DetailWindow(cell)
    def __init__(self,root):
        root.title("MainWindow")
        self.cells = [
            Cell("Emperor Ku","Emperor Ku was not the most \nimportant of the Five Emperors, \nso it was not considered as \none of the Three Sovereigns","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\Emperor_Ku.jpg"),
            Cell("Emperor Shun","Emperor Shun was not the most \nimportant of the Five Emperors, \nso it was not considered as \none of the Three Sovereigns","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\EmperorShun.jpg"),
            Cell("Emperor Yao","Emperor Yao was not the most \nimportant of the Five Emperors, \nso it was not considered as \none of the Three Sovereigns","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\EmperorYao.jpg"),
            Cell("Emperor Zhuanxu","Emperor Zhuanxu was not the most \nimportant of the Five Emperors, \nso it was not considered as \none of the Three Sovereigns","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\EmperorZhuanxu.jpg"),
            Cell("Yellow Emperor","The Yellow Emperor was the most \nimportant of the Five Emperors, \nto the point it was considered as \none of the Three Sovereigns","C:\\msys64\\home\\Alumno\\DI\\sprint1Tkinter\\catalog\\data\\unedited\\Yellowemperor.jpg"),
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))