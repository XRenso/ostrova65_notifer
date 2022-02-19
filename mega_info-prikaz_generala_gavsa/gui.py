import random
from tkinter import ttk
from tkinter import *
import tkinter.font as font

import parser
import webbrowser
import user_profile as us_prof
import os.path



def main(extermenatus, sasati, anus_sani):
    if extermenatus != None and sasati != None and anus_sani != None:
        extermenatus.destroy()
        us_prof.save_user_interest(anus_sani, *sasati)

    root = Tk()
    root.geometry('300x250')
    root.resizable(False,  False)
    root.title('Borch News')
    root.focus_set()
    label = Label(root,text="Выберите топик:")
    label.pack()
    main_frame = Frame(root, width = 370, height= 700)
    main_frame.place(x=0,y=0)
    my_canvas = Canvas(main_frame, width = 370, height= 700)
    my_canvas.place(x=0,y=0)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.place(x=370,y=0,height=700)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))
    def _on_mouse_wheel(event):
        my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
    my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
    second_frame = Frame(my_canvas, width = 370, height = 700)
    second_frame.place(x=0,y=0)
    my_canvas.create_window((0,0), window = second_frame, anchor="nw")
    selected_topik = StringVar()
    selected_vib = StringVar()
    topik = ttk.Combobox(root, textvariable=selected_topik, state="readonly")
    vib = ttk.Combobox(root, textvariable=selected_vib, state="readonly")
    thanks = ["Моя подборка"]
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
        symbols = 0
        speed_reading_minute = 1400
        myFont = font.Font(family='Helvetica', size=10)
        news = Toplevel(root)
        news.focus_set()
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
            text.tag_add(i, '1.0','1.end' )
            text.tag_config(i,font=("Helvetica", 10))
            text.insert(1.0, i + ' \n')
            text.pack()
            for a in i:
                symbols += len(a)
        skorost = round(symbols/speed_reading_minute)
        if skorost > 0:
            time_for_read_pribliz = f"\n\n\nПримерное время чтения {skorost} минут/ы/а"
        else:
            time_for_read_pribliz = f"\n\n\nВремя чтения не займет у вас и минуты"

        for i in time_for_read_pribliz:
            text.insert(END,i)
            text.tag_add(time_for_read_pribliz, 2.0)
            text.tag_config(i,font=("Arial", 10, 'italic'))



        text.config(state=DISABLED)
        news.title(title + f" !!Символов : {str(symbols)}!!")




    vib.pack(pady=5)
    topik.pack(pady=5)


    news_btn_list=[]
    class btn_news:
        def __init__(self,text,url):
            self.font = font.Font(family='Helvetica', size=10)
            self.text = text
            self.url = url
            self.button = Button(second_frame, text=self.text, wraplength=350, width=50, command=lambda: open_news(self.text, self.url), relief = GROOVE)
            self.button.pack(fill=X)
            second_frame.configure(height=0)
            root.geometry('360x700')
        def get_text(self):
            return self.text
        def get_url(self):
            return self.url
        def destroy(self):
            self.button.destroy()

    def topik_changed(event):
        clear_news_buttons()
        text12 = selected_topik.get()

        root.title('Borch News - ' + text12)
        if text12 != 'Моя подборка':
            parser.get_news_from_topics(parser.get_urls_from_topic(text12))
        elif text12 == 'Моя подборка':
            try:
                temp = list(zip(parser.personal_url,parser.personal_title))
                random.shuffle(temp)
                new_pers_urls, new_pers_titles = list(zip(*temp))
                parser.personal_url = new_pers_urls
                parser.personal_title = new_pers_titles
            except ValueError:
                pass
        if text12 != 'Моя подборка':
            for i in range(20):

                l = btn_news(parser.topics_title[i],parser.topics_url[i])
                news_btn_list.append(l)
        elif text12 == 'Моя подборка':
            for i in range(20):
                try:
                    l = btn_news(parser.personal_title[i], parser.personal_url[i])
                    news_btn_list.append(l)
                except IndexError:
                    parser.create_user_news()

            temp = list(zip(parser.personal_url, parser.personal_title))
            random.shuffle(temp)
            new_pers_urls, new_pers_titles = list(zip(*temp))
            parser.personal_url = new_pers_urls
            parser.personal_title = new_pers_titles
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
    main_frame.pack(fill = BOTH, expand=1)
    my_canvas.pack(side = LEFT, fill = BOTH, expand=1)
    my_scrollbar.pack(side=RIGHT, fill = Y)
    
    root.mainloop()
    
if os.path.exists('config.txt'):
   main(None, None, None)
    
else:
    start = Tk()
    to_send = []
    start.title("Добро пожаловать!")
    start.geometry('280x650')
    start.resizable(False,False)
    start.focus_set()
    startlabel = Label(start, text = "Выберите интересуюшую вас категории:").pack()
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
    butt = Button(start, text = "продолжить",relief = SUNKEN,command = lambda: main(start,to_send,combobox.get()))
    butt.pack(side = BOTTOM, fill = X)
    start.mainloop()
