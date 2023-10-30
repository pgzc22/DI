import tkinter as tk
from tkinter import messagebox
import json
import random

class Juego:
    def __init__(self, difficulty):
        self.difficulty = None
        self.word = None
        self.guessed_letters = []
        self.mistakes = 0
        with open('words.json', 'r') as f:
            self.words = json.load(f)

        with open('images.json', 'r') as f:
            self.images = json.load(f)
        self.difficulty = difficulty
        self.word = random.choice(self.words[difficulty])
        self.game_window = tk.Toplevel(self.window)
        self.game_window.title("Juego del Ahorcado - " + difficulty)

        # Add your widgets here
        self.word_label = tk.Label(self.game_window, text="_" * len(self.word))
        self.word_label.pack()

        self.mistakes_label = tk.Label(self.game_window, text="Fallos: 0")
        self.mistakes_label.pack()

        self.letter_entry = tk.Entry(self.game_window)
        self.letter_entry.pack()

        tk.Button(self.game_window, text="Intentos", command=self.guess_letter).pack()

    def guess_letter(self):
        letter = self.letter_entry.get()
        if letter in self.word and letter not in self.guessed_letters:
            # Replace _ with the letter
            new_word = ""
            for l in self.word:
                if l == letter:
                    new_word += l
                else:
                    new_word += "_"
            self.word_label.config(text=new_word)
            if "_" not in new_word:
                messagebox.showinfo("Enhorabuena", "¡Ganaste!")
                self.game_window.destroy()
                return
        else:
            self.mistakes += 1
            if self.mistakes == 6:
                messagebox.showinfo("Fin del Juego", "¡Perdiste! La palabra era " + self.word)
                self.game_window.destroy()
                return
            
if __name__ == "__main__":
    Juego().window.mainloop()