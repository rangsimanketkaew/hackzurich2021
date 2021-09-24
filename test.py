# from tkinter import *
# root = Tk()

# canv = Canvas(root, width=80, height=80, bg='white')
# canv.grid(row=2, column=3)

# img = PhotoImage(file="assets/apple.jpg")
# canv.create_image(20,20, anchor=NW, image=img)

# mainloop()

from tkinter import *
import os

from PIL import ImageTk, Image

# def loadrelimages(relativepath):
#     from PIL import ImageTk, Image
#     import os
#     directory_path = os.path.dirname(__file__)
#     file_path = os.path.join(directory_path, relativepath)
#     img = ImageTk.PhotoImage(Image.open(file_path.replace('\\',"/")))  
#     return img

root = Tk()

canvas = Canvas(root, width=500, height=500)
img = ImageTk.PhotoImage(Image.open("assets/apple.jpg"))

# loadedimage=loadrelimages('assets/apple.jpg')
# canvas.create_image(250, 250, image=loadedimage)
canvas.create_image(50, 50, image=img)
canvas.pack()

root.mainloop()