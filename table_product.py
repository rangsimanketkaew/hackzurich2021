import tkinter as tk
import os

class Table(tk.Toplevel):
    """Mygarden main app
    """
    def __init__(self, data_list):
        self.master = tk.Toplevel()
        self.insert_table(data_list)
        self.master.mainloop()

    def loadrelimages(self, relativepath, size=(200,200)):
        from PIL import ImageTk, Image
        directory_path = os.path.dirname(__file__)
        file_path = os.path.join(directory_path, relativepath)
        image = Image.open(file_path.replace('\\',"/"))
        image = image.resize(size, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image, master=self.master)  
        return img

    def insert_table(self, data_list):
        # loop over product
        # for i in range(4):

        # Column 1
        loadedimage = self.loadrelimages('assets/apple.jpg')
        self.canvas_1 = tk.Label(self.master, width=200, height=200, image=loadedimage)
        self.canvas_1.grid(row=0, column=0)

        # Column 2
        loadedimage = self.loadrelimages('assets/apple.jpg')
        self.canvas_1 = tk.Label(self.master, width=200, height=200, image=loadedimage)
        self.canvas_1.grid(row=0, column=1)