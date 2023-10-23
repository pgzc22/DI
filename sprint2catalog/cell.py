# Importing necessary libraries
import tkinter as tk
from PIL import Image, ImageTk
# Used for making HTTP requests, a url to a image in this case
import requests
# Used for reading and writing binary data from/to a stream in memory
from io import BytesIO

class Cell:
    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        #Lanczos generally produces better results but its more computationally intensive than bicubic,
        #unless the computer that will run the code is a pos, use lanczos
        self.image = self.load_image_from_url(url).resize((100,100), resample=Image.LANCZOS)
        # The image_tk attribute is a tkinter-compatible version of the image.
        self.image_tk = ImageTk.PhotoImage(self.image)
    def load_image_from_url(self, url):
        response=requests.get(url)
        img=Image.open(BytesIO(response.content))
        return img