from tkinter import *
import tkinter.messagebox
import passGen

window = Tk()

ssidName = StringVar()


def generatePassword():
    tkinter.messagebox.showinfo("Wifi Password", passGen.magic(ssidName.get()))


firstEntry = Entry(textvariable=ssidName)
firstEntry.pack(side=TOP)
firstButton = Button(text="Generate", command=generatePassword)
firstButton.pack(side=BOTTOM)

window.mainloop()
