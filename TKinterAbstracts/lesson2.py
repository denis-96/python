# Знакомство с виджетами. Виджет Label

import tkinter as tk

window = tk.Tk()
window.geometry('300x400+100+200')
window.title('Урок 2')

label1 = tk.Label(window,
                  text='Hello\nworld',
                  bg='red', # цвет заднего фона
                  fg='white', # цвет текста
                  font=('Arial', 20, 'bold'), # ihban
                  padx=10, # отступ текста от левого о правго края лейбла
                  pady=5, # отступ текста нижнего и верхнего края лейбла
                  width=10, # ширина лейбла
                  height=2, # высота лейбла
                  anchor='c', # расположение текста в лейбле (n-верх, s-низ, w-лево, e-право)
                  # все комбинации n, ne, e, se, s, sw, w, nw, или center
                  relief=tk.GROOVE, # стиль лейбла
                  # flat, groove, raised, ridge, solid, or sunken
                  border=5, # размер обводки (bd)
                  justify=tk.LEFT # центрует или прижимает многострочный текст к границе
                  # left, right, or center
                  )
label1.pack()


window.mainloop()