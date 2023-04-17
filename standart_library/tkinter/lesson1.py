# ВВедение в tkinter. Главное окно

import tkinter as tk

window = tk.Tk()

window.config(background='blue')

window.title('Первое графическое приложение')

photo = tk.PhotoImage(file='icons/cat.png')
window.iconphoto(False, photo)


window.geometry('500x600+600+200') 
# 500x600 - размер окна в пикселях, +600 - отступ от левого края экрана
# +200 - отступ отверхнего края экрана

window.resizable(True, True) # первый параметр - изменяемость по ширине, 2-ой - по высоте

window.minsize(300, 400) # мин размер окна
window.maxsize(700, 800) # макс размер окна

window.mainloop()