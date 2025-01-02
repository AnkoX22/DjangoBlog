from display import update_display, EXCEPTION, END
import math


def per_cent(display):
    try:
        y = str(float(display.get())/100.0)
        update_display(y, display)
    except EXCEPTION:
        update_display("0", display)


# command function for reverse button
def reverse(display):
    try:
        y = str(-float(display.get()))
        update_display(y, display)
    except EXCEPTION:
        update_display("Error", display)


# command function for sqrt button
def square_root(display):
    float_input = float(eval(display.get()))
    try:
        y = str(math.sqrt(float_input))
        update_display(y, display)
    except EXCEPTION:
        update_display("Error, the number cannot be negative", display)


# command function for inverse function
def inverse(display):
    try:
        y = str(1/float(display.get()))
        update_display(y)
    except ZeroDivisionError:
        update_display("Error, you cannot divide with zero", display)


# command function for the 2nd power button
def power2(display):
    try:
        y = str(pow(float(eval(display.get())), 2))
        update_display(y, display)
    except EXCEPTION:
        update_display("Error, the number under the root cannot be negative", display)


# command function for equal button
def equal(display, event=None):
    try:
        y = str(eval(display.get()))
        display.delete(0, END)
        update_display(y, display)
    except EXCEPTION:
        update_display("Error, not valid input", display)


# command function for ce button
def ce(display):
    last_numeric = display.get()
    if last_numeric.isnumeric():
        clear(display)
    else:
        i = 1
        while ('/' in last_numeric) | ('*' in last_numeric) | ('+' in last_numeric) | ('-' in last_numeric):
            last_numeric = last_numeric[1:]
            i += 1
        display.config(state='normal')
        display.delete(i-1, END)
        display.config(state='readonly')


# command function for c button
def c(display, event=None):
    display.config(state='normal')
    display.delete(len(display.get())-1, len(display.get()))
    display.config(state='readonly')


# command function of clear button
def clear(display):
    display.config(state='normal')
    display.delete(0, END)
    display.config(state='readonly')

