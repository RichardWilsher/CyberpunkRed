# Program to add, track, and remove initiative values for Cyberpunk Red

import tkinter as tk
from tkinter import ttk
import random

def initialize_initiatives(initiative_list):
    for _ in range(35):
        initiative_list.append("empty")
    return initiative_list

def reverse_list(initiative_list):
    return initiative_list[::-1]

def move_up(initiative_list, roll, name):
    if initiative_list[roll] == "empty":
        initiative_list[roll] = name
    else:
        old_name = initiative_list[roll]
        initiative_list[roll] = name
        initiative_list = move_up(initiative_list, roll - 1, old_name)
    return initiative_list

def fill_listbox(initiative_list):
    listbox.delete(0, 'end')
    reversed_list = reverse_list(initiative_list)
    for index, entry in enumerate(reversed_list):
        if entry != "empty":
            listbox.insert(index, entry)

def items_selected(event):
    selected_indices = listbox.curselection()
    selected_entity = [listbox.get(i) for i in selected_indices]
    if selected_entity:
        name_textbox.delete(0, 'end')
        name_textbox.insert('end', selected_entity[0])
        for index, x in enumerate(initiative_list):
            if x == selected_entity[0]:
                initiative_textbox.delete(0, 'end')
                initiative_textbox.insert('end', index)
                break

def add_initiative_value(initiative_list, roll, name):
    if initiative_list[roll] == "empty":
        initiative_list[roll] = name
    else:
        old_name = initiative_list[roll]
        order = random.randrange(1, 3)
        if order == 1:
            initiative_list[roll] = name
            initiative_list = move_up(initiative_list, roll - 1, old_name)
        else:
            initiative_list = move_up(initiative_list, roll - 1, name)
    fill_listbox(initiative_list)
    return initiative_list

def handle_add():
    name = name_textbox.get().strip()
    initiative_str = initiative_textbox.get().strip()

    if not name:
        print("Error: Name cannot be empty.")
        return

    try:
        roll = int(initiative_str)
        if not 0 <= roll <= 34:
            print("Error: Initiative must be between 0 and 34.")
            return
    except ValueError:
        print("Error: Initiative must be an integer.")
        return

    add_initiative_value(initiative_list, roll, name)
    name_textbox.delete(0, 'end')
    initiative_textbox.delete(0, 'end')

def remove_selected_entry():
    selected_indices = listbox.curselection()
    selected_entity = [listbox.get(i) for i in selected_indices]
    if selected_entity:
        name_to_remove = selected_entity[0]
        for i, val in enumerate(initiative_list):
            if val == name_to_remove:
                initiative_list[i] = "empty"
                break
        fill_listbox(initiative_list)
        name_textbox.delete(0, 'end')
        initiative_textbox.delete(0, 'end')

# Declare initiative list array
initiative_list = []

# Setup the tkinter window
win = tk.Tk()
win.geometry("500x260")
win.title("Cyberpunk Initiative Tracker")
canvas = tk.Canvas(win, width=500, height=260, bg="white")
canvas.pack()

# Listbox and scrollbar
listbox = tk.Listbox(win, height=10, bg="white", fg="black", selectmode="SINGLE")
scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL, command=listbox.yview)
listbox['yscrollcommand'] = scrollbar.set
listbox.bind('<<ListboxSelect>>', items_selected)

# Labels and textboxes
name_label = tk.Label(win, text="Name:", font=("Arial", 12), bg='#fff', fg='#000')
name_label.place(x=240, y=25)
name_textbox = tk.Entry(win, font=("Arial", 12), bg='#fff', fg='#000')
name_textbox.place(x=305, y=25)

initiative_label = tk.Label(win, text="Initiative:", font=("Arial", 12), bg='#fff', fg='#000')
initiative_label.place(x=240, y=55)
initiative_textbox = tk.Entry(win, font=("Arial", 12), bg='#fff', fg='#000')
initiative_textbox.place(x=305, y=55)

# Add button
add_button = tk.Button(win, text="Add", font=("Arial", 12), bg='#a32', fg='#fff', command=handle_add)
add_button.place(x=240, y=90)

# Remove button
remove_button = tk.Button(win, text="Remove", font=("Arial", 12), bg='#a32', fg='#fff', command=remove_selected_entry)
remove_button.place(x=310, y=90)

# Place components
listbox.place(x=5, y=5, height=240, width=200)
scrollbar.place(x=200, y=5, height=240, width=20)

# Initialize initiative values
initiative_list = initialize_initiatives(initiative_list)

# Start GUI event loop
win.mainloop()
