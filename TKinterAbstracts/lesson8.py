# Виджет Combobox

import tkinter as tk
from tkinter import ttk


def show_day():
    print(combo.get(), combo_int.get())
    
def set_day():
    combo.set('Friday')

weekDays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
list_int = [n+1 for n in range(5)]


window = tk.Tk()
window.geometry('300x400+600+200')
window.title('Урок 7')

combo = ttk.Combobox(window, values=weekDays)
combo.current(3)
combo.pack()

combo_int = ttk.Combobox(window, values=list_int)
combo_int.pack()

ttk.Button(window, text='Show day', command=show_day).pack()
ttk.Button(window, text='Set day', command=set_day).pack()


window.mainloop()