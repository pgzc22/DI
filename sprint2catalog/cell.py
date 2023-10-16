import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, description, path):
        self.title = title
        self.description = description
        self.path = path
        # lanczos generally produces better results but its more computationally intensive than bicubic,
        # unless the computer that will run the code is a pos, use lanczos
        self.image_tk = ImageTk.PhotoImage(Image.open(self.path).resize((100,100),resample=Image.LANCZOS))