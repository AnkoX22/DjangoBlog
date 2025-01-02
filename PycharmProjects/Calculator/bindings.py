from operations import *
from display import *


def set_up_bindings(master, display):
    master.bind('<Return>', lambda event: equal(display))
    master.bind('=', lambda event: equal(display))
    master.bind('<BackSpace>', lambda event: c(display))

    for num in range(10):
        master.bind(str(num), lambda event, n=num: on_click(str(n), display))

    arithmetic_operations = ['+', '-', '/', '*', '(', ')']

    for operator in arithmetic_operations:
        master.bind(operator, lambda event, op=operator: on_click(op, display))
