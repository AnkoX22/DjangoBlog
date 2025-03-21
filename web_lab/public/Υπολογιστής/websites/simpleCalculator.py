import tkinter as tk
from tkinter import Frame
from tkinter import Button
from tkinter import Tk
from tkinter import Pack
from tkinter import Entry
from tkinter import DISABLED
from tkinter import BOTTOM
from math import *

master = Tk()
master.geometry("300x400")
master.title("Simple Calculator")

buttonFrame = Frame(master)
buttonFrame.pack(side=BOTTOM)



displayFrame = Frame(master)
displayFrame.pack()

input = tk.StringVar()

h = 3
w = 5
px = 2
py = 2
num1=0
num2=0

display = Entry(displayFrame,textvariable=input)
display.pack(ipady=3)

def clear():
    display.delete(0, tk.END)


def equal():
    try:
        y = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

def power2():
    try:
        y = str(pow(float(display.get()),2))
        display.delete(0, tk.END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

def inverse():
    try:
        y = str(1/float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

def srt():
    try:
        y = str(sqrt(float(display.get())))
        display.delete(0, tk.END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

def equal():
    try:
        y = str(-float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, y)
    except:
        clear()
        display.insert(0,"Error")

def onClick(name):
    display.insert(tk.END,name)

perCent = Button(buttonFrame,text='%',height=h,width=w,command=lambda: onClick("%"))
perCent.grid(row=1,column=1,padx=px,pady=py)
ce = Button(buttonFrame,text='CE',height=h,width=w,command=lambda: onClick())
ce.grid(row=1,column=2,padx=px,pady=py)
c = Button(buttonFrame,text='C',height=h,width=w,command=lambda: onClick())
c.grid(row=1,column=3,padx=px,pady=py)
delete = Button(buttonFrame,text='delete',height=h,width=w,command=clear)
delete.grid(row=1,column=4,padx=px,pady=py)
inverse = Button(buttonFrame,text='1/x',height=h,width=w,command=inverse)
inverse.grid(row=2,column=1,padx=px,pady=py)
power2 = Button(buttonFrame,text='^2',height=h,width=w,command=power2)
power2.grid(row=2,column=2,padx=px,pady=py)
squareRoot = Button(buttonFrame,text='sqrt()',height=h,width=w,command=srt)
squareRoot.grid(row=2,column=3,padx=px,pady=py)
division = Button(buttonFrame,text='/',height=h,width=w,command=lambda: onClick("/"))
division.grid(row=2,column=4,padx=px,pady=py)
b7 = Button(buttonFrame,text='7',height=h,width=w,command=lambda: onClick("7"))
b7.grid(row=3,column=1,padx=px,pady=py)
b8 = Button(buttonFrame,text='8',height=h,width=w,command=lambda: onClick("8"))
b8.grid(row=3,column=2,padx=px,pady=py)
b9 = Button(buttonFrame,text='9',height=h,width=w,command=lambda: onClick("9"))
b9.grid(row=3,column=3,padx=px,pady=py)
multip = Button(buttonFrame,text='*',height=h,width=w,command=lambda: onClick("*"))
multip.grid(row=3,column=4,padx=px,pady=py)
b4 = Button(buttonFrame,text='4',height=h,width=w,command=lambda: onClick("4"))
b4.grid(row=4,column=1,padx=px,pady=py)
b5 = Button(buttonFrame,text='5',height=h,width=w,command=lambda: onClick("5"))
b5.grid(row=4,column=2,padx=px,pady=py)
b6 = Button(buttonFrame,text='6',height=h,width=w,command=lambda: onClick("6"))
b6.grid(row=4,column=3,padx=px,pady=py)
minus = Button(buttonFrame,text='-',height=h,width=w,command=lambda: onClick("-"))
minus.grid(row=4,column=4,padx=px,pady=py)
b1 = Button(buttonFrame,text='1',height=h,width=w,command=lambda: onClick("1"))
b1.grid(row=5,column=1,padx=px,pady=py)
b2 = Button(buttonFrame,text='2',height=h,width=w,command=lambda: onClick("2"))
b2.grid(row=5,column=2,padx=px,pady=py)
b3 = Button(buttonFrame,text='3',height=h,width=w,command=lambda: onClick("3"))
b3.grid(row=5,column=3,padx=px,pady=py)
plus = Button(buttonFrame,text='+',height=h,width=w,command=lambda: onClick("+"))
plus.grid(row=5,column=4,padx=px,pady=py)
reverse = Button(buttonFrame,text='+/-',height=h,width=w,command=lambda:reverse)
reverse.grid(row=6,column=1,padx=px,pady=py)
b0 = Button(buttonFrame,text='0',height=h,width=w,command=lambda: onClick("0"))
b0.grid(row=6,column=2,padx=px,pady=py)
dot = Button(buttonFrame,text='.',height=h,width=w,command=lambda: onClick("."))
dot.grid(row=6,column=3,padx=px,pady=py)
equal = Button(buttonFrame,text='=',height=h,width=w,command=equal)
equal.grid(row=6,column=4,padx=px,pady=py)


master.mainloop()
