# Виджет Entry

import tkinter as tk

def get_entry():
    name_value = name.get()
    surname_value = surname.get()
    pass_value = password.get()
    if name_value and surname_value and pass_value:
        print(name_value, surname_value, pass_value)
    else:
        print('Не введено имя, фамилия или пароль')

    name.delete(0, 'end')
    surname.delete(0, 'end')
    password.delete(0, 'end')


window = tk.Tk()
window.geometry('374x500+600+200')
window.title('Урок 5')

frame = tk.Frame(window, relief='solid', bd=2, padx=10, pady=10, bg='#212F3C')
frame.grid(row=0, column=0)

frame.grid_columnconfigure(0, minsize=150)
frame.grid_columnconfigure(1, minsize=200)
frame.grid_rowconfigure(0, minsize=50)
frame.grid_rowconfigure(1, minsize=50)
frame.grid_rowconfigure(2, minsize=50)
frame.grid_rowconfigure(3, minsize=50)



tk.Label(frame, text='Name', anchor='w', bg='#212F3C',
         foreground='white', font=('Arial', 13, 'bold')).grid(row=0, column=0,
                                                              sticky='wens')

name = tk.Entry(frame, font=('Arial', 11))
name.grid(row=0, column=1, sticky='wens', pady=10)

tk.Label(frame, text='Surname', anchor='w', bg='#212F3C',
         foreground='white', font=('Arial', 13, 'bold')).grid(row=1, column=0,
                                                              sticky='wens')

surname = tk.Entry(frame, font=('Arial', 11))
surname.grid(row=1, column=1, sticky='wens', pady=10)

tk.Label(frame, text='Password', anchor='w', bg='#212F3C',
         foreground='white', font=('Arial', 13, 'bold')).grid(row=2, column=0,
                                                              sticky='wens')

password = tk.Entry(frame, font=('Arial', 11), show='?')
password.grid(row=2, column=1, sticky='wens', pady=10)

tk.Button(frame, text='Submit', relief='solid', bd=1,
          command=get_entry, font=('Arial', 15, 'bold')).grid(row=3, column=0,
                                                              columnspan=2, sticky='wens', pady=5)
          
tk.Button(frame, text='Insert !', relief='solid', bd=1,
          command=lambda: [i.insert('end', '!') for i in (name, surname)], 
          font=('Arial', 15, 'bold')).grid(row=4, column=0, columnspan=2, sticky='wens', pady=5)



window.mainloop()