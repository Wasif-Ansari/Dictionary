from PyDictionary import PyDictionary
from tkinter import *


root = Tk()
root.title("DICTIONARY")
root.geometry('610x500')

entry = Entry(root,font=("Times New Roman", 15, "bold"))
entry.grid(row=1,column=2)
entry.place(x=10,y=10,width=600)

buttons = Button(root , text="FIND MEANING")
buttons.grid(row=4 , column=2)
buttons.place(x=225,y=45,width=150)

means = Label(root,text="None",font=("Times New Roman",10,"bold" ),bg="white",fg="blue",wraplength=300, justify="center")
means.place(x=10,y=100,height=200,width=600)

root.mainloop()