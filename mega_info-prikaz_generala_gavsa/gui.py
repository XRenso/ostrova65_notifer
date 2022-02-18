from lib2to3.pgen2.token import LEFTSHIFT
from operator import ne
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from turtle import width
import parser
import webbrowser
root = Tk()

root.geometry('600x750')
root.resizable(False, False)
root.title('Borch News')
all_in_one =[]
label = ttk.Label(text="Выбери топик:")
label.pack()


selected_topik = StringVar()
selected_vib = StringVar()
topik = ttk.Combobox(root, textvariable=selected_topik)
vib = ttk.Combobox(root, textvariable=selected_vib)
def click():
    webbrowser.open(parser.topics_url[0], new=2)
vib['values'] = ["Рубрики", "Города"]
text1= selected_vib.get()
if text1 == "Рубрики":
    for i in parser.rubriks_name:
        topik['values'] = i
elif text1 == "Города":
    topik['values'] = parser.city_names


    


btn = Button(root, text="открыть ссылку", command=click, width = 50) 
vib.pack(padx=0, pady=0)
topik.pack(padx = 0,  pady  = 0)
label = Label(text="привет!")
label.place(relx = .2 , rely = .2)
label1 = Label(text = "")
label1.place(relx = .2 , rely = .2)

def topik_changed(event):
    text12 = selected_topik.get()
    print(text12)
    root.title('Borch News - ' + text12)
    parser.get_news_from_topics(parser.get_urls_from_topic(text12))
    print(parser.topics_title[0])   
    label.configure(text = parser.topics_title[0])
    label1.configure(text = parser.topics_url[0])
    btn.configure(text=parser.topics_title[0] + '\n' + parser.topics_url[0])
def vib_changed(event):
    text1= selected_vib.get()
    if text1 == "Рубрики":
        topik['values'] = parser.rubriks_name
    elif text1 == "Города":
        topik['values'] = parser.city_names

topik.bind('<<ComboboxSelected>>', topik_changed)
vib.bind('<<ComboboxSelected>>', vib_changed)
label.pack()
label1.pack()
btn.place( relx = 0.1 , rely =0.22)
btn.pack(side = BOTTOM,fill = X)
root.mainloop()