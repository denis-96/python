# Виджет Radiobutton

import tkinter as tk

window = tk.Tk()
window.geometry('300x400+600+200')
window.title('Урок 7')

levels = {1: 'Easy', 2: 'Middle', 3: 'Hard'}

def select_level():
    level = level_var.get()
    level_text.set(f"Вы выбрали {level} уровень")
    print(levels[level])
    

level_var = tk.IntVar()
level_text = tk.StringVar()

tk.Label(window, text='Выберите уровень сложности').pack()
for level in levels:
    tk.Radiobutton(window, text=levels[level], variable=level_var, value=level, command=select_level).pack()

tk.Label(window, textvariable=level_text).pack()

window.mainloop()