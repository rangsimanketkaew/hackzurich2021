from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import io
import cairosvg

def loadimgurl_svg(imgurl):
    raw_data = cairosvg.svg2png(url=imgurl)
    # raw_data = urllib.request.urlopen(imgurl).read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image

def loadimgurl(imgurl):
    raw_data = urllib.request.urlopen(imgurl).read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image

root = Tk()

myurl = "https://image.migros.ch/original/abb4b97a2571bff7f68e554bdcc630ffbef18d57.svg"
# myurl = "https://image.migros.ch/original/7d8431afdd3f163932da1e3b874e7764940e4494/v-vegetarisch.jpg"

# imgtab1 = loadimgurl(myurl)
imgtab1 = loadimgurl_svg(myurl)
label = Label( root, image=imgtab1)
label.grid()
root.mainloop()