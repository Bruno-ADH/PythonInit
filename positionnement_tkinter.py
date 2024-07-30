#coding:utf-8
import tkinter
import os
os.system("cls")

app = tkinter.Tk()
app.geometry("640x480")
app.title("Positionnement widget")

mainframe = tkinter.LabelFrame(app, text="Titre")
mainframe.pack()

label_gender = tkinter.Label(app, text = "Un label")
ent = tkinter.Entry(app)
btn = tkinter.Button(app, text="Welcome")

label_gender.pack()
ent.pack()
btn.pack(ipadx=100, ipady=50)
app.mainloop()