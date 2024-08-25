from tkinter import *
from tkinter import ttk
import datetime


# open file and if it doesnt exist create one to save the todo list
with open("to_do_list.txt") as file:
        # write the title of the file
        file.write('To do list\n','w+')

# a function to get the month name from 
def findMonth(number):

    # the number of the month with the name of the month in enum / dictionary 
    months = {
        1 : "January", 2 : "February", 3 : "March", 4 : "April",
        5 : "May", 6 : "June", 7 : "July", 8 : "August",9 : "September",
        10 : "October", 11 : "November",12 : "December" 
    }

    # return the name of the month or nothing (word) if not in dictionary
    return months.get(number, "nothing")


# class to do for the checkbox and the entry of every day of the week
class toDo:
    
    # initialization for the creation of a toDo object, class properties
    def __init__(self,root,num):
        # root in which creates the elements
        self.root = root
        # the number of the line in the grid that we are currently on
        self.num = num
        # the add to do entry of every check box / day
        self.addToDo = ttk.Entry(root, foreground="black")
        # the boolean value of the checkbox
        self.boolVal = BooleanVar()
        # save text when user pushes enter
        root.bind('<Button-1>', self.save_text)

        
    # function for when user clicks on entry
    def on_click_entry(self,event):
        if self.addToDo.get() == "To do":
            self.addToDo.delete(0,END)
            self.addToDo.insert(0,"")
            self.addToDo.config(foreground = 'black')

    # function for when the user  focuses out of entry
    def on_focus_out(self,event):
        if self.addToDo.get() == "":
            self.addToDo.insert(0,"To do")
            self.addToDo.config(foreground = 'grey')
    
    # save text function to save the text in file 
    def save_text(self,event=None):

        self.addToDo.get()

    # inserts to do entries and checkbuttons on grid
    def createToDo(self):
        self.addToDo.grid(row=self.num,column=1)
        self.addToDo.insert(0,"To do")
        self.addToDo.config(foreground ='grey')
        self.addToDo.bind('<FocusIn>',self.on_click_entry)
        self.addToDo.bind('<FocusOut>', self.on_focus_out)
        self.addToDo.bind('<Return>',self.save_text)

        check1 =  ttk.Checkbutton(root, text="", variable=self.boolVal, command= self.mark_task )
        check1.grid(row=self.num,column=0)
        return self.num+1
    
    # create default to dos (3)
    def defaultToDo(self,num):
        for i in range(3):
            num = toDo(self.root,num).createToDo()
        return num
    
    #  mark or unmark task (with strike through) controlled by checkbutton
    def mark_task(self) :
        string = self.addToDo.get()
        # if checkbutton unchecked
        if(self.boolVal.get() == 0):
            string = self.addToDo.get()
            if self.boolVal:
                output = ""
                self.addToDo.config(foreground="black")
                for c in string:
                    if c != '\u0336':
                        output += c
            self.addToDo.delete(0,END)
            self.addToDo.add(0,output)
        # if checkbutton checked
        else :
            self.addToDo.configure(foreground='grey')
            if self.boolVal:
                output = ""
                for c in string :
                    output = output + c + '\u0336'
            self.addToDo.delete(0,END)
            self.addToDo.insert(0,output)
        
        return output
        
# get datetime now
datetimeToday = datetime.datetime.now()
# create root
root = Tk()
# choose window dimensions
root.geometry("700x650")

# create style elements to create specific style
style = ttk.Style()

# use a  theme style (existing)
style.theme_use("vista")
# Create a custom style for a label
style.configure("Custom.TLabel", 
                font=("ComicSan", 12), 
                foreground="black")


# finfd the name of the month from number using the findMonth function
month = findMonth(datetimeToday.month)
day = datetimeToday.day # get day

# create date week string
dateWeek = month + " " + str(day) + " - " + month + " " + str(day + 7)

# days array
days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

# var lineCounter to keep count of the row in grid
lineCounter = 0

# create initial label and put in grid
label = ttk.Label(root, text="My to do list", style='Custom.TLabel')
label.grid(column=0,row= lineCounter)
lineCounter += 1

# add button to increase the to do checkbuttons / entries
addToDoB = ttk.Button(root, text="+")
addToDoB.grid(row=lineCounter, column=100)

# create week label and put in grid
weekLabel = ttk.Label(root,text = dateWeek, style='Custom.TLabel')
weekLabel.grid(column=0, row=lineCounter)
lineCounter += 1

# create to do object
toDo1 = toDo(root,lineCounter)

# create mon label, default to dos and put in grid
mon = ttk.Label(root, text="Mon", style='Custom.TLabel')
mon.grid(row=lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)

# create tue label, default to dos and put in grid
tue = ttk.Label(root, text="Tue", style='Custom.TLabel')
tue.grid(row=lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)

# create wed label, default to dos and put in grid
wed = ttk.Label(root, text="Wed", style='Custom.TLabel')
wed.grid(row =lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)

# create thir label, default to dos and put in grid
thir = ttk.Label(root, text="Thir", style='Custom.TLabel')
thir.grid(row=lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)

# create fri label, default to dos and put in grid
fri = ttk.Label(root, text="Fri", style='Custom.TLabel')
fri.grid(row= lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)

# create sat label, default to dos and put in grid
sat = ttk.Label(root, text = "Sat", style='Custom.TLabel')
sat.grid(row= lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)

# create sun label, default to dos and put in grid
sun = ttk.Label(root, text="Sun", style='Custom.TLabel')
sun.grid(row= lineCounter)
lineCounter += 1
lineCounter += toDo1.defaultToDo(lineCounter)


root.mainloop()

