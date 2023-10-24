# Import necessary modules from tkinter and PIL
from tkinter import ttk
import tkinter as tk
from cell import Cell
from tkinter import messagebox
from detail_window import DetailWindow
from PIL import Image, ImageTk

class MainWindow:
    # Define a method that will be called when a button is clicked. 
    # This method creates a new DetailWindow with the details of the clicked cell.
    def on_button_clicked(self, cell):
        DetailWindow(cell)
    def __init__(self,root, json_data):
        # Set the title of the root window
        root.title("MainWindow")
        # Create a menu bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)
        # Create a menu and add it to the menu bar
        help_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        # Add a command to the menu
        help_menu.add_command(
            label="Acerca de",
            command=self.show_about)
        self.cells=[]
        # For each item in json_data, create a new Cell with the name, description, and image URL from the item.
        # Add the new Cell to the cells list.
        for i in json_data:
            name=i.get("name")
            description=i.get("description")
            url=i.get("image_url")
            self.cells.append(Cell(name, description, url))
        # For each cell in cells, create a new Label with the cell's image and title.
        # Add the Label to the root window's grid.
        # Bind the Label's <Button-1> (left mouse button) event to the on_button_clicked method.
        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))
        
        width=int(180)
        height=int(400)
        #Sets the window size
        root.geometry(str(width)+"x"+str(height))
        #Positions the window in the middle of the screen
        x=(root.winfo_screenwidth() - width)/2
        y=(root.winfo_screenheight() - height)/2
        root.geometry(f"+{int(x)}+{int(y)}")
    def show_about(self):
        messagebox.showinfo("Acerca del desarrollador", "El desarrollador desearía que no lloviese")