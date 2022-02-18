import tkinter as tk
from tkinter import Tk, Frame, Menu
 
class Example(Frame):
 
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Borch News")
 
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
 
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="МЧС", command=self.onExit)
        fileMenu.add_command(label="Выход", command=self.onExit)
        
        menubar.add_cascade(label="Категории", menu=fileMenu)
 
    def onExit(self):
        self.quit()
 
 
def main():
    root = tk.Tk()
    root.geometry("400x650")
    label = tk.Label(text = "вот здесь твои новости")
    label.pack()
    app = Example()
    root.mainloop()
 
 
if __name__ == '__main__':
    main()

