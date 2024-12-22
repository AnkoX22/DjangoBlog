from tkinter import *
from tkinter import ttk
import math

master = Tk()
master.geometry("350x220")
master.title("Simple Calculator")

buttonFrame = Frame(master)
buttonFrame.pack(side=BOTTOM)

display_frame = Frame(master)
display_frame.pack()

user_input = StringVar()

# create constants for interface
h = 3
w = 5
px = 2
py = 2

# the display entry for the input
display = ttk.Entry(display_frame, textvariable=user_input)
display.pack(ipady=3)
display.config(state='readonly')


# updating the display
def update_display(value):
    display.config(state='normal')
    display.delete(0, END)
    display.insert(0, value)
    display.config(state='readonly')


# command function of clear button
def clear():
    display.config(state='normal')
    display.delete(0, END)
    display.config(state='readonly')


# command function for c button
def c(event=None):
    display.config(state='normal')
    display.delete(len(display.get())-1, len(display.get()))
    display.config(state='readonly')


# command function for ce button
def ce():
    last_numeric = display.get()
    if last_numeric.isnumeric():
        clear()
    else:
        i = 1
        while ('/' in last_numeric) | ('*' in last_numeric) | ('+' in last_numeric) | ('-' in last_numeric):
            last_numeric = last_numeric[1:]
            i += 1
        display.config(state='normal')
        display.delete(i-1, END)
        display.config(state='readonly')


# command function for equal button
def equal(event=None):
    try:
        y = str(eval(display.get()))
        display.delete(0, END)
        update_display(y)
    except EXCEPTION:
        update_display("Error, not valid input")


# command function for the 2nd power button
def power2():
    try:
        y = str(pow(float(eval(display.get())), 2))
        update_display(y)
    except EXCEPTION:
        update_display("Error, the number under the root cannot be negative")


# command function for inverse function
def inverse():
    try:
        y = str(1/float(display.get()))
        update_display(y)
    except ZeroDivisionError:
        update_display("Error, you cannot divide with zero")


# command function for sqrt button
def square_root():
    float_input = float(eval(display.get()))
    try:
        y = str(math.sqrt(float_input))
        update_display(y)
    except EXCEPTION:
        update_display("Error, the number cannot be negative")


# command function for reverse button
def reverse():
    try:
        y = str(-float(display.get()))
        update_display(y)
    except EXCEPTION:
        update_display("Error")


# command function to insert in display the numbers of the pressed buttons
def on_click(name):
    current_text = display.get() + name
    update_display(current_text)


def per_cent():
    try:
        y = str(float(display.get())/100.0)
        update_display(y)
    except EXCEPTION:
        update_display("0")


def create_button(frame, input_text, input_command, input_row, input_column, pad_x, pad_y):
    new_button = ttk.Button(frame, text=input_text, command=input_command)
    new_button.grid(row=input_row, column=input_column, padx=pad_x, pady=pad_y)
    master.grid_rowconfigure(input_row, weight=1)
    master.grid_columnconfigure(input_column, weight=1)
    return new_button


master.bind('<Return>', equal)
master.bind('=', equal)
master.bind('<BackSpace>', c)

for num in range(10):
    master.bind(str(num), lambda event, n=num: on_click(str(n)))

arithmetic_operations = ['+', '-', '/', '*', '(', ')']


for operator in arithmetic_operations:
    master.bind(operator, lambda event, op=operator: on_click(op))


buttons = [
    {'text': '%', 'command': per_cent, 'row': 1, 'column': 1},
    {'text': 'CE', 'command': ce, 'row': 1, 'column': 2},
    {'text': 'C', 'command': c, 'row': 1, 'column': 3},
    {'text': 'Delete', 'command': clear, 'row': 1, 'column': 4},
    {'text': '1/x', 'command': inverse, 'row': 2, 'column': 1},
    {'text': '^2', 'command': power2, 'row': 2, 'column': 2},
    {'text': 'sqrt()', 'command': square_root, 'row': 2, 'column': 3},
    {'text': '/', 'command': lambda: on_click('/'), 'row': 2, 'column': 4},
    {'text': '7', 'command': lambda: on_click('7'), 'row': 3, 'column': 1},
    {'text': '8', 'command': lambda: on_click('8'), 'row': 3, 'column': 2},
    {'text': '9', 'command': lambda: on_click('9'), 'row': 3, 'column': 3},
    {'text': '*', 'command': lambda: on_click('*'), 'row': 3, 'column': 4},
    {'text': '4', 'command': lambda: on_click('4'), 'row': 4, 'column': 1},
    {'text': '5', 'command': lambda: on_click('5'), 'row': 4, 'column': 2},
    {'text': '6', 'command': lambda: on_click('6'), 'row': 4, 'column': 3},
    {'text': '-', 'command': lambda: on_click('-'), 'row': 4, 'column': 4},
    {'text': '1', 'command': lambda: on_click('1'), 'row': 5, 'column': 1},
    {'text': '2', 'command': lambda: on_click('2'), 'row': 5, 'column': 2},
    {'text': '3', 'command': lambda: on_click('3'), 'row': 5, 'column': 3},
    {'text': '+', 'command': lambda: on_click('+'), 'row': 5, 'column': 4},
    {'text': '+/-', 'command': reverse, 'row': 6, 'column': 1},
    {'text': '0', 'command': lambda: on_click('0'), 'row': 6, 'column': 2},
    {'text': '.', 'command': lambda: on_click('.'), 'row': 6, 'column': 3},
    {'text': '=', 'command': equal, 'row': 6, 'column': 4},
]

for button in buttons:
    create_button(buttonFrame, button['text'], button['command'], button['row'], button['column'], px, py)


# run interface
master.mainloop()
