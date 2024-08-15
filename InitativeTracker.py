# Program to add and track initative values for Cyberpunk Red

import tkinter as tk
from tkinter import ttk 
import random

def initaliseinitatives(initativelist):
    # method to initialise initative array
    for _ in range(35):
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

def filllistbox(initativelist):
    # method to fill the listbox
    listbox.delete(0,'end')
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
    filllistbox(initativelist)
    return initativelist

#declare initative list array
initativelist = []

# setup the tkinter window
win = tk.Tk()
win.geometry("500x220")
win.title("Cyberpunk Initative Tracker")
canvas = tk.Canvas(win, width=500, height=220, bg="white")
canvas.pack()

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
# setup the buttons
add_button = tk.Button(win, text="Add", font=("Arial", 12), bg='#a32', fg='#fff', command=lambda: addinitiativevalue(initativelist, int(initative_textbox.get()), str(name_textbox.get())))
add_button.place(x=240, y=85)
# pack components
listbox.pack()
scrollbar.pack()
# #place opponents in window
listbox.place(x=5,y=5, height=200, width=200)
scrollbar.place(x=200,y=5, height=200, width=20)

# add initative values
initativelist = initaliseinitatives(initativelist)

win.mainloop()