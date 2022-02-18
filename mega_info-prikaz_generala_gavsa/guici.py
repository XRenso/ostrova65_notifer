from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
from calendar import month_name
import parser
root = Tk()

# config the root window
root.geometry('500x750')
root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="Please select a month:")
label.pack(fill=X, padx=5, pady=5)

# create a combobox
selected_month = StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# get first 3 letters of every month name
# for i in parser.rubriks_name:
month_cb['values'] = parser.rubriks_name 

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=X, padx=5, pady=5)

label = Label(text = "hello nigger").pack()
parser.get_news_from_topics(parser.get_urls_from_topic('Здравоохранение'))
print(parser.topics_title[0])
# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    text12 = selected_month.get()
    print(text12)
    if text12 == "Здравоохранение":

        #parser.get_news_from_topics(parser.get_urls_from_topic('Здравоохранение'))
        #parser.get_news_from_topics(parser.get_urls_from_topic('Здравоохранение'))
        print(parser.topics_title[0])   
    

month_cb.bind('<<ComboboxSelected>>', month_changed)

root.mainloop()