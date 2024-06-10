import databaseTools
import mook
import tkinter as tk
from tkinter import ttk 
import numbers

db = databaseTools.databaseTools()

win = tk.Tk()
win.title("Cyberpunk Red Mook Adder")
canvas = tk.Canvas(win, width=830, height=645, bg="white")
# Shadow Box
rectangle = canvas.create_rectangle(9, 9, 829, 644, fill="#ddd", outline="#ddd", width=2)
# Border Box
rectangle = canvas.create_rectangle(5, 5, 825, 640, fill="white", outline="#ccc", width=2)
canvas.pack()

type_label = tk.Label(win, text="Type:", font=("Arial", 12), bg='#fff', fg='#000')
type_label.place(x=10, y=15)
type_v = tk.StringVar()
type_combo = ttk.Combobox(win, width = 5, textvariable = type_v)
type_combo['values'] = ('Mook', 'NPC', 'PC')
type_combo['state'] = 'readonly'
type_combo.current(0)
type_combo.place(x=80, y=15)
mooktype_label = tk.Label(win, text="Mook Type:", font=("Arial", 12), bg='#fff', fg='#000')
mooktype_label.place(x=440, y=15)
mooktype_v = tk.StringVar()
mooktype_combo = ttk.Combobox(win, width = 20, textvariable = mooktype_v)
mooktype_combo['values'] = ('Mook', 'Hardened Mook', 'Lieutenant', 'Hardened Lieutenant', 'Mini-Boss', 'Hardened Mini-Boss', 'Boss', 'Hardened Boss')
mooktype_combo['state'] = 'readonly'
mooktype_combo.current(0)
mooktype_combo.place(x=560, y=15)
name_label = tk.Label(win, text="Name:", font=("Arial", 12), bg='#fff', fg='#000')
name_label.place(x=10, y=55)
mooknaname_text = tk.Text(win, height=1, width=20, font=("Arial", 12), bg='#fff', fg='#000')
mooknaname_text.place(x=80, y=55)
rep_label = tk.Label(win, text="Rep:", font=("Arial", 12), bg='#fff', fg='#000')
rep_label.place(x=310, y=55)
rep_v = tk.StringVar() 
rep_combo = ttk.Combobox(win, width = 2, textvariable = rep_v) 
rep_combo['values'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
rep_combo['state'] = 'readonly'
rep_combo.current(0)
rep_combo.place(x=435, y=55)
role_label = tk.Label(win, text="Role:", font=("Arial", 12), bg='#fff', fg='#000')
role_label.place(x=10, y=96)
role_v = tk.StringVar()
role_combo = ttk.Combobox(win, width = 10, textvariable = role_v)
role_combo['values'] = ('none', 'Exec', 'Fixer', 'Lawman', 'Media', 'Medtech', 'Netrunner', 'Nomad', 'Rockerboy', 'Solo', 'Tech')
role_combo['state'] = 'readonly'
role_combo.current(0)
role_combo.place(x=80, y=96)
roleability_label = tk.Label(win, text="Role Ability:", font=("Arial", 12), bg='#fff', fg='#000')
roleability_label.place(x=310, y=96)
roleability_v = tk.StringVar()
roleability_combo = ttk.Combobox(win, width = 2, textvariable = roleability_v)
roleability_combo['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
roleability_combo['state'] = 'readonly'
roleability_combo.current(0)
roleability_combo.place(x=435, y=96)

seriouslywoundedlabel = tk.Label(win, text="SERIOUSLY WOUNDED", font=("Arial", 8, "bold"), bg='#fff', fg='#000', wraplength=100, justify="left")
seriouslywoundedlabel.place(x=510, y=47)
mookseriouslywounded_label = tk.Label(win, text="10", font=("Arial", 12), bg='#fff', fg='#000')
mookseriouslywounded_label.place(x=640, y=55)
deathsavelabel = tk.Label(win, text="DEATH SAVE", font=("Arial", 8, "bold"), bg='#fff', fg='#000', wraplength=100, justify="left")
deathsavelabel.place(x=510, y=102)
mookdeathsave_label = tk.Label(win, text="2", font=("Arial", 12), bg='#fff', fg='#000')
mookdeathsave_label.place(x=640, y=96)
hplabel = tk.Label(win, text="HP", font=("Arial", 14, "bold"), bg='#fff', fg='#000')
hplabel.place(x=687, y=46)
mookhp_label = tk.Label(win, text="20", font=("Arial", 20), bg='#fff', fg='#000')
mookhp_label.place(x=740, y=69)

statslabel = tk.Label(win, text="STATS", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
statslabel.place(x=17, y=131)
# Stats Labels
intlabel = tk.Label(win, text="INT", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
intlabel.place(x=20, y=160)
reflabel = tk.Label(win, text="REF", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
reflabel.place(x=85, y=160)
dexlabel = tk.Label(win, text="DEX", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
dexlabel.place(x=165, y=160)
techlabel = tk.Label(win, text="TECH", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
techlabel.place(x=250, y=160)
coollabel = tk.Label(win, text="COOL", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
coollabel.place(x=330, y=160)
willlabel = tk.Label(win, text="WILL", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
willlabel.place(x=410, y=160)
lucklabel = tk.Label(win, text="LUCK", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
lucklabel.place(x=490, y=160)
movelabel = tk.Label(win, text="MOVE", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
movelabel.place(x=570, y=160)
bodylabel = tk.Label(win, text="BODY", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
bodylabel.place(x=670, y=160)
emplabel = tk.Label(win, text="EMP", font=("Arial", 10, "bold"), bg='#ddd', fg='#000')
emplabel.place(x=750, y=160)






win.mainloop()