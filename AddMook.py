import databaseTools
import mook
import tkinter as tk
from tkinter import ttk 
import numbers

db = databaseTools.databaseTools()
standardstats = [2, 3, 4, 5, 6, 7, 8]
stats = {
    'int': 2,
    'ref': 2,
    'dex': 2,
    'tech': 2,
    'cool': 2,
    'will': 2,
    'luck': '-',
    'move': 2,
    'body': 2,
    'emp': 2
}
# not sure if these will be used or not
will = 2
body = 2
armour_modifier = 0 

def save():
    print("save")

def clear():
    print("clear")

win = tk.Tk()
w = 832
h = 902
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
win.geometry('%dx%d+%d+%d' % (w, h, x, y))
win.title("Cyberpunk Red Mook Adder")
canvas = tk.Canvas(win, width=w, height=h, bg="white")
# Shadow Box
rectangle = canvas.create_rectangle(9, 9, w-3, h-3, fill="#ddd", outline="#ddd", width=2)
# Border Box
rectangle = canvas.create_rectangle(5, 5, w-7, h-7, fill="white", outline="#ccc", width=2)
canvas.pack()

type_label = tk.Label(win, text="Type:", font=("Arial", 12), bg='#fff', fg='#000')
type_label.place(x=10, y=15)
type_v = tk.StringVar()
type_combo = ttk.Combobox(win, width = 5, textvariable = type_v)
mastertype = db.selectedfindall("cpr.type", "name")
type_combo['values'] = mastertype
type_combo['state'] = 'readonly'
type_combo.current(0)
type_combo.place(x=80, y=15)
mooktype_label = tk.Label(win, text="Mook Type:", font=("Arial", 12), bg='#fff', fg='#000')
mooktype_label.place(x=440, y=15)
mooktype_v = tk.StringVar()
mooktype_combo = ttk.Combobox(win, width = 20, textvariable = mooktype_v)
mooktype = db.selectedfindall("cpr.mook_type", "name")
mooktypes = []
for mook in mooktype:
    mooktypes.append(mook[0])
mooktype_combo['values'] = mooktypes
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
roles = db.orderedselecectedfindall("cpr.roles", "name", "name")
role_combo['values'] = roles
role_combo['state'] = 'readonly'
position = 0
for index,role in enumerate(roles):
    string = str(role)
    string = string.lstrip('(\')')
    string = string.rstrip(',\')')
    if string == "none":
        position = index
role_combo.current(position)
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

# Stats divider
rectangle = canvas.create_rectangle(15, 130, 135, 155, fill="#a32", outline="#a32", width=3)
# Stats cut out
canvas.create_line(131, 127, 151, 157, fill="#fff", width=7)
# Stats Divider
canvas.create_line(15, 157, 818, 157, fill="#000", width=2)
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
# stat combo boxes
int_value = tk.StringVar()
int_combo = ttk.Combobox(win, width = 2, textvariable = int_value)
int_combo['values'] = standardstats
int_combo['state'] = 'readonly'
int_combo.current(0)
int_combo.place(x=49, y=160)
ref_value = tk.StringVar()
ref_combo = ttk.Combobox(win, width = 2, textvariable = ref_value)
ref_combo['values'] = standardstats
ref_combo['state'] = 'readonly'
ref_combo.current(0)
ref_combo.place(x=117, y=160)
dex_value = tk.StringVar()
dex_combo = ttk.Combobox(win, width = 2, textvariable = dex_value)
dex_combo['values'] = standardstats
dex_combo['state'] = 'readonly'
dex_combo.current(0)
dex_combo.place(x=199, y=160)
tech_value = tk.StringVar()
tech_combo = ttk.Combobox(win, width = 2, textvariable = tech_value)
tech_combo['values'] = standardstats
tech_combo['state'] = 'readonly'
tech_combo.current(0)
tech_combo.place(x=292, y=160)
cool_value = tk.StringVar()
cool_combo = ttk.Combobox(win, width = 2, textvariable = cool_value)
cool_combo['values'] = standardstats
cool_combo['state'] = 'readonly'
cool_combo.current(0)
cool_combo.place(x=375, y=160)
will_value = tk.StringVar()
will_combo = ttk.Combobox(win, width = 2, textvariable = will_value)
will_combo['values'] = standardstats
will_combo['state'] = 'readonly'
will_combo.current(0)
will_combo.place(x=453, y=160)
luck_value = tk.StringVar()
luck_combo = ttk.Combobox(win, width = 2, textvariable = luck_value)
luck_combo['values'] = ['-', '2', '3', '4', '5', '6', '7', '8']
luck_combo['state'] = 'readonly'
luck_combo.current(0)
luck_combo.place(x=533, y=160)
move_value = tk.StringVar()
move_combo = ttk.Combobox(win, width = 2, textvariable = move_value)
move_combo['values'] = standardstats
move_combo['state'] = 'readonly'
move_combo.current(0)
move_combo.place(x=615, y=160)  
body_value = tk.StringVar()
body_combo = ttk.Combobox(win, width = 2, textvariable = body_value)
body_combo['values'] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 14]
body_combo['state'] = 'readonly'
body_combo.current(0)
body_combo.place(x=712, y=160)
emp_value = tk.StringVar()
emp_combo = ttk.Combobox(win, width = 2, textvariable = emp_value)
emp_combo['values'] = standardstats
emp_combo['state'] = 'readonly'
emp_combo.current(0)
emp_combo.place(x=788, y=160)
# armour divider
rectangle = canvas.create_rectangle(15, 190, 135, 215, fill="#a32", outline="#a32", width=3)
# armour cut out
canvas.create_line(131, 187, 151, 217, fill="#fff", width=7)
# armour Divider
canvas.create_line(15, 217, 818, 217, fill="#000", width=2)
armour_label = tk.Label(win, text="ARMOUR", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
armour_label.place(x=15, y=190)
# armour selector
# head armor Box
rectangle = canvas.create_rectangle(20, 222, 31, 265, fill="#a32", outline="#a32", width=3)
# body armor Box
rectangle = canvas.create_rectangle(20, 266, 31, 309, fill="#a32", outline="#a32", width=3)
#head armour Boxes
rectangle = canvas.create_rectangle(31, 222, 306, 265, fill="#fff", outline="#a32", width=3)
rectangle = canvas.create_rectangle(311, 222, 371, 265, fill="#fff", outline="#a32", width=3)
# body armour Boxes
rectangle = canvas.create_rectangle(31, 266, 306, 309, fill="#fff", outline="#a32", width=3)
rectangle = canvas.create_rectangle(311, 266, 371, 309, fill="#fff", outline="#a32", width=3)
# head body shield labels
canvas.create_text(25, 265, text="HEAD", font=("Arial", 10, "bold"), fill='#ffffff', angle=90, anchor="w")
canvas.create_text(25, 308, text="BODY", font=("Arial", 10, "bold"), fill='#ffffff', angle=90, anchor="w")
# armour combo boxes
armours = db.selectedfindall("cpr.armour","name")
armour_names = []
for armour in armours:
    armour_names.append(armour[0]) 
headsp_var = tk.StringVar()
bodysp_var = tk.StringVar()
headsp_combo = ttk.Combobox(win, width = 20, textvariable = headsp_var)
headsp_combo['values'] = armour_names
headsp_combo['state'] = 'readonly'
headsp_combo.current(0)
headsp_combo.place(x=40, y=232)
bodysp_combo = ttk.Combobox(win, width = 20, textvariable = bodysp_var)
bodysp_combo['values'] = armour_names
bodysp_combo['state'] = 'readonly'
bodysp_combo.current(0)
bodysp_combo.place(x=40, y=280)
# SP labels
headsp_label = tk.Label(win, text="0", font=("Arial", 10, "bold"), bg='#fff', fg='#000')
headsp_label.place(x=335, y=232)
bodysp_label = tk.Label(win, text="0", font=("Arial", 10, "bold"), bg='#fff', fg='#000')
bodysp_label.place(x=335, y=280)
# weapon divider
rectangle = canvas.create_rectangle(15, 320, 135, 345, fill="#a32", outline="#a32", width=3)
# weapon cut out
canvas.create_line(131, 317, 151, 347, fill="#fff", width=7)
# weapon Divider
canvas.create_line(15, 347, 818, 347, fill="#000", width=2)
weapon_label = tk.Label(win, text="WEAPONS", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
weapon_label.place(x=15, y=320)
# weapon controls
weapons = db.selectedfindall("cpr.weapons","name")
qualities = db.selectedfindall("cpr.weapon_quality","name")
weapon_list = []
for weapon in weapons:
    weapon_list.append(weapon[0])
weapon_listbox = tk.Listbox(win, height=3, width=20, font=("Arial", 12), bg='#fff', fg='#000')
weapon_listbox.place(x=10, y=360)
weapon_scrollbar = ttk.Scrollbar(win, orient="vertical", command=weapon_listbox.yview)
weapon_listbox['yscrollcommand'] = weapon_scrollbar.set
weapon_scrollbar.pack(side="right", fill="y")
weapon_scrollbar.place(x=192, y=360, height=61)
# skills divider
rectangle = canvas.create_rectangle(15, 428, 135, 453, fill="#a32", outline="#a32", width=3)
# skills cut out
canvas.create_line(131, 425, 151, 455, fill="#fff", width=7)
# skills Divider
canvas.create_line(15, 455, 818, 455, fill="#000", width=2)
skilllabel = tk.Label(win, text="SKILL BASES", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
skilllabel.place(x=15, y=428)
# skills
skills = {}
skill_list = db.orderedselecectedfindall("cpr.skills", "name", "name")
display_skills = []
skill_list_items =tk.Variable(win, value=display_skills)
skills_listbox = tk.Listbox(win, listvariable=skill_list_items, height=8, width=20, font=("Arial", 12), bg='#fff', fg='#000')
skills_listbox.place(x=10, y=460)
skills_scrollbar = ttk.Scrollbar(win, orient="vertical", command=skills_listbox.yview)
skills_listbox.configure(yscrollcommand=skills_scrollbar.set)
skills_scrollbar.pack(side="right", fill="y")
skills_scrollbar.place(x=192, y=460, height=155)
# equipment divider
rectangle = canvas.create_rectangle(15, 620, 135, 645, fill="#a32", outline="#a32", width=3)
# equipment cut out
canvas.create_line(131, 617, 151, 643, fill="#fff", width=7)
# equipment Divider
canvas.create_line(15, 647, 818, 647, fill="#000", width=2)
equiplabel = tk.Label(win, text="EQUIPMENT", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
equiplabel.place(x=15, y=620)
# equipment
equipment = db.orderedselecectedfindall("cpr.equipment", "name", "name")   
display_equipment = []
for equip in equipment:
    display_equipment.append(equip[0])
equipment_list_items =tk.Variable()
equipment_listbox = tk.Listbox(win, listvariable=equipment_list_items, height=4, width=20, font=("Arial", 12), bg='#fff', fg='#000')
equipment_listbox.place(x=10, y=650)
equipment_scrollbar = ttk.Scrollbar(win, orient="vertical", command=equipment_listbox.yview)
equipment_listbox.configure(yscrollcommand=equipment_scrollbar.set)
equipment_scrollbar.pack(side="right", fill="y")
equipment_scrollbar.place(x=192, y=650, height=79)
# Cyberwear divider
rectangle = canvas.create_rectangle(15, 735, 135, 760, fill="#a32", outline="#a32", width=3)
# Cyberwear cut out
canvas.create_line(131, 732, 151, 758, fill="#fff", width=7)
# Cyberwear Divider
canvas.create_line(15, 762, 818, 762, fill="#000", width=2)
cyberlabel = tk.Label(win, text="CYBERWEAR", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
cyberlabel.place(x=15, y=732)
# Cyberwear
cyberwear = db.orderedselecectedfindall("cpr.cyberwear", "name", "name")
display_cyberwear = []
for cyber in cyberwear:
    display_cyberwear.append(cyber[0])
equipment_list_items =tk.Variable()
equipment_listbox = tk.Listbox(win, listvariable=equipment_list_items, height=4, width=20, font=("Arial", 12), bg='#fff', fg='#000')
equipment_listbox.place(x=10, y=770)
equipment_scrollbar = ttk.Scrollbar(win, orient="vertical", command=equipment_listbox.yview)
equipment_listbox.configure(yscrollcommand=equipment_scrollbar.set)
equipment_scrollbar.pack(side="right", fill="y")
equipment_scrollbar.place(x=192, y=770, height=79)
# buttons
save_button = tk.Button(win, text="SAVE", font=("Arial", 12, "bold"), bg='#a32', fg='#fff', command=save)
save_button.place(x=10, y=855)
clear_button = tk.Button(win, text="CLEAR", font=("Arial", 12, "bold"), bg='#a32', fg='#fff', command=clear)
clear_button.place(x=100, y=855)





win.mainloop()