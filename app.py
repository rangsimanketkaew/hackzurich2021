import os
import tkinter as tk
import tkinter.scrolledtext as tkscrolled

# from tkinter import PhotoImage, filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo

from datetime import datetime
import webbrowser
# from urllib.request import urlopen
# from PIL import ImageTk, Image

## For barcode scanner
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def loadrelimages(relativepath):
    from PIL import ImageTk, Image
    import os
    directory_path = os.path.dirname(__file__)
    file_path = os.path.join(directory_path, relativepath)
    img = ImageTk.PhotoImage(Image.open(file_path.replace('\\',"/")))  
    return img

class Mygarden:
    """Mygarden main app
    """
    def __init__(self):
        self.master = tk.Tk()

        self.start_master()
        self.add_menu()
        self.add_widgets()
        self.start_app()

    def start_master(self):
        """Start application with UI settings
        """
        self.master.title("MyGarden v.0.1")
        font = "Arial 10"
        self.master.option_add("*Font", font)
        # center_width = (self.master.winfo_screenwidth() / 2.0) - (550 / 2.0)
        # center_height = (self.master.winfo_screenheight() / 2.0) - (750 / 2.0)
        # self.master.geometry("525x635+%d+%d" % (center_width, center_height))
        # self.master.resizable(0, 0)

    def add_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        file_menu = tk.Menu(self.master, tearoff=0)
        help_menu = tk.Menu(self.master, tearoff=0)

        # file menu
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=lambda: self.master.destroy())

        # help meny
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="User Documentation", command=lambda: webbrowser.open_new_tab(
            "Contact us"
        ))
    
    def add_widgets(self):
        """Add all widgets and components to master windows

        All gui styles use ttk style
        """
        gui_ttk = ttk.Style()
        gui_ttk.configure("TButton", relief="sunken", padding=5)
        gui_ttk.configure("My.TLabel", foreground="balck")
        gui_ttk.configure("My.TLabelframe", foreground="brown")

        ###########
        # Frame 1 #
        ###########

        frame1 = tk.LabelFrame(self.master, text="Program Console")
        frame1.grid(padx=5, pady=5, ipadx=2, ipady=2, sticky=tk.N, row=0, column=0)

        btn1 = ttk.Button(frame1, text="Inventory", command=self.test_command)
        btn1.config(width=14)
        btn1.grid(padx="10", pady="5", row=0, column=0)
        btn2 = ttk.Button(frame1, text="Scan", command=self.test_command)
        btn2.config(width=14)
        btn2.grid(padx="10", pady="5", row=0, column=1)

        ###########
        # Frame 2 #
        ###########

        frame2 = tk.Frame(self.master)
        frame2.grid(padx=5, pady=10, row=1, column=0, columnspan=3)
        self.box_result = tkscrolled.ScrolledText(frame2)
        self.box_result.configure(height="19", width="70", wrap="word", undo="True")
        self.box_result.grid(row=0)

        # # show image
        # def show_tree(self):
        #     canvas = tk.Canvas(self.master, width=300, height=300)
        #     canvas.pack()
        #     img = PhotoImage

        ###########
        # Frame 3 #
        ###########
        frame3 = tk.Frame(self.master)
        frame3.grid(column=0, columnspan=3)
        # img = ImageTk.PhotoImage(Image.open("assets/apple.jpg"))
        canvas = tk.Canvas(frame3, width=200, height=200)
        loadedimage = loadrelimages('assets/oak.jpg')
        canvas.create_image(200, 200, image=loadedimage)
        # canvas.create_image(200, 200, image=img)
        canvas.pack()

    # def scanner(self):


    def start_app(self):
        """Start application
        """
        self.master.mainloop()

    ###### All functions should be defined from here on ######
    def test_command(self):
        print("ok")
    
# window.title("Welcome to [M]yGarden")
# window.geometry('500x300')

# btt = tk.Button(window, text="Enter", command = helloCallBack())

# chk_state = tk.BooleanVar()
# chk_state.set(True) #set check state
# chk = tk.Checkbutton(window, text='Choose', var=chk_state)
# chk.grid(column=0, row=0)
# btt.grid(column=0, row=1)

# window.mainloop()

def main():
    app = Mygarden()
    app.start_app()

if __name__ == "__main__":
    main()