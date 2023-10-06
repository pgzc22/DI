import tkinter as tk
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, path):
        self.title = title
        self.path = path
        self.image_tk = ImageTk.PhotoImage(Image.open(self.path).resize((100,100),resample=Image.LANCZOS))