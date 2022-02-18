from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from turtle import width
import parser
import webbrowser
root = Tk()

root.geometry('500x750')
root.title('Borch News')
all_in_one =[]
label = ttk.Label(text="Выбери топик:")
label.grid(column = 0, row = 0)
label.pack()


selected_month = StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

def click():
    webbrowser.open(parser.topics_url[0], new=2)
for i in parser.rubriks_name:
    all_in_one.append(i)
for i in parser.city_names:
    all_in_one.append(i)
month_cb['values'] = all_in_one
btn = Button(root, text="открыть ссылку", command=click, width = 55)
btn.place(relx = 0.1, rely = 0.1)  
month_cb.pack()
label = Label(text="привет!")
label.place(relx = 0.2 , rely = 0.2)
label1 = Label(text = "")
label1.place(relx = 0.2 , rely = 0.2)

def month_changed(event):
    text12 = selected_month.get()
    print(text12)
    parser.get_news_from_topics(parser.get_urls_from_topic(text12))
    print(parser.topics_title[0])   
    label.configure(text = parser.topics_title[0])
    label1.configure(text = parser.topics_url[0])
    

month_cb.bind('<<ComboboxSelected>>', month_changed)
label.pack()
label1.pack()
root.mainloop()