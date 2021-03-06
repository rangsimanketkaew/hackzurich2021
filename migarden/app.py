#!/usr/bin/env python3

# v. 0.1 - HackZurich 2021

import sys

sys.setrecursionlimit(1500)

import os
import io
import tkinter as tk
import tkinter.scrolledtext as tkscrolled
from tkinter import ttk

import webbrowser

from PIL import ImageTk, Image

## For barcode scanner
import cv2
import numpy as np
from pyzbar.pyzbar import decode

## JSON API
import urllib.request, json 
from json_reader import check_item

## Import garden generator
from .garden import Garden
from .table_product import Table
from .inventory import Inventory
from .item import Item

## convert svg to png
import cairosvg

## Global variables are defined here!
data_file = 'json_reader/products.json'

class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Toplevel Window')

        ttk.Button(self,
                text='Close',
                command=self.destroy).pack(expand=True)

class Migarden:
    """Migarden main app
    """
    def __init__(self):
        self.barcodes = set([])
        self.total_co2 = 0
        self.score = 0
        self.num_trees = 0
        self.slotsnx = 5
        self.slotsny = 4

        self.master = tk.Tk()
        self.start_master()
        self.add_menu()
        self.add_widgets()
        self.welcome_msg()
        self.start_app()

    ##########
    # Helper #
    ##########

    def loadrelimages(self, relativepath, size=(200,200)):
        from PIL import ImageTk, Image
        directory_path = os.path.dirname(__file__)
        file_path = os.path.join(directory_path, relativepath)
        image = Image.open(file_path.replace('\\',"/"))
        image = image.resize(size, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)  
        return img

    def loadimgurl(self, imgurl, size=(200,200)):
        raw_data = urllib.request.urlopen(imgurl).read()
        image = Image.open(io.BytesIO(raw_data))
        image = image.resize(size, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        return img

    def loadimgurl_svg(self, imgurl, size=(200,200)):
        raw_data = cairosvg.svg2png(url=imgurl)
        # raw_data = cairosvg.svg2png(bytestring=open(imgurl).read().encode('utf-8'))
        # raw_data = urllib.request.urlopen(imgurl).read()
        image = Image.open(io.BytesIO(raw_data))
        image = image.resize(size, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        return img

    ############
    # core app #
    ############

    def start_master(self):
        """Start application with UI settings
        """
        self.master.title("MiGarden v.0.1")
        font = "Helvetica 15"
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
        self.frame1 = tk.Frame(self.master)
        self.frame1.grid(padx=5, pady=5, ipadx=2, ipady=2, sticky=tk.N, row=0, column=0)
        self.co2text = tk.Label(self.frame1, text=f"CO2 saved: {self.total_co2} kg")
        self.co2text.grid(padx="10", pady="5", row=0, column=0)

        #---------
        self.btn1 = ttk.Button(self.frame1, text="Scan", command=self.scanner)
        self.btn1.config(width=14)
        self.btn1.grid(padx="10", pady="5", row=1, column=0)
        #---------
        self.btn2 = ttk.Button(self.frame1, text="Calculate score", 
                               command=lambda: [self.calc_score(), self.print_codes()])
        self.btn2.config(width=14)
        self.btn2.grid(padx="10", pady="5", row=2, column=0)
        #---------
        self.btn3 = ttk.Button(self.frame1, text="Inventory", command=self.open_inventory)
        self.btn3.config(width=14)
        self.btn3.grid(padx="10", pady="5", row=1, column=1)
        #---------
        self.btn4 = ttk.Button(self.frame1, text="Advance", command=self.update)
        self.btn4.config(width=14)
        self.btn4.grid(padx="10", pady="5", row=2, column=1)

        ################
        # garden frame #
        ################
        self.garden = Garden(self.master)

        #############
        # inventory #
        #############
        self.inventory = Inventory(self.garden)
        # self.inventory.additem("debug")
        # self.inventory.additem("apple")
        # self.inventory.additem("applesapling")
        # self.inventory.additem("appletree")
        # self.inventory.additem("beehive")
        # self.inventory.additem("chickens")
        # self.inventory.additem("cows")
        # self.inventory.additem("fertilizer")
        # self.inventory.additem("oaksapling")
        # self.inventory.additem("oaktree")
        # self.inventory.additem("pigs")

        ###########
        # Frame 2 #
        ###########
        frame2 = tk.LabelFrame(self.master, text="Progress")
        frame2.grid(padx=15, pady=15, row=3, column=0, sticky=tk.N, columnspan=2)
        # box 1 showing barcode info
        self.box_product = tkscrolled.ScrolledText(frame2)
        self.box_product.configure(height="15", width="42", wrap="word", undo="True")
        self.box_product.grid(row=0, column=0, columnspan=2)

    ###################
    # Barcode scanner #
    ###################

    def info_stop_scanner(self):
        self.show_text_product("Press \'q\' to close the scanner")

    def decoder(self, image):
        gray_img = cv2.cvtColor(image,0)
        barcode = decode(gray_img)
        barcodeData = 0
        
        for obj in barcode:
            points = obj.polygon
            (x,y,w,h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)

            barcodeData = obj.data.decode("utf-8")
            barcodeType = obj.type
            string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
            
            cv2.putText(image, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
            print("Barcode: " + barcodeData +" | Type: "+barcodeType)

            return int(barcodeData)

    def scanner(self):
        cap = cv2.VideoCapture(0)
        no_product = 1
        while True:
            ret, frame = cap.read()
            barcode_data = self.decoder(frame)
            # store unique barcode
            if barcode_data not in self.barcodes:
                # self.show_text(barcode_data)
                print("yes")
                self.show_text_product(f"Product {no_product} added")
                no_product += 1

            self.barcodes.add(barcode_data)

            ## shutdown scanner when detected
            # if int(barcode_data) > 1:
            #     cv2.destroyWindow(winname="Close")
            #     break

            cv2.imshow('Scan your product', frame)
            code = cv2.waitKey(10)
            # press "q" to close the scanner
            if code == ord('q'):
                break

        # cap.release()
        cv2.destroyAllWindows()

    def open_inventory(self):
        self.inventory.createwidget(self.master)

    def open_garden(self):
        self.garden.createwidget(self.master)

    def update(self):
        self.total_co2 += self.garden.update()
        self.co2text = tk.Label(self.frame1, text=f"CO2 saved: {self.total_co2} kg")
        self.co2text.grid(padx="10", pady="5", row=0, column=0)

    ##########################
    # Calculate score        #
    ##########################

    def insert_table(self, items):
        master_table = tk.Toplevel()
        master_table.geometry('900x800')
        master_table.title('Your rewards!')
        master_frame = Frame(master_table)
        master_frame.pack(fill=tk.BOTH,expand=1)

        sec = Frame(master_frame)
        sec.pack(fill=tk.X, side=tk.BOTTOM)
        # Create A Canvas
        my_canvas = tk.Canvas(master_table, width=900, height=800)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        # Add A Scrollbars to Canvas
        x_scrollbar = ttk.Scrollbar(sec, orient=tk.HORIZONTAL, command=my_canvas.xview)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        y_scrollbar = ttk.Scrollbar(master_table, orient=tk.VERTICAL, command=my_canvas.yview)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Configure the canvas
        my_canvas.configure(xscrollcommand=x_scrollbar.set)
        my_canvas.configure(yscrollcommand=y_scrollbar.set)
        my_canvas.bind("<Configure>", lambda e: my_canvas.config(scrollregion=my_canvas.bbox(tk.ALL)))

        # real frame
        frame = tk.Frame(my_canvas)
        # new frame window in canvas
        my_canvas.create_window((0, 0), window=frame, anchor="nw")

        ##### header #####
        self.head1 = tk.Label(frame, text="Product", font=('Helvetica', 18, 'bold')).grid(row=0, column=0)
        self.head2 = tk.Label(frame, text="CO2", font=('Helvetica', 18, 'bold')).grid(row=0, column=1)
        self.head3 = tk.Label(frame, text="Animal welfare", font=('Helvetica', 18, 'bold')).grid(row=0, column=2)
        self.head4 = tk.Label(frame, text="Feature", font=('Helvetica', 18, 'bold')).grid(row=0, column=3)
        self.head5 = tk.Label(frame, text="Env Score", font=('Helvetica', 18, 'bold')).grid(row=0, column=4)

        ##################

        for i, barcode in enumerate(items):
            # self.show_text_product("Barcode: " + str(barcode) + " & score: " + str(score))

            # Column 1
            self.tab1 = tk.Label(frame, text=barcode["name"], 
                                font="helvetica 14", wraplength=200, justify="center")
            self.tab1.grid(row=i+1, column=0)
            # column 2
            imgtab1 = self.loadimgurl_svg(barcode["url_co2"], size=(80,100))
            self.tab2 = tk.Label(frame, width=150, height=150, image=imgtab1)
            self.tab2.image = imgtab1 # save reference
            self.tab2.grid(row=i+1, column=1)
            # Column 3
            if barcode["url_ani"] == None:
                self.tab3 = tk.Label(frame, text="N/A")
            else:
                imgtab2 = self.loadimgurl_svg(barcode["url_ani"], size=(80,100))
                self.tab3 = tk.Label(frame, width=150, height=150, image=imgtab2)
                self.tab3.image = imgtab2 # save reference
            self.tab3.grid(row=i+1, column=2)
            # Column 4
            if len(barcode["url_features"]) == 0:
                self.tab4 = tk.Label(frame, text="N/A")
            else:
                imgtab3 = self.loadimgurl(barcode["url_features"][0], size=(100,100))
                self.tab4 = tk.Label(frame, width=150, height=150, image=imgtab3)
                self.tab4.image = imgtab3 # save reference
            self.tab4.grid(row=i+1, column=3)
            # Column 5
            self.tab5 = tk.Label(frame, text=barcode["env_score"])
            self.tab5.grid(row=i+1, column=4)

        self.rewardstext = tk.Label(frame, text="Congratulations! You won:").grid(row=len(items)+1, column=0)
        self.rewardsitems = Item("applesapling").addtowidget(frame).grid(row=len(items)+1, column=1)
        self.rewardsitems = Item("beehive").addtowidget(frame).grid(row=len(items)+1, column=1)
        self.inventory.additem("beehive")
        self.rewardsitems = Item("applesapling").addtowidget(frame).grid(row=len(items)+1, column=2)
        self.inventory.additem("applesapling")
        self.rewardsitems = Item("oaksapling").addtowidget(frame).grid(row=len(items)+1, column=3)
        self.inventory.additem("oaksapling")

    def calc_score(self):
        # Remove None
        self.barcodes = list(filter(None, self.barcodes))
        for barcode in self.barcodes:
            items, score = check_item.check_json(str(barcode), data_file)
            self.show_text_product("Barcode: " + str(barcode))

        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        chaper_url = "https://tools.learningcontainer.com/sample-json-file.json"
        req = urllib.request.Request(url=chaper_url, headers=headers)
        data = urllib.request.urlopen(req).read()
        data = json.loads(data.decode())
        items, score = check_item.check_json(str(self.barcodes[0]), data_file)
        # print score to text box
        self.show_text_product("My Score: " + str(score))
        # self.change_product_img("assets/cows.jpg")
        self.insert_table(items)

        # convert it back to set
        self.barcodes = set(self.barcodes)

    ##########################
    # Text printer (frame 3) #
    ##########################

    def show_text_product(self, text):
        """Insert text to result box
        """
        self.box_product.insert(tk.INSERT, text + "\n")
        self.box_product.see(tk.END)

    def clear_box_product(self):
        """Clear box
        """
        self.box_product.delete(1.0, tk.END)

    ####################################################

    def welcome_msg(self):
        """Show welcome message in result box:
        """
        self.show_text_product(f"Welcome to MiGarden version 0.1")
        self.show_text_product(f"Developed in HackZurich 2021")
        self.show_text_product(f"For the benefit of mankind")
        self.show_text_product(f"===============================\n")

    def start_app(self):
        """Start application
        """
        self.master.mainloop()
        

def main():
    app = Migarden()
    app.start_app()

if __name__ == "__main__":
    main()
