import tkinter as tk
from tkinter import messagebox

def add_digit(digit):
    value = entry_field.get()
    if value == '0':
        entry_field.delete(0)
    entry_field.insert('end', digit)

def add_operation(operation):
    value = entry_field.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    try:
        result = eval(value)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание!', 'На ноль делить нельзя!')
        clear()
        return None
    entry_field.delete(0, 'end')
    entry_field.insert('end', str(result) + operation)

def calculate():
    expression = entry_field.get()
    entry_field.delete(0, 'end')
    try:
        result = eval(expression)
    except SyntaxError:
        result = '0'
        messagebox.showinfo('Внимание!', "Выражение не может заканчиваться знаком!")
    except ZeroDivisionError:
        result = '0'
        messagebox.showinfo('Внимание!', 'На ноль делить нельзя!')
    entry_field.insert(0, result)
        

def clear():
    entry_field.delete(0, 'end')
    entry_field.insert(0, '0')
    
def keyboard_input(event: tk.Event):
    value = event.char
    # print(repr(value))
    if value.isdigit():
        add_digit(value)
    elif value in '-+/*':
        add_operation(value)
    elif value == '\x08' and len(entry_field.get()) < 1:
        entry_field.insert(0, '0')
    elif value == '\r':
        calculate()
    
def make_digit_btn(digit):
    return tk.Button(window, text=digit, bd=0, bg='white', font=('Sabril', 20), command=lambda: add_digit(digit))
def make_operation_btn(operation):
    return tk.Button(window, text=operation, bd=0, bg='white', font=('Sabril', 20, 'bold'), command=lambda: add_operation(operation))


window = tk.Tk()
window.geometry('280x350+600+200')
window.title('Калькулятор')
window.config(bg='#F4F6F6')
window.resizable(False, False)

photo = tk.PhotoImage(file='icons/calc.png')
window.iconphoto(False, photo)

window.bind('<Key>', keyboard_input)

for i in range(4):
    window.grid_columnconfigure(i, minsize='70')
    window.grid_rowconfigure(i, minsize='70')
window.grid_rowconfigure(4, minsize='70')
    
entry_field = tk.Entry(window, relief=tk.FLAT, bg='white', font=('Sabril', 16), justify='right')
entry_field.grid(row=0, column=0, columnspan=4, sticky='wens', padx=6, pady=8)
clear()
entry_field.icursor(1)

for row in range(3):
    for col in range(3):
        make_digit_btn(col+7-3*row).grid(row=row+1, column=col, sticky='wens', padx=5, pady=5)
make_digit_btn('0').grid(row=4, column=0, sticky='wens', padx=5, pady=5)

for row, operation in enumerate('/*-+'):
    make_operation_btn(operation).grid(row=row+1, column=3, sticky='wens', padx=5, pady=5)
    
tk.Button(window, text='C', bd=0, bg='white', font=('Sabril', 20), command=clear).grid(row=4, column=1, sticky='wens', padx=5, pady=5)
tk.Button(window, text='=', bd=0, bg='white', font=('Sabril', 20), command=calculate).grid(row=4, column=2, sticky='wens', padx=5, pady=5)


window.mainloop()