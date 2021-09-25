import tkinter as tk
import os

from PIL import ImageTk, Image

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
img = ImageTk.PhotoImage(Image.open("assets/apple.jpg"))

# loadedimage=loadrelimages('assets/apple.jpg')
# canvas.create_image(250, 250, image=loadedimage)
canvas.create_image(50, 50, image=img)
canvas.pack()

root.mainloop()