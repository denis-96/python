# Виджет  Button

import tkinter as tk
from random import choice


count = 0
btn1_count = 0


def disable_all_btns():
    global btn1_count
    btn1_count += 1
    if btn1_count % 2:
        for btn in (btn2, btn3, btn4):
            btn['state'] = tk.DISABLED
    else: 
        for btn in (btn2, btn3, btn4):
            btn['state'] = tk.NORMAL
            

def counter():
    global count
    count += 1
    btn4['text'] = f'Счётчик: {count}'


window = tk.Tk()
window.geometry('300x400+100+200')
window.title('Урок 3')

btn1 = tk.Button(window, text='disable all',
                 command=disable_all_btns
                 )
btn1.pack()

btn2 = tk.Button(window, text='random color',
                 command=lambda: window.config(background=choice(('red', 'green', 'blue', 'yellow')))
                 )
btn2.pack()

btn3 = tk.Button(window, text='button 3',
                 command=lambda: tk.Label(window, text='hi').pack()
                 )
btn3.pack()


btn4 = tk.Button(window, text=f'Счётчик: {count}',
                 command=counter,
                 activebackground='blue',
                 bg='red',
                 state=tk.NORMAL
                 )
btn4.pack()

window.mainloop()