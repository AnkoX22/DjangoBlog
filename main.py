from tkinter import *
from tkinter import ttk
import datetime

def findMonth(number):

    addToDo = ttk.Entry

    values = {
        1 : "January", 2 : "February", 3 : "March", 4 : "April",
        5 : "May", 6 : "June", 7 : "July", 8 : "August",9 : "September",
        10 : "October", 11 : "November",12 : "December" 
    }
    return values.get(number, "nothing")


class toDo:
    
    def __init__(self,root,num):
        self.root = root
        self.num = num
        self.addToDo = ttk.Entry(root, foreground="black", background="white")
        self.boolVal = BooleanVar()
        root.bind('<Button-1>', self.save_text)

        
    
    def on_click_entry(self,event):
        if self.addToDo.get() == "To do":
            self.addToDo.delete(0,END)
            self.addToDo.insert(0,"")
            self.addToDo.config(foreground = 'black')

    def on_focus_out(self,event):
        if self.addToDo.get() == "":
            self.addToDo.insert(0,"To do")
            self.addToDo.config(foreground = 'grey')
    
    def save_text(self,event=None):

        self.addToDo.get()

    def createToDo(self):
        self.addToDo.grid(row=self.num,column=1)
        self.addToDo.insert(0,"To do")
        self.addToDo.config(foreground ='grey')
        self.addToDo.bind('<FocusIn>',self.on_click_entry)
        self.addToDo.bind('<FocusOut>', self.on_focus_out)
        self.addToDo.bind('<Return>',self.save_text)

        check1 =  ttk.Checkbutton(root, text="", variable=self.boolVal, command= self.mark_task_done )
        check1.grid(row=self.num,column=0)
        return self.num+1
    
    def defaultToDo(self,num):
        for i in range(3):
            num = toDo(self.root,num).createToDo()
        return num
    
    def mark_task_done(self) :
        string = self.addToDo.get()
        self.addToDo.configure(foreground='grey');
        if self.boolVal:
            output = ""
            for c in string :
                output = output +'\u0336'+ c + '\u0336'
        self.addToDo.delete(0,END)
        self.addToDo.insert(0,output)
        
        return output

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

toDo1 = toDo(root,lineCounter)

mon = ttk.Label(root, text="Mon")
mon.grid(row=lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)

tue = ttk.Label(root, text="Tue")
tue.grid(row=lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)

wed = ttk.Label(root, text="Wed")
wed.grid(row =lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)


thir = ttk.Label(root, text="Thir")
thir.grid(row=lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)


fri = ttk.Label(root, text="Fri")
fri.grid(row= lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)


sat = ttk.Label(root, text = "Sat")
sat.grid(row= lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)


sun = ttk.Label(root, text="Sun")
sun.grid(row= lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)


root.mainloop()

