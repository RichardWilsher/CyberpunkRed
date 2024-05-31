import tkinter as tk
from tkinter import ttk 
import random

# tutorial from https://www.pythontutorial.net/tkinter/tkinter-listbox/

def initaliseinitatives(initativelist):
    # method to initialise initative array
    # currently fills the listbox, but not the final usage
    for i in range(35):
        initativelist.append("empty")
    return initativelist

def reverselist(initativelist):
    # method to reverse the list
    newlist = initativelist[:: -1]
    return newlist

def moveup(initativelist, roll, name):
    # method to resolve moving an initative position after a clash
    if initativelist[roll] == "empty":
        initativelist[roll] = name
    else:
        oldname = initativelist[roll]
        initativelist[roll] = name
        initativelist = moveup(initativelist, roll-1, oldname)
    return initativelist

def addinitiativevalue(initativelist, roll, name):
    # method to add a value to initative
    if initativelist[roll] == "empty": 
        initativelist[roll] = name
    else:
        oldname = initativelist[roll]
        order = random.randrange(1,3)
        if order == 1:
            initativelist[roll] = name
            initativelist = moveup(initativelist, roll-1, oldname)
        else: 
            initativelist = moveup(initativelist, roll-1, name)
    return initativelist

def filllistbox(initativelist):
    # method to fill the listbox
    newlist = []
    newlist = reverselist(initativelist)
    index = 0
    for x in newlist:
        if (x != "empty"): 
            listbox.insert(index,x)
            index += 1

def printlist(initativelist):
    # method to print the list for debug purposes
    for x in initativelist:
        print(x)

#declare initative list array
initativelist = []

# setup the tkinter window
win = tk.Tk()
win.geometry("300x300")
win.title("Cyberpunk Initative Tracker")

#setup the listbox and scrollbar
listbox = tk.Listbox(win, height = 10,  bg = "white", fg = "black", selectmode = "SINGLE")
scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL, command=listbox.yview)
# assign the scrollbar to the listbox
listbox['yscrollcommand'] = scrollbar.set
# pack components
listbox.pack()
scrollbar.pack()
# #place opponents in window
listbox.place(x=5,y=5, height=200, width=200)
scrollbar.place(x=200,y=5, height=200, width=20)

# add initative values
initativelist = initaliseinitatives(initativelist)
initativelist = addinitiativevalue(initativelist, 16, "Forty")
initativelist = addinitiativevalue(initativelist, 12, "Grease")
initativelist = addinitiativevalue(initativelist, 11, "Sanjay")
initativelist = addinitiativevalue(initativelist, 12, "Redeye")
initativelist = addinitiativevalue(initativelist, 10, "Mook1")
initativelist = addinitiativevalue(initativelist, 10, "Mook2")
# fill the listbox
filllistbox(initativelist)

win.mainloop()