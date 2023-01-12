# Виджет  CheckButton

import tkinter as tk

lbl_list = []

def select_all():
    for check in [over_18, commercial, follow]:
        check.select()
        
def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()    

def show():
    lbl_list.append(tk.Label(frm, text=f'Флажок 18, {over_18_value.get()}\nФлажок реклама, {commercial_value.get()}\nФлажок подписка, {follow_value.get()}', justify='right'))
    lbl_list[-1].pack()

window = tk.Tk()
window.geometry('374x500+600+200')
window.title('Урок 5')

frm = tk.Frame(window)
frm.pack()

over_18_value = tk.StringVar()
over_18_value.set('No')
commercial_value = tk.BooleanVar()
follow_value = tk.IntVar()

over_18 = tk.Checkbutton(frm, text='Вам исполнилось 18 лет?', variable=over_18_value,
                         offvalue='No', onvalue='Yes')
over_18.pack()

commercial = tk.Checkbutton(frm, text='Хотите получать рекламу?', variable=commercial_value,
                            offvalue=False, onvalue=True)
commercial.pack()

follow = tk.Checkbutton(frm, text='Хотите подписаться на канал?', indicatoron=0,
                        variable=follow_value, offvalue=0, onvalue=1)
follow.pack()


tk.Button(frm, text='Select all', command=select_all).pack()
tk.Button(frm, text='Deselect all', command=deselect_all).pack()
tk.Button(frm, text='Toggle all', command=lambda: [check.toggle() for check in [over_18, commercial, follow]]).pack()
tk.Button(frm, text='Show', command=show).pack()
tk.Button(frm, text='Clear', command=lambda: [lbl.destroy() for lbl in lbl_list]).pack()


window.mainloop()