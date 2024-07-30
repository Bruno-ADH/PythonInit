#coding: utf-8

import tkinter
from tkinter import messagebox
import os
os.system("cls")

#observateur
def update_label(*args):
    # print("Sexe : {}".format(var_entry.get()))
    if var_entry.get():
        print("C'est un homme")
        var_label.set("C'est un homme")
    else:
        print("C'est une femme")
        var_label.set("C'est une femme")
app = tkinter.Tk()
app.geometry("400x300")
app.title("Variable tkinter")

#widget..
var_entry = tkinter.IntVar()
var_entry.trace("w", update_label)

radio1 = tkinter.Radiobutton(app, text="Homme", value=1, variable=var_entry)
radio2 = tkinter.Radiobutton(app, text="Femme", value=0, variable=var_entry)

var_label = tkinter.StringVar()
label_gender = tkinter.Label(app, textvariable=var_label)

radio1.pack()
radio2.pack()
label_gender.pack()

app.mainloop()