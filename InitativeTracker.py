import tkinter as tk
from tkinter import ttk 
import random

# to do, add in tkinter controls at manually add participants

def initaliseinitatives(initativelist):
    # method to initialise initative array
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

def items_selected(event):
    # method to get selected item in the listbox and display in the textboxes
    global initative_list
    selected_indices = listbox.curselection()
    selected_entity = [listbox.get(i) for i in selected_indices]
    name_textbox.delete(0,'end')
    name_textbox.insert('end', selected_entity)
    for index,x in enumerate(initativelist):
        if x == selected_entity[0]:
            initative_textbox.delete(0,'end')
            initative_textbox.insert('end', index)

#declare initative list array
initativelist = []

# setup the tkinter window
win = tk.Tk()
win.geometry("600x300")
win.title("Cyberpunk Initative Tracker")

#setup the listbox and scrollbar
listbox = tk.Listbox(win, height = 10,  bg = "white", fg = "black", selectmode = "SINGLE")
scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL, command=listbox.yview)
# assign the scrollbar to the listbox
listbox['yscrollcommand'] = scrollbar.set
# assign the ListboxSelection command to the listbox
listbox.bind('<<ListboxSelect>>', items_selected)
# setup the labels and textboxes
name_label = tk.Label(win, text="Name:", font=("Arial", 12), bg='#fff', fg='#000')
name_label.place(x=240, y=25)
name_textbox = tk.Entry(win, font=("Arial", 12), bg='#fff', fg='#000')
name_textbox.place(x=305, y=25)
initative_label = tk.Label(win, text="Initative:", font=("Arial", 12), bg='#fff', fg='#000')
initative_label.place(x=240, y=55)
initative_textbox = tk.Entry(win, font=("Arial", 12), bg='#fff', fg='#000')
initative_textbox.place(x=305, y=55)

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