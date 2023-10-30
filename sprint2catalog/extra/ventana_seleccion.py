import tkinter as tk
from ventana_juego import Juego

class Seleccion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Juego del Ahorcado")

        self.difficulty_buttons()

    def difficulty_buttons(self):
        tk.Button(self.window, text="Easy", command=lambda: Juego("Easy")).pack()
        tk.Button(self.window, text="Normal", command=lambda: Juego("Normal")).pack()
        tk.Button(self.window, text="Hard", command=lambda: Juego("Hard")).pack()
        tk.Button(self.window, text="Exit", command=self.window.quit).pack()


if __name__ == "__main__":
    Seleccion().window.mainloop()
