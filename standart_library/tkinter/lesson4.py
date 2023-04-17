# Метод grid

import tkinter as tk

window = tk.Tk()
window.geometry('345x400+100+200')
window.title('Урок 4')

count = 0
for row in range(3):
    for col in range(3):
        count += 1
        tk.Button(window, text=f'Hello {count}', width=15, height=2).grid(row=row, column=col, sticky='w')


# btn1 = tk.Button(window, text='Hello 1', width=15, height=2)
# btn2 = tk.Button(window, text='Hello 2', width=15, height=2)
# btn3 = tk.Button(window, text='Hello 3', width=15, height=2)
# btn4 = tk.Button(window, text='Hello 4', width=15, height=2)
# btn5 = tk.Button(window, text='Hello 5', width=15, height=2)
# btn6 = tk.Button(window, text='Hello 6', width=15, height=2)
# btn7 = tk.Button(window, text='Hello 7', width=15, height=2)
# btn8 = tk.Button(window, text='Hello 8', width=15, height=2)

# btn1.grid(row=0, column=0, sticky='we')
# btn2.grid(row=0, column=1)
# btn3.grid(row=0, column=2)
# btn4.grid(row=1, column=0, sticky='we')
# btn5.grid(row=1, column=1)
# btn6.grid(row=1, column=2)
# btn7.grid(row=2, column=0, columnspan=3, sticky='we')
# btn8.grid(row=0, column=3, rowspan=3, sticky='ns')

window.grid_columnconfigure(0, minsize=150)
window.grid_columnconfigure(1, minsize=150)
window.grid_columnconfigure(2, minsize=150)
window.mainloop()