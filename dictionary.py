from PyDictionary import PyDictionary
from tkinter import *


root = Tk()
root.title("DICTIONARY")
root.geometry('610x500')

entry = Entry(root,font=("Times New Roman", 15, "bold"))
entry.grid(row=1,column=2)
entry.place(x=10,y=10,width=600)

root.mainloop()