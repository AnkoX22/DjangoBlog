from tkinter import *
from tkinter import ttk
import datetime

def findMonth(number):

    values = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July", 
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December" 
    }
    return values.get(number, "nothing")

def deleteTask(boolVal, string) :
    if boolVal:
        output = ""
        for c in string :
            output += c + '\u0336'
        
    return output

def on_click_entry(event,addToDo):
    if addToDo.get() == "To do":
        addToDo.delete(0,END)
        addToDo.insert(0,' ')
        addToDo.config(foreground = 'black')

def on_focus_out(event,addToDo):
    if addToDo.get() == "":
        addToDo.insert(0,'To do')
        addToDo.config(foreground = 'grey')


def toDo(root, num):
   boolVal = BooleanVar
   addToDo = ttk.Entry(root, foreground="black", background="white")
   addToDo.grid(row=num,column=1)
   addToDo.insert(0,"To do")
   addToDo.config(foreground ='grey')
   addToDo.bind('<FocusIn>',on_click_entry(event=any,addToDo= addToDo))
   addToDo.bind('<FocusOut>', on_focus_out(event= any,addToDo=addToDo))

   check1 =  ttk.Checkbutton(root, text="", variable=boolVal )
   check1.grid(row=num,column=0)
   return num+1

def defaultToDo(root,num):
    for i in range(3):
        toDo(root,num+i)
    return num+3

datetimeToday = datetime.datetime.now()
root = Tk()
root.geometry("700x650")

style = ttk.Style()

style.configure("To-do-Entry",fg="black", bg="white")

month = findMonth(datetimeToday.month)
day = datetimeToday.day

dateWeek = month + " " + str(day) + " - " + month + " " + str(day + 7)

lineCounter = 0

label = ttk.Label(root, text="My to do list")
label.grid(column=0,row= lineCounter)
lineCounter += 1

addToDoB = ttk.Button(root, text="+")
addToDoB.grid(row=lineCounter, column=100)


weekLabel = ttk.Label(root,text = dateWeek)
weekLabel.grid(column=0, row=lineCounter)
lineCounter += 1

mon = ttk.Label(root, text="Mon")
mon.grid(row=lineCounter)
lineCounter += 1
lineCounter += defaultToDo(root,lineCounter)

tue = ttk.Label(root, text="Tue")
tue.grid(row=lineCounter)
lineCounter += 1
lineCounter += defaultToDo(root,lineCounter)

wed = ttk.Label(root, text="Wed")
wed.grid(row =lineCounter)
lineCounter += 1
lineCounter += defaultToDo(root,lineCounter)


thir = ttk.Label(root, text="Thir")
thir.grid(row=lineCounter)
lineCounter += 1
lineCounter += defaultToDo(root,lineCounter)


fri = ttk.Label(root, text="Fri")
fri.grid(row= lineCounter)
lineCounter += 1
lineCounter += defaultToDo(root,lineCounter)


sat = ttk.Label(root, text = "Sat")
sat.grid(row= lineCounter)
lineCounter += 1
lineCounter += defaultToDo(root,lineCounter)


sun = ttk.Label(root, text="Sun")
sun.grid(row= lineCounter)
lineCounter += 1
lineCounter += defaultToDo(root,lineCounter)


root.mainloop()

