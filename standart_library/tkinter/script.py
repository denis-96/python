import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog

# Create the main window
window = tk.Tk()

# Display the message box when the button is clicked
def show_message_box():
    print(messagebox.showinfo('Title', 'message'))
    

# Create a button to trigger the message box
tk.Button(text="Show Message Box", command=show_message_box).pack()
tk.Button(text="Show Color Chooser", command=lambda: print(colorchooser.askcolor())).pack()
tk.Button(text="Show File Dialog", command=lambda: print(filedialog.askdirectory())).pack()

# Create the label widget
label = tk.Label(window, text="This is a flash message", font=("Helvetica", 16), bg="yellow")

# Display the label for a short time and then remove it
def show_flash_message():
    label.pack()
    window.after(3000, label.pack_forget)


# Create a button to trigger the flash message
button = tk.Button(text="Show Flash Message", command=show_flash_message)
button.pack()



# Create the frames
frame1 = tk.Frame(window, bg="red", width=200, height=200)
frame2 = tk.Frame(window, bg="blue", width=200, height=200)

# Create a function to switch to frame1
def show_frame1():
    frame1.pack()
    frame2.pack_forget()

# Create a button to switch to frame1
button1 = tk.Button(window, text="Show Frame 1", command=show_frame1)
button1.pack()

# Create a function to switch to frame2
def show_frame2():
    frame2.pack()
    frame1.pack_forget()

# Create a button to switch to frame2
button2 = tk.Button(window, text="Show Frame 2", command=show_frame2)
button2.pack()

# Run the main loop
window.mainloop()