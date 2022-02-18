import parser
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
root = tk.Tk()
root.title("Borch News")
root.geometry("500x750")
combo = Combobox()
combo["values"]= (parser.rubriks_name)
combo.current(1) #Элемент выбранный по умолчанию
combo.grid(column=0, row=0)

root.mainloop()
