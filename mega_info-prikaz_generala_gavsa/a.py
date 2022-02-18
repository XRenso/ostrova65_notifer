from re import A
from tkinter import *
import parser

root = Tk()
root.geometry("500x750")
root.title("Borch News")
mainmenu = Menu(root) 
root.config(menu=mainmenu) 
menu = Menu(mainmenu, tearoff=0)
menu2 = Menu(menu, tearoff=0)
menu3 = Menu(menu, tearoff=0)
def num(i):
    global a
    a = i
    print(a)
o = 1
for i in parser.city_names:
    
    menu2.add_radiobutton(label=i, command=num(o))
    o +=1
 
menu.add_cascade(label="Города",menu=menu2)
for i in parser.rubriks_name:
    menu3.add_radiobutton(label=i)

mainmenu.add_cascade(label="Категории",menu=menu)
menu.add_cascade(label="Рубрики",menu=menu3)
menu.add_separator()
menu.add_command(label= "Выход", command = root.quit)
txt = Entry(root,width=40)
txt.grid(column=1, row=0)

parser.get_news_from_topics(parser.get_urls_from_topic(txt.get))
btn = Button(root, text="нажимать!", command=clicked)
label1 = Label(text = parser.topics_title[0]).pack()
label1.grid(column=0, row=0)
label = Label(text = parser.topics_url[0]).pack()
label.grid(column=0, row=1)
print(parser.topics_url[0] + str(parser.topics_title[0]))
root.mainloop() 