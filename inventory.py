"""
Holds the player's unused items
"""
import tkinter as tk

from item import Item

class Inventory:

    def __init__(self, garden):
        self.itemlist = []
        self.garden = garden
        self.garden.inventory = self
        pass

    def additem(self, itemid):
        self.itemlist += [Item(itemid)]
        self.itemlist[-1].inventory = self
        self.itemlist[-1].ingarden = False
        self.itemlist[-1].garden = self.garden

    def removeitem(self, itemid):
        for i, item in enumerate(self.itemlist):
            if item.itemid == itemid:
                del self.itemlist[i]
                break

    def createwidget(self, root):
        invwindow = tk.Toplevel(root)
        invwindow.title("Inventory")
        n = len(self.itemlist)
        for i, x in enumerate(self.itemlist):
            x.addtowidget(invwindow).grid(column=i%5, row=i//5)
        self.dialog = invwindow

if __name__ == "__main__":
    root = tk.Tk()
    inv = Inventory()
    inv.additem("debug")
    inv.additem("apple")
    inv.additem("applesapling")
    inv.additem("appletree")
    inv.additem("beehive")
    inv.additem("chickens")
    inv.additem("cows")
    inv.additem("fertilizer")
    inv.additem("oaksapling")
    inv.additem("oaktree")
    inv.additem("pigs")
    inv.createwidget(root)
    root.mainloop()
