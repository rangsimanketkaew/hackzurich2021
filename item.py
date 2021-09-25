"""
The item class represents either: locked slots, usable slots, plants, animals, fertilizer, watering
can
"""

import tkinter as tk
from PIL import ImageTk, Image
import os

ITEMS = {
    "debug": {
        "name": "debug",
        "growth": 0,
        "growingfactor": 1.,
        "co2consumption": 1.,
        "drop": "apple",
        "growsto": "oaktree",
        "growsat": 6,
        "lifetime": 10,
        "rare": None,
        "compostable": True,
        "consumable": True,
        "redeemable": True,
        "waterable": True,
        "fertilizable": True,
        "plantable": True
    },
    "apple": {
        "name": "apple",
        "growth": None,
        "growingfactor": None,
        "co2consumption":None,
        "drop": None,
        "lifetime": None,
        "growsto": "oaktree",
        "growsat": 6,
        "rare": None,
        "compostable": False,
        "consumable": False,
        "redeemable": True,
        "waterable": False,
        "fertilizable": False,
        "plantable": False
    },
    "applesapling": {
        "name": "applesappling",
        "growingfactor": 1.,
        "co2consumption": 10.,
        "drop": None,
        "rare": True,
        "lifetime": None,
        "growsto": "appletree",
        "growsat": 5,
        "compostable": True,
        "consumable": False,
        "redeemable": False,
        "waterable": True,
        "fertilizable": True,
        "plantable": True
    },
    "appletree": {
        "name": "appletree",
        "growingfactor": 1.,
        "co2consumption": 20.,
        "drop": "apple",
        "lifetime": None,
        "growsto": None,
        "growsat": None,
        "rare": None,
        "compostable": True,
        "consumable": False,
        "redeemable": False,
        "waterable": True,
        "fertilizable": True,
        "plantable": False
    },
    "beehive": {
        "name": "beehive",
        "growingfactor": 0.,
        "co2consumption": 0.,
        "growsto": "oaktree",
        "growsat": 6,
        "drop": None,
        "lifetime": 5,
        "rare": False,
        "compostable": False,
        "consumable": False,
        "redeemable": False,
        "waterable": False,
        "fertilizable": False,
        "plantable": True
    },
    "chickens": {
        "name": "chickens",
        "growingfactor": 0.,
        "co2consumption": 0.,
        "growsto": "oaktree",
        "growsat": 6,
        "drop": None,
        "lifetime": 2,
        "rare": False,
        "compostable": False,
        "consumable": False,
        "redeemable": False,
        "waterable": False,
        "fertilizable": False,
        "plantable": True
    },
    "cows": {
        "name": "cows",
        "growingfactor": 0.,
        "co2consumption": 0.,
        "growsto": "oaktree",
        "growsat": 6,
        "drop": None,
        "lifetime": 5,
        "rare": True,
        "compostable": False,
        "consumable": False,
        "redeemable": False,
        "waterable": False,
        "fertilizable": False,
        "plantable": True
    },
    "fertilizer": {
        "name": "fertilizer",
        "growingfactor": None,
        "co2consumption": None,
        "growsto": "oaktree",
        "growsat": 6,
        "drop": None,
        "lifetime": None,
        "rare": False,
        "compostable": False,
        "consumable": True,
        "redeemable": False,
        "waterable": False,
        "fertilizable": False,
        "plantable": False
    },
    "oaksapling": {
        "name": "oaksapling",
        "growingfactor": 1.,
        "co2consumption": 12.,
        "drop": None,
        "lifetime": None,
        "rare": None,
        "growsto": "oaktree",
        "growsat": 6,
        "consumable": False,
        "compostable": True,
        "redeemable": False,
        "waterable": True,
        "fertilizable": True,
        "plantable": True
    },
    "oaktree": {
        "name": "oaktree",
        "growingfactor": 1.,
        "co2consumption": 24.,
        "drop": None,
        "lifetime": None,
        "growsto": "oaktree",
        "growsat": 6,
        "rare": None,
        "compostable": True,
        "consumable": False,
        "redeemable": True,
        "waterable": True,
        "fertilizable": True,
        "plantable": True
    },
    "pigs": {
        "name": "pigs",
        "co2saved": None,
        "growingfactor": None,
        "co2consumption": None,
        "growsto": "oaktree",
        "growsat": 6,
        "drop": None,
        "lifetime": 3,
        "rare": False,
        "compostable": False,
        "consumable": False,
        "redeemable": False,
        "waterable": False,
        "fertilizable": False,
        "plantable": True
    },
    "rainfall": {
        "name": "rainfall",
        "co2saved": None,
        "growingfactor": None,
        "co2consumption": None,
        "drop": None,
        "growsto": "oaktree",
        "growsat": 6,
        "lifetime": -1.,
        "rare": False,
        "compostable": False,
        "consumable": True,
        "redeemable": False,
        "waterable": False,
        "fertilizable": False,
        "plantable": False
    }
}

class Item:

    def __init__(self, itemid):
        self.growth = 0.
        self.growsat = ITEMS[itemid]["growsat"]
        self.growsto = ITEMS[itemid]["growsto"]
        self.itemid = itemid
        self.name = ITEMS[itemid]["name"]
        self.growingfactor = ITEMS[itemid]["growingfactor"]  # how fast the item grows
        self.co2consumption = ITEMS[itemid]["co2consumption"]  # how much CO2 the item consumes
        self.drop = ITEMS[itemid]["drop"]  # whether the item has a drop to collect
        self.lifetime = ITEMS[itemid]["lifetime"]  # how long the item stays. negative values mean indefinite
        self.picture = loadrelimages(f"assets/{itemid}.jpg")  # the picture of the item
        self.rare = ITEMS[itemid]["rare"]  # whether the item is a rare drop for sustainable shopping
        self.consumable = ITEMS[itemid]["consumable"]  # whether the item can be consumed for in-game use
        self.compostable = ITEMS[itemid]["compostable"]  # whether the item can be consumed for in-game use
        self.redeemable = ITEMS[itemid]["redeemable"]  # whether the item can be redeemed for real
        self.waterable = ITEMS[itemid]["waterable"]  # whether the item can be watered
        self.plantable = ITEMS[itemid]["plantable"]  # whether the item can be fertilized
        self.inventory = None  # the inventory that holds the item
        self.ingarden = None

    def update(self):
        self.growth += 1
        if self.growth == self.lifetime:
            self.garden.removeitem(self.itemid)
        if self.growth == self.growsat:
            self.garden.removeitem(self.itemid)
            self.garden.additem(self.growsto)

    def addtowidget(self, root):
        widget = tk.Label(root, width=200, height=200, image=self.picture)
        widget.bind("<Button-1>", self.onclick)
        return widget

    def consume(self):
        self.inventory.removeitem(self.itemid)
        self.garden.addbuff(self.itemid)
        self.dialog.destroy()
        self.inventory.dialog.destroy()

    def compost(self):
        self.inventory.removeitem(self.itemid)
        self.inventory.additem("fertilizer")
        self.dialog.destroy()
        self.inventory.dialog.destroy()

    def plant(self):
        self.garden.additem(self.itemid)
        self.inventory.removeitem(self.itemid)
        self.dialog.destroy()
        self.inventory.dialog.destroy()
        self.garden.redraw()

    def water(self):
        self.addbuff("water")

    def addbuff(self):
        pass

    def redeem(self):
        self.inventory.removeitem(self.itemid)
        self.dialog.destroy()
        self.inventory.dialog.destroy()

    def onclick(self, event=None):
        dialog = tk.Toplevel()
        buttons = []
        if self.compostable:
            buttons += [tk.Button(dialog, text="compost", command=self.compost, width=14).grid(row=0, column=0)]
        if self.consumable:
            buttons += [tk.Button(dialog, text="consume", command=self.consume, width=14).grid(row=len(buttons), column=0)]
        if self.plantable and not self.ingarden:
            buttons += [tk.Button(dialog, text="plant", command=self.plant, width=14).grid(row=len(buttons), column=0)]
        if self.waterable and self.ingarden:
            buttons += [tk.Button(dialog, text="water", command=self.water, width=14).grid(row=len(buttons), column=0)]
        if self.redeemable:
            buttons += [tk.Button(dialog, text="redeem", command=self.redeem, width=14).grid(row=len(buttons), column=0)]
        self.dialog = dialog

def loadrelimages(relativepath):
    directory_path = os.path.dirname(__file__)
    file_path = os.path.join(directory_path, relativepath)
    image = Image.open(file_path.replace('\\',"/"))
    image = image.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    return img

if __name__ == "__main__":
    root = tk.Tk()
    debugitem = Item("debug")
    debugitem.addtowidget(root).grid(row=0, column=0)
    appleitem = Item("apple")
    appleitem.addtowidget(root).grid(row=0, column=1)
    applesaplingitem = Item("applesapling")
    applesaplingitem.addtowidget(root).grid(row=0, column=2)
    appletreeitem = Item("appletree")
    appletreeitem.addtowidget(root).grid(row=0, column=3)
    beehiveitem = Item("beehive")
    beehiveitem.addtowidget(root).grid(row=0, column=4)
    chickenitem = Item("chickens")
    chickenitem.addtowidget(root).grid(row=0, column=5)
    cowitem = Item("cows")
    cowitem.addtowidget(root).grid(row=1, column=0)
    fertilizeritem = Item("fertilizer")
    fertilizeritem.addtowidget(root).grid(row=1, column=1)
    oaksaplingitem = Item("oaksapling")
    oaksaplingitem.addtowidget(root).grid(row=1, column=2)
    oaktreeitem = Item("oaktree")
    oaktreeitem.addtowidget(root).grid(row=1, column=3)
    pigitem = Item("pigs")
    pigitem.addtowidget(root).grid(row=1, column=4)
    root.mainloop()
