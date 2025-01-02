import tkinter
from tkinter import ttk
from display import on_click
from operations import *

# button_list = []

# style = ttk.Style()


def create_buttons(button_f, display, master, px, py):

    button_list = []

    buttons = [
        {'text': '%', 'command': lambda: per_cent(display), 'row': 1, 'column': 1},
        {'text': 'CE', 'command': lambda: ce(display), 'row': 1, 'column': 2},
        {'text': 'C', 'command': lambda: c(display), 'row': 1, 'column': 3},
        {'text': 'Delete', 'command': lambda: clear(display), 'row': 1, 'column': 4},
        {'text': '1/x', 'command': lambda: inverse(display), 'row': 2, 'column': 1},
        {'text': '^2', 'command': lambda: power2(display), 'row': 2, 'column': 2},
        {'text': 'sqrt()', 'command': lambda:  square_root(display), 'row': 2, 'column': 3},
        {'text': '/', 'command': lambda: on_click('/', display), 'row': 2, 'column': 4},
        {'text': '7', 'command': lambda: on_click('7', display), 'row': 3, 'column': 1},
        {'text': '8', 'command': lambda: on_click('8', display), 'row': 3, 'column': 2},
        {'text': '9', 'command': lambda: on_click('9', display), 'row': 3, 'column': 3},
        {'text': '*', 'command': lambda: on_click('*', display), 'row': 3, 'column': 4},
        {'text': '4', 'command': lambda: on_click('4', display), 'row': 4, 'column': 1},
        {'text': '5', 'command': lambda: on_click('5', display), 'row': 4, 'column': 2},
        {'text': '6', 'command': lambda: on_click('6', display), 'row': 4, 'column': 3},
        {'text': '-', 'command': lambda: on_click('-', display), 'row': 4, 'column': 4},
        {'text': '1', 'command': lambda: on_click('1', display), 'row': 5, 'column': 1},
        {'text': '2', 'command': lambda: on_click('2', display), 'row': 5, 'column': 2},
        {'text': '3', 'command': lambda: on_click('3', display), 'row': 5, 'column': 3},
        {'text': '+', 'command': lambda: on_click('+', display), 'row': 5, 'column': 4},
        {'text': '+/-', 'command': lambda: reverse(display), 'row': 6, 'column': 1},
        {'text': '0', 'command': lambda: on_click('0', display), 'row': 6, 'column': 2},
        {'text': '.', 'command': lambda: on_click('.', display), 'row': 6, 'column': 3},
        {'text': '=', 'command': equal, 'row': 6, 'column': 4},
    ]
    for button in buttons:
        button_list.append(create_button(button_f, button['text'], button['command'], button['row'], button['column'], px, py))

    return button_list


def create_button(frame, input_text, input_command, input_row, input_column, pad_x, pad_y):
    new_button = ttk.Button(frame, text=input_text, command=input_command)
    new_button.grid(row=input_row, column=input_column, padx=pad_x, pady=pad_y, sticky="nsew")
    frame.grid_rowconfigure(input_row, weight=1)
    frame.grid_columnconfigure(input_column, weight=1)
    return new_button


# def change_color(theme, button_list):
#
#     if theme.lower() == 'dark':
#         button_color = "black"
#         fg_color = 'white'
#     else:
#         button_color = 'white'
#         fg_color = 'black'
#     style.configure('Custom.TButton', background=button_color, foreground=fg_color)
#     for button in button_list:
#
#         button.configure(style='Custom.TButton')
