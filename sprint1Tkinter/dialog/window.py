import tkinter as tk
from yes_window import YesWindow
from no_window import NoWindow

class MainWindow:
    root = tk.Tk()
    root.title("Ejemplo de pack")

    label1 = tk.Label(root, text="wtv")

    button1 = tk.Button(root, text="Sí", command= YesWindow.yesWindow)
    button2 = tk.Button(root, text="No", command= NoWindow.noWindow)

    label1.pack(side="top")
    button1.pack(side="left", fill="both", expand=True)
    button2.pack(side="right", fill="both", expand=True)

    root.mainloop()