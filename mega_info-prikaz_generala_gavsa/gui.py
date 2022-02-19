
from tkinter import ttk
from tkinter import *
import tkinter.font as font
import parser
import webbrowser
import user_profile as us_prof
import os.path
import time








def main(extermenatus, sasati, anus_sani):
    if extermenatus != None and sasati != None and anus_sani != None:
        extermenatus.destroy()
        #print(sasati)
        #print([k for k, v in Counter(sasati).items() if v % 2 != 0])
        us_prof.save_user_interest(anus_sani, *sasati)

    root = Tk()
    root.geometry('600x750')
    root.resizable(False, False)
    root.title('Borch News')
    canvas = Canvas(root, bd=0, highlightthickness=0)
    label = Label(root,text="Выберите топик:")
    label.pack()
    scrollbar = Scrollbar(canvas, orient=VERTICAL)
    canvas.configure(yscrollcommand=scrollbar.set)
    selected_topik = StringVar()
    selected_vib = StringVar()
    topik = ttk.Combobox(root, textvariable=selected_topik)
    vib = ttk.Combobox(root, textvariable=selected_vib)
    thanks = ["Моя подборочка, родненькая"]
    def click(url):
        webbrowser.open(url, new=2)
    vib['values'] = ["Рубрики", "Города", "Свой Борщ"]
    text1= selected_vib.get()
    if text1 == "Рубрики":
        topik['values'] = parser.rubriks_name
        topik.pack()
    elif text1 == "Города":
        topik['values'] = parser.city_names
        topik.pack()
    elif text1 == "Свой Борщ":
        print('da')
        topik['values'] = thanks
        topik.pack()
        




    def open_news(title,url):
        myFont = font.Font(family='Helvetica', size=10)
        news = Toplevel(root)
        btn = Button(news, text= "Источник - " + url, command=lambda :click(url), width=50)
        btn.pack(side = BOTTOM,fill = X)
        news.title(title)
        news.geometry("900x700")
        news.resizable(False, False)
        text = Text(news, width = 900, height = 400)
        Scrollbar1 = Scrollbar(news, orient = VERTICAL, command=text.yview)
        Scrollbar1.pack(side=RIGHT, fill=Y)
        parser.get_topic_descript_sakh(url)
        desc = parser.topic_desk
        for i in desc:
            text.insert(1.0, i + ' \n')
            text['font'] = myFont
            text.pack()




    vib.pack(padx=0, pady=0)
    topik.pack(padx = 0,  pady  = 0)


    news_btn_list=[]
    class btn_news:
        def __init__(self,text,url):
            self.font = font.Font(family='Helvetica', size=10)
            self.text = text
            self.url = url
            self.button = Button(canvas, text=self.text, wraplength=400, width=50, command=lambda: open_news(self.text, self.url))
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
        #print(text12)
        root.title('Borch News - ' + text12)
        if text12 != 'Моя подборочка, родненькая':
            parser.get_news_from_topics(parser.get_urls_from_topic(text12))
        elif text12 == 'Моя подборочка, родненькая':
            parser.create_user_news()


       
    #label.configure(text = parser.topics_title[0])
    #label1.configure(text = parser.topics_url[0])
        scrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        if text12 != 'Моя подборочка, родненькая':
            for i in parser.topics_title:

                l = btn_news(i,parser.topics_url[parser.topics_title.index(i)])
                news_btn_list.append(l)
        elif text12 == 'Моя подборочка, родненькая':
            for i in parser.personal_title:
                l = btn_news(i, parser.personal_url[parser.personal_title.index(i)])
                news_btn_list.append(l)

    def clear_news_buttons():
        for i in news_btn_list:
            i.destroy()


    def vib_changed(event):
        text1= selected_vib.get()
        if text1 == "Рубрики":
            topik['values'] = parser.rubriks_name
        elif text1 == "Города":
            topik['values'] = parser.city_names
        elif text1 == "Свой Борщ":
            topik['values'] = thanks

    topik.bind('<<ComboboxSelected>>', topik_changed)
    vib.bind('<<ComboboxSelected>>', vib_changed)
    label.pack()
    canvas.place()
    canvas.pack(fill=BOTH)
    root.mainloop()
    
if os.path.exists('config.txt'):
   main(None, None, None)
    
else:
    start = Tk()
    to_send = []
    start.title("Добро пожаловать!")
    startlabel = Label(start, text = "Добро пожаловать! Выберите интересуюшую вас категории:").pack()
    combobox = ttk.Combobox(start)    
    combobox['values'] = parser.city_names
    combobox.pack()    
    checkers =[]
    def add_text(text):
        to_send.append(text)
    class chkbtn():
        def __init__(self,text, index, varsa) -> None:
            self.text = text
            self.index = index
            self.button = Checkbutton(start, text = self.text, variable = varsa,command=lambda:add_text(self.text)).pack()
        def get_text(self):
            return self.text
        def get_butt(self):
            return self.button
        def cget(self,type):
            return self.button.get(type)
    for i in parser.rubriks_name:
        vars = IntVar()
        chkb = chkbtn(text=i, index=parser.rubriks_name.index(i), varsa= vars)
        checkers.append(chkb)
    butt = Button(start, text = "продолжить",command = lambda: main(start,to_send,combobox.get()))
    butt.pack()
    start.mainloop()

   # btn.configure(text=parser.topics_title[0] + '\n' + parser.topics_url[0])






    
    