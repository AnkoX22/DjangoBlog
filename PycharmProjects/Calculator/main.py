from tkinter import *
from tkinter import ttk
# from pynput.keyboard import Key, Controller
import buttons
import display
import bindings

master = Tk()
master.geometry("500x500")
master.title("Simple Calculator")


user_input = StringVar()
# create constants for interface
h = 3
w = 5
px = 2
py = 2

display_frame = Frame(master)
display_frame.pack(fill='both', expand=True)
label = Label(display_frame, text='My Calculator', font=('sans serif', 15, 'bold'), foreground='black')
label.grid(row=0, column=0, columnspan=10, padx=3, pady=3, sticky='nsew')
theme_label = Label(display_frame, text="Theme:", font=('sans serif', 10))
theme_label.grid(row=1, column=0, columnspan=1, padx=3, pady=3, sticky='nsew')
theme = ttk.Combobox(display_frame, values=["Classic", "Dark"], state='readonly')
theme.current(0)
theme.grid(row=1, column=1, columnspan=1, padx=3, pady=3, sticky='nsew')
button_frame = Frame(master)
button_frame.pack(fill='both', expand=True, side='bottom')

display = display.create_display(display_frame, user_input)
button_list = buttons.create_buttons(button_frame, display, master, px, py)

bindings.set_up_bindings(master, display)


# def change_color(event, button_list, display):
#     buttons.change_color(theme.get(), button_list)
#     # display.change_color(display, theme.get())


# change theme when combo box choice changes
# theme.bind("<<ComboboxSelected>>", lambda event: change_color(button_list, display))


# create shortcut
def create_keyboard_shortcut(value):
    keyboard = Controller()
    keyboard.press(Key.ctrl.value)
    keyboard.press(value)
    keyboard.release(value)


# run interface
master.mainloop()
