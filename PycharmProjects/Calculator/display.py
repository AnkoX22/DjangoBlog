from tkinter import ttk
from tkinter import *

style = ttk.Style()


# the display entry for the input
def create_display(display_frame, user_input):
    scroll_bar = Scrollbar(display_frame, orient='horizontal')
    display = ttk.Entry(display_frame, textvariable=user_input, xscrollcommand=scroll_bar.set, font=('sans serif', 13))
    display.focus()
    display.grid(row=2, column=0, columnspan=4, padx=3, pady=3, sticky='nsew')
    display.config(state='readonly')
    scroll_bar.grid(row=3, column=0, columnspan=4, padx=3, pady=3, sticky='nsew')
    scroll_bar.config(command=display.xview)
    display_frame.grid_rowconfigure(0, weight=3)
    display_frame.grid_columnconfigure(0, weight=1)
    display_frame.grid_rowconfigure(1, weight=0)
    display_frame.grid_columnconfigure(1, weight=1)
    display_frame.grid_rowconfigure(2, weight=3)
    display_frame.grid_columnconfigure(2, weight=2)
    display_frame.grid_rowconfigure(3, weight=0)
    display_frame.grid_columnconfigure(3, weight=1)
    return display


# updating the display
def update_display(value, display):
    display.config(state='normal')
    display.delete(0, END)
    display.insert(0, value)
    display.config(state='readonly')


# command function to insert in display the numbers of the pressed buttons
def on_click(name, display, event=None):
    current_text = display.get() + name
    update_display(current_text, display)


# def change_theme(event, display, theme):
#     display.config({"background": 'black'}, foreground='white')
#
#     # handle combobox changes
#     theme.bind('<<ComboboxSelected>>', change_theme)


# def change_color(display, color):
#     if color == 'black':
#         display_color = color
#         bg_color = 'white'
#     else:
#         display_color = color
#         bg_color = 'black'
#     style.configure('Entry', background=display_color, foreground=bg_color)
