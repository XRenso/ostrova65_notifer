from tkinter import *
import parser
import tkinter as tk
root = tk.Tk()
root.geometry("500x750")
root.title("Borch News")
mainmenu = Menu(root) 
root.config(menu=mainmenu) 
menu = Menu(mainmenu, tearoff=0)
menu2 = Menu(menu, tearoff=0)
menu3 = Menu(menu, tearoff=0)

for i in parser.city_names:
    menu2.add_radiobutton(label=i)
 
menu.add_cascade(label="Города",menu=menu2)
for i in parser.rubriks_name:
    menu3.add_radiobutton(label=i)
 
mainmenu.add_cascade(label="Категории",menu=menu)
menu.add_cascade(label="Рубрики",menu=menu3)
menu.add_separator()
menu.add_command(label= "Выход", command = root.quit)
 
root.mainloop() 

