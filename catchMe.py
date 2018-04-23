from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("Catch me!")

def run(event):
    butt.place(x=random.randint(0,430),y=random.randint(0,470))

butt = Button(root, text="Catch me!")
butt.place(x=random.randint(0,430),y=random.randint(0,470))
butt.bind("<Enter>",run)

root.mainloop()
