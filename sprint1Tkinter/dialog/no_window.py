import tkinter as tk

class NoWindow:
    def noWindow():
        root = tk.Tk()
        label1=tk.Label(root, text="shoulda")
        label1.pack()
        root.mainloop()