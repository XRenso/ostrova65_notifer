import tkinter

from tkinter import Tk, Frame, Menu

a = input("введи сюда текст быстро ")
window = tk.Tk()
label = tk.Label(text=a)
menubar = Menu(self.parent)
self.parent.config(menu=menubar)
label.pack()
window.geometry("400x650")
window.mainloop()