# PIL solution
from tkinter import *
from PIL import ImageTk, Image

tkFenster = Tk()

canv = Canvas(master=tkFenster)
canv.place(x=0, y=0, width=750, height=531)

img = ImageTk.PhotoImage(Image.open("https://i.ibb.co/D9TXbyH/a.jpg"))  # <-- PIL
canv.create_image(0, 0, image=img, anchor='nw')

mainloop()