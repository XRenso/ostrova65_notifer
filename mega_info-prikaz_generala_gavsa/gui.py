
from tkinter import ttk
from tkinter import *
import tkinter.font as font
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
def click(url):
    webbrowser.open(url, new=2)
vib['values'] = ["Рубрики", "Города"]
text1= selected_vib.get()
if text1 == "Рубрики":
    for i in parser.rubriks_name:
        topik['values'] = i
elif text1 == "Города":
    topik['values'] = parser.city_names



def open_news(title,url):
    myFont = font.Font(family='Helvetica', size=10)
    news = Toplevel(root)
    btn = Button(news, text="Перейти к источнику", command=lambda :click(url), width=50)
    btn.pack(side = BOTTOM,fill = X)
    news.title(title)
    news.geometry("800x700")
    news.resizable(False, False)
    parser.get_topic_descript_sakh(url)
    desc = parser.topic_desk
    for i in desc:
        label = Label(news,text=i,wraplength=800,width=800)
        label['font'] = myFont
        label.pack()

    source = Label(news,text='\n\n' +'Источник -' + url,wraplength=800,width=50)
    source.pack()
#btn = Button(root, text="открыть ссылку", command=click, width = 50)
vib.pack(padx=0, pady=0)
topik.pack(padx = 0,  pady  = 0)
label = Label(text="привет!")
label.place(relx = .2 , rely = .2)
label1 = Label(text = "")
label1.place(relx = .2 , rely = .2)

news_btn_list=[]

class btn_news:
    def __init__(self,text,url,desc=['213','123123']):

        self.text = text
        self.url = url
        self.desc = []
        self.desc = desc
        self.button = Button(root, text=self.text, wraplength=600, width=50, command=lambda: open_news(self.text, self.url))
        self.button.pack(fill=X)

    def get_text(self):
        return self.text
    def get_url(self):
        return self.url
    def destroy(self):
        self.button.destroy()


def topik_changed(event):
    clear_news_buttons()
    text12 = selected_topik.get()
    print(text12)
    root.title('Borch News - ' + text12)
    parser.get_news_from_topics(parser.get_urls_from_topic(text12))
    print(parser.topics_title[0])
    #label.configure(text = parser.topics_title[0])
    #label1.configure(text = parser.topics_url[0])

    for i in parser.topics_title:

        l = btn_news(i,parser.topics_url[parser.topics_title.index(i)])
        news_btn_list.append(l)



   # btn.configure(text=parser.topics_title[0] + '\n' + parser.topics_url[0])







def clear_news_buttons():
    for i in news_btn_list:
        i.destroy()


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
#btn.place( relx = 0.1 , rely =0.22)
#btn.pack(side = BOTTOM,fill = X)
root.mainloop()