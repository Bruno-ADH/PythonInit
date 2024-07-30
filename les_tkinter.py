#coding:utf-8
import tkinter
import os
os.system("cls")

mainapp = tkinter.Tk()
mainapp.title("Le Programme")
# mainapp.minsize(400, 390)
# mainapp.maxsize(800, 700)

windows_x = 400
windows_y = 360
screen_x = mainapp.winfo_screenwidth()
screen_x = (screen_x // 2) - (windows_x // 2)
print(screen_x)

screen_y = mainapp.winfo_screenheight()
screen_y = (screen_y // 2) - (windows_y // 2)
# screen_y = int(screen_y)

geo = "{}x{}+{}+{}".format(windows_x,windows_y,screen_x,screen_y)

mainapp.geometry(geo)

mainapp.mainloop()

