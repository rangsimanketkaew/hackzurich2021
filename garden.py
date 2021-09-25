"""
Holds the player's in use items
"""
import tkinter as tk
from item import Item

class Garden:

    def __init__(self):
        self.itemlist = []
        self.bufflist = []

    def createwidget(self, root):
        self.root = root
        tk.Button(root, text="kik")
        n = len(self.itemlist)
        if not self.itemlist:
            tk.Frame(self.root, width=200, height=200, bg="brown").grid(column=0, row=0)
        else:
            for i, x in enumerate(self.itemlist):
                x.addtowidget(self.root).grid(column=i%5, row=i//5)

    def addbuff(self, itemid):
        self.bufflist += [itemid]

    def additem(self, itemid):
        self.itemlist += [Item(itemid)]
        self.itemlist[-1].ingarden = True
        self.itemlist[-1].inventory = self.inventory
        self.itemlist[-1].garden = self
        self.redraw()

    def removeitem(self, itemid):
        for i, item in enumerate(self.itemlist):
            if item.itemid == itemid:
                del self.itemlist[i]
                break

    def redraw(self):
        self.createwidget(self.root)

    def update(self):
        # advance time
        for item in self.itemlist:
            item.update()

if __name__ == "__main__":
    root = tk.Tk()
    garden = Garden(5, 4)


# # The factory function
# def dnd_start(source, event):
#     h = DndHandler(source, event)
#     if h.root:
#         return h
#     else:
#         return None
#
# # The class that does drag and drop
# class DndHandler:
#     root = None
#     def __init__(self, source, event):
#         if event.num > 5:
#             return
#         root = event.widget._root()
#         try:
#             root.__dnd
#             return # Don't start recursive dnd
#         except AttributeError:
#             root.__dnd = self
#             self.root = root
#         self.source = source
#         self.target = None
#         self.initial_button = button = event.num
#         self.initial_widget = widget = event.widget
#         self.release_pattern = "<B%d-ButtonRelease-%d>" % (button, button)
#         self.save_cursor = widget['cursor'] or ""
#         widget.bind(self.release_pattern, self.on_release)
#         widget.bind("<Motion>", self.on_motion)
#         widget['cursor'] = "hand2"
#
#     def __del__(self):
#         root = self.root
#         self.root = None
#         if root:
#             try:
#                 del root.__dnd
#             except AttributeError:
#                 pass
#
#     def on_motion(self, event):
#         x, y = event.x_root, event.y_root
#         target_widget = self.initial_widget.winfo_containing(x, y)
#         source = self.source
#         new_target = None
#         while target_widget:
#             try:
#                 attr = target_widget.dnd_accept
#             except AttributeError:
#                 pass
#             else:
#                 new_target = attr(source, event)
#                 if new_target:
#                     break
#             target_widget = target_widget.master
#         old_target = self.target
#         if old_target is new_target:
#             if old_target:
#                 old_target.dnd_motion(source, event)
#         else:
#             if old_target:
#                 self.target = None
#                 old_target.dnd_leave(source, event)
#             if new_target:
#                 new_target.dnd_enter(source, event)
#                 self.target = new_target
#
#     def on_release(self, event):
#         self.finish(event, 1)
#
#     def cancel(self, event=None):
#         self.finish(event, 0)
#
#     def finish(self, event, commit=0):
#         target = self.target
#         source = self.source
#         widget = self.initial_widget
#         root = self.root
#         try:
#             del root.__dnd
#             self.initial_widget.unbind(self.release_pattern)
#             self.initial_widget.unbind("<Motion>")
#             widget['cursor'] = self.save_cursor
#             self.target = self.source = self.initial_widget = self.root = None
#             if target:
#                 if commit:
#                     target.dnd_commit(source, event)
#                 else:
#                     target.dnd_leave(source, event)
#         finally:
#             source.dnd_end(target, event)
#
# # ----------------------------------------------------------------------
# # Class for gardening
#
# class Icon:
#     def __init__(self, name):
#         self.name = name
#         self.canvas = self.label = self.id = None
#
#     def attach(self, canvas, x=10, y=10):
#         if canvas is self.canvas:
#             self.canvas.coords(self.id, x, y)
#             return
#         if self.canvas:
#             self.detach()
#         if not canvas:
#             return
#         label = tk.Label(canvas, text=self.name, borderwidth=2, relief="raised")
#         id = canvas.create_window(x, y, window=label, anchor="nw")
#         self.canvas = canvas
#         self.label = label
#         self.id = id
#         label.bind("<ButtonPress>", self.press)
#
#     def detach(self):
#         canvas = self.canvas
#         if not canvas:
#             return
#         id = self.id
#         label = self.label
#         self.canvas = self.label = self.id = None
#         canvas.delete(id)
#         label.destroy()
#
#     def press(self, event):
#         if dnd_start(self, event):
#             # where the pointer is relative to the label widget:
#             self.x_off = event.x
#             self.y_off = event.y
#             # where the widget is relative to the canvas:
#             self.x_orig, self.y_orig = self.canvas.coords(self.id)
#
#     def move(self, event):
#         x, y = self.where(self.canvas, event)
#         self.canvas.coords(self.id, x, y)
#
#     def putback(self):
#         self.canvas.coords(self.id, self.x_orig, self.y_orig)
#
#     def where(self, canvas, event):
#         # where the corner of the canvas is relative to the screen:
#         x_org = canvas.winfo_rootx()
#         y_org = canvas.winfo_rooty()
#         # where the pointer is relative to the canvas widget:
#         x = event.x_root - x_org
#         y = event.y_root - y_org
#         # compensate for initial pointer offset
#         return x - self.x_off, y - self.y_off
#
#     def dnd_end(self, target, event):
#         pass
#
# class Toys:
#     def __init__(self):
#         self.canvas = self.label = self.id = None
#
#     def loadrelimages(self, relativepath):
#         from PIL import ImageTk, Image
#         directory_path = os.path.dirname(__file__)
#         file_path = os.path.join(directory_path, relativepath)
#         image = Image.open(file_path.replace('\\',"/"))
#         image = image.resize((50, 50), Image.ANTIALIAS)
#         # img = ImageTk.PhotoImage(image, master=self.canvas)
#         img = ImageTk.PhotoImage(image)
#         return img
#
#     def attach(self, canvas, x=100, y=100):
#         if canvas is self.canvas:
#             self.canvas.coords(self.id, x, y)
#             return
#         if self.canvas:
#             self.detach()
#         if not canvas:
#             return
#
#         toy_1 = tk.Canvas(canvas, width=500, height=500)
#         loadedimage = self.loadrelimages('assets/pigs.jpg')
#         # toy_1 = toy_1.create_image(50, 50, anchor="center", image=loadedimage)
#         toy_1 = tk.Label(canvas, image=loadedimage, borderwidth=2, relief="raised")
#
#         id = canvas.create_window(x, y, window=toy_1.grid(), anchor="nw")
#         self.canvas = canvas
#         # self.label = label
#         self.label = toy_1
#         self.id = id
#         toy_1.bind("<ButtonPress>", self.press)
#
#     def detach(self):
#         canvas = self.canvas
#         if not canvas:
#             return
#         id = self.id
#         label = self.label
#         self.canvas = self.label = self.id = None
#         canvas.delete(id)
#         label.destroy()
#
#     def press(self, event):
#         if dnd_start(self, event):
#             # where the pointer is relative to the label widget:
#             self.x_off = event.x
#             self.y_off = event.y
#             # where the widget is relative to the canvas:
#             self.x_orig, self.y_orig = self.canvas.coords(self.id)
#
#     def move(self, event):
#         x, y = self.where(self.canvas, event)
#         self.canvas.coords(self.id, x, y)
#
#     def putback(self):
#         self.canvas.coords(self.id, self.x_orig, self.y_orig)
#
#     def where(self, canvas, event):
#         # where the corner of the canvas is relative to the screen:
#         x_org = canvas.winfo_rootx()
#         y_org = canvas.winfo_rooty()
#         # where the pointer is relative to the canvas widget:
#         x = event.x_root - x_org
#         y = event.y_root - y_org
#         # compensate for initial pointer offset
#         return x - self.x_off, y - self.y_off
#
#     def dnd_end(self, target, event):
#         pass
#
# class Garden(tk.Toplevel):
#     def __init__(self, master):
#         # tk.Toplevel.__init__(master)
#
#         ## Everything is in the same frame
#         self.top = master
#
#         ## All are in different frames
#         # self.top = tk.Toplevel(master)
#
#         self.canvas = tk.Canvas(self.top, width=400, height=100)
#         self.canvas.pack(fill="both", expand=1)
#         self.canvas.dnd_accept = self.dnd_accept
#
#     def dnd_accept(self, source, event):
#         return self
#
#     def dnd_enter(self, source, event):
#         self.canvas.focus_set() # Show highlight border
#         x, y = source.where(self.canvas, event)
#         x1, y1, x2, y2 = source.canvas.bbox(source.id)
#         dx, dy = x2-x1, y2-y1
#         self.dndid = self.canvas.create_rectangle(x, y, x+dx, y+dy)
#         self.dnd_motion(source, event)
#
#     def dnd_motion(self, source, event):
#         x, y = source.where(self.canvas, event)
#         x1, y1, x2, y2 = self.canvas.bbox(self.dndid)
#         self.canvas.move(self.dndid, x-x1, y-y1)
#
#     def dnd_leave(self, source, event):
#         self.top.focus_set() # Hide highlight border
#         self.canvas.delete(self.dndid)
#         self.dndid = None
#
#     def dnd_commit(self, source, event):
#         self.dnd_leave(source, event)
#         x, y = source.where(self.canvas, event)
#         source.attach(self.canvas, x, y)
