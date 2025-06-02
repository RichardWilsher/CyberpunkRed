import mook
import tkinter as tk
from tkinter import END, ttk, messagebox 
import math
import skillclass as sc
import weaponclass as wc
import equipmentclass as ec
import cyberwearclass as cc
import orm as orm

# TODO add notes field
# TODO add weapon attachments
# TODO add vehicles

standardstats = [2, 3, 4, 5, 6, 7, 8]
# multiple entry arrays
mook_weapons = []
mook_skills = []
mook_equipment = []
mook_cyberwear = []

def sort(mook_skills):
    mook_skills.sort(key=lambda x: (x.name, x.notes))
    skills_listbox.delete(0, END)
    for skill in mook_skills:
        if skill.notes == "":
            skills_listbox.insert(END, f"{skill.name} {skill.value}")
        else:
            skills_listbox.insert(END, f"{skill.name} ({skill.notes}) {skill.value}")
    return mook_skills

def calc_hp(*arg):
    try:
        body = body_combo.get()
    except Exception:
        body = 2
    try:
        will = will_combo.get()
    except Exception:
        will = 2
    hp = 10 + (5 *(math.ceil((int(body) + int(will))/2)))
    mookhp_label.config(text=str(hp))
    mookdeathsave_label.config(text=str(body))
    seriouslywounded = math.ceil(hp/2)
    mookseriouslywounded_label.config(text=str(seriouslywounded))
        
def change_type(*arg):
    if type_combo.get() == 'Mook':
        mooktype_combo.place(x=560, y=15)
        mooktype_label.place(x=440, y=15)
    else:
        mooktype_combo.place_forget()
        mooktype_label.place_forget()

def change_armour(*arg):
    global headsp_label
    global bodysp_label
    try: 
        armour_value = armourdb.find("","name", headsp_combo.get())
        headsp = armour_value[0][2]
    except Exception:
        headsp = 4
    headsp_label.config(text=headsp)
    try:
        armour_value = armourdb.find("","name", bodysp_combo.get())
        bodysp = armour_value[0][2]
    except Exception:
        bodysp = 4
    bodysp_label.config(text=bodysp)

def clear():
    global mook_weapons
    global mook_skills
    global mook_equipment
    global mook_cyberwear
    mook_weapons.clear()
    mook_skills.clear()
    mook_equipment.clear()
    mook_cyberwear.clear()
    # clear all items
    mooktype_combo.current(0)
    type_combo.current(0)
    mookname_entry.delete(0, tk.END)
    rep_combo.current(0)
    role_entry.delete(0, tk.END)
    role_entry.insert(0, "none")
    location_entry.delete(0, tk.END)
    # stats
    int_combo.current(0)
    ref_combo.current(0)
    dex_combo.current(0)
    tech_combo.current(0)
    cool_combo.current(0)
    will_combo.current(0)
    luck_combo.current(0)
    move_combo.current(0)
    body_combo.current(0)
    emp_combo.current(0)
    # armour
    headsp_combo.current(0)
    bodysp_combo.current(0)
    headtup_var.set(0)
    bodytup_var.set(0)
    # weapons
    weapon_combo.current(0)
    weaponquality_combo.current(0)
    weapon_listbox.delete(0, tk.END)
    # skills
    skill_combo.current(0)
    skillvalue_combo.current(0)
    skillnotes_entry.delete(0, tk.END)
    skills_listbox.delete(0, tk.END)
    # add universal skills
    skillname = "Athletics"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 6))
    skillname = "Brawling"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 32))
    skillname = "Concentration"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 1))
    skillname = "Conversation"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 44))
    skillname = "Education"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 24))
    skillname = "Evasion"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 33))
    skillname = "First Aid"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 57))
    skillname = "Human Perception"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 45))
    skillname = "Language"
    skilllevel = "6"
    skills_listbox.insert(tk.END, skillname + " (Native) " + skilllevel)
    mook_skills.append(sc.skill(skillname, 6, "Native", 26))
    skillname = "Language"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " (Streetslang) " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "Streetslang", 26))
    skillname = "Local Expert"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " (Your Home) " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "Your Home", 28))
    skillname = "Perception"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 4))
    skillname = "Persuasion"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 47))
    skillname = "Stealth"
    skilllevel = "4"
    skills_listbox.insert(tk.END, skillname + " " + skilllevel)
    mook_skills.append(sc.skill(skillname, 4, "", 11))
    # equipment
    equipment_combo.current(0)
    equipmentquantity_combo.current(0)
    equipmentnotes_entry.delete(0, tk.END)
    equipment_listbox.delete(0, tk.END)
    # cyberwear
    cyberwear_combo.current(0)
    cyberwearquantity_combo.current(0)
    cyberwearnotes_entry.delete(0, tk.END)
    cyberwear_listbox.delete(0, tk.END)
    # clear arrays

def save_mook():
    name = mookname_entry.get()
    temp_type = type_combo.get()
    mtype = typedb.find("id","name", temp_type)[0][0]
    tempmook_type = mooktype_combo.get()
    mook_type = mooktypedb.find("id","name", tempmook_type)[0][0]
    location = location_entry.get()
    rep = rep_combo.get()
    role = role_entry.get()
    mookdb.insert(["name", "mook_type", "type", "location", "rep", "role"], [name, mook_type, mtype, location, rep, role])
    mookid = mookdb.find("id","name", name)[0][0]
    return mookid

def save_stats(mookid):
    stats = [int_combo.get(), ref_combo.get(), dex_combo.get(), tech_combo.get(), cool_combo.get(), will_combo.get(), luck_combo.get(), move_combo.get(), body_combo.get(), emp_combo.get()]
    for index,stat in enumerate(stats):
        mookstatdb.insert(["mookid", "statid", "value"], [mookid, index+1, stat])

def save_armour(mookid):
    headsp = headsp_combo.get()
    headid = armourdb.find("", "name", headsp)[0][0]
    bodysp = bodysp_combo.get()
    bodyid = armourdb.find("", "name", bodysp)[0][0]
    if headtup_var.get() == 1:
        headtup = 'y'
    else:
        headtup = 'n'
    if bodytup_var.get() == 1:
        bodytup = 'y'
    else:
        bodytup = 'n'
    mookheadarmourdb.insert(["mookid", "armourid", "techupgraded"], [mookid, headid, headtup])
    mookbodyarmourdb.insert(["mookid", "armourid", "techupgraded"], [mookid, bodyid, bodytup])

def save_weapons(mookid):
    for weapon in mook_weapons:
        quality = weapon.quality
        qualityid = weaponqualitydb.find("", "name", quality)[0][0]
        mookweapondb.insert(["mookid", "weaponid", "qualityid"], [mookid, weapon.id, qualityid])

def save_skills(mookid):
    sort(mook_skills)
    for skill in mook_skills:
        value = skill.value
        notes = skill.notes
        mookskilldb.insert(["mookid", "skillid", "value", "notes"], [mookid, skill.id, value, notes])

def save_equipment(mookid):
    for equipment in mook_equipment:
        quantity = equipment.quantity
        notes = equipment.notes
        mookequipmentdb.insert(["mookid", "equipmentid", "quantity", "notes"], [mookid, equipment.id, quantity, notes])
        

def save_cyberwear(mookid):
    for cyberwear in mook_cyberwear:
        cyberwearid = cyberwear.id
        quantity = cyberwear.quantity
        notes = cyberwear.notes
        mookcyberweardb.insert(["mookid", "cyberwearid", "quantity", "notes"], [mookid, cyberwearid, quantity, notes])  

def save():
    readytocommit = True
    mookid = -1
    if mookname_entry.get() == '':
        readytocommit = False
        messagebox.showerror("Error", "Mook Name is Required")
    else:
        if len(mookdb.find("", "name", mookname_entry.get())) > 0:
            readytocommit = False
            messagebox.showerror("Error", "Mook Name already Exists")
        else:
            mookid = save_mook()
            if mookid == -1:
                readytocommit = False
                messagebox.showerror("Error", "Mook ID not Found")
    if readytocommit:
        save_stats(mookid)
        save_armour(mookid)
        save_weapons(mookid)
        save_skills(mookid)
        save_equipment(mookid)
        save_cyberwear(mookid)
        clear()

def weaponadd():
    global mook_weapons
    weapon = weapondb.find("", "name", weapon_combo.get())
    quality = weaponqualitydb.find("", "name", weaponquality_combo.get())
    weaponentry = wc.weapon(weapon[0][1], quality[0][1], quality[0][0], weapon[0][2], weapon[0][3], weapon[0][0])
    mook_weapons.append(weaponentry)
    weaponname = quality[0][1] + " " + weapon[0][1]
    weapon_listbox.insert(tk.END, weaponname)

def weaponremove():
    global mook_weapons
    selected_indices = weapon_listbox.curselection()
    for i in selected_indices:
        mook_weapons.pop(i)
        weapon_listbox.delete(i)

def skilladd():
    new_skill = sc.skill("", 0, "", 1)
    new_skill.name = skill_combo.get().strip()

    try:
        new_skill.value = int(skill_value.get())
    except ValueError:
        messagebox.showerror("Invalid Value", "Skill value must be a number.")
        return

    new_skill.notes = skillnotes_entry.get()
    new_skill.id = skilldb.find("", "name", new_skill.name)[0][0]

    if new_skill.notes != "":
        name = new_skill.name + " " + new_skill.notes
    else:
        name = new_skill.name

    # Check for existing skill to update
    for i, skill in enumerate(mook_skills):
        if skill.notes != "":
            skillname = skill.name + " " + skill.notes
        else:
            skillname = skill.name
        
        if name == skillname:
            mook_skills[i] = new_skill  # ✅ Assign the instance, not the class
            skills_listbox.delete(i)
            if new_skill.notes == "":
                skills_listbox.insert(i, f"{new_skill.name} {new_skill.value}")
            else:
                skills_listbox.insert(i, f"{new_skill.name} ({new_skill.notes}) {new_skill.value}")
            break
    else:
        # Skill not found, so append
        mook_skills.append(new_skill)  # ✅ Append the instance
        if new_skill.notes == "":
            skills_listbox.insert(END, f"{new_skill.name} {new_skill.value}")
        else:
            skills_listbox.insert(END, f"{new_skill.name} ({new_skill.notes}) {new_skill.value}")

    # Reset input fields
    skill_combo.set("")
    skill_value.set("3")
    skillnotes_entry.delete(0, END)
    sort(mook_skills)

def skillremove():
    global mook_skills
    selected_indices = skills_listbox.curselection()
    for i in selected_indices:
        mook_skills.pop(i)
        skills_listbox.delete(i)

def on_skill_select(event):
    selection = event.widget.curselection()
    if not selection:
        return
    index = selection[0]

    try:
        skill = mook_skills[index]
        skill_combo.set(skill.name)
        skill_value.set(str(skill.value))  # assuming skill_value is a StringVar
        skillnotes_entry.delete(0, END)
        skillnotes_entry.insert(0, skill.notes)
    except IndexError:
        pass

def equipmentadd():
    global mook_equipment
    equipment = equipmentdb.find("", "name", equipment_combo.get())
    quantity = int(equipmentquantity_combo.get())
    notes = equipmentnotes_entry.get()
    equipmententry = ec.equipment(equipment[0][2], quantity, notes, equipment[0][0])
    if notes != '':
        note = "(" + notes + ")"
    else:
        note = ""
    if quantity > 1:
        equipmentname = equipment[0][2] + " x" + str(quantity) + " " + note
    else:
        equipmentname = equipment[0][2] + " " + note
    # # check for duplicate entry and replace if found
    position = -1
    for index,equipment in enumerate(mook_equipment):
        if equipment.name == equipmententry.name and equipment.notes == equipmententry.notes:
            position = index
    if position != -1:
        mook_equipment[index] = equipmententry
        equipment_listbox.delete(position)
        equipment_listbox.insert(position, equipmentname)
    else:
        mook_equipment.append(equipmententry)
        equipment_listbox.insert(tk.END, equipmentname)
    equipmentnotes_entry.delete(0,'end')
    equipmentquantity_combo.current(0)
    
def equipmentremove():
    global mook_equipment
    selected_indices = equipment_listbox.curselection()
    for i in selected_indices:
        mook_equipment.pop(i)
        equipment_listbox.delete(i)

def cyberwearadd():
    global mook_cyberwear
    cyberwear = cyberweardb.find("", "name", cyberwear_combo.get())
    quantity = int(cyberwearquantity_combo.get())
    notes = cyberwearnotes_entry.get()
    cyberwearentry = cc.cyberwear(cyberwear[0][2], quantity, notes, cyberwear[0][0])
    if notes != '':
        note = "(" + notes + ")"
    else:
        note = ""
    if quantity > 1:
        cyberwearname = cyberwear[0][2] + " x" + str(quantity) + " " + note
    else:
        cyberwearname = cyberwear[0][2] + " " + note
    # check for duplicate entry and replace if found
    position = -1
    for index,cyberwear in enumerate(mook_cyberwear):
        if cyberwear.name == cyberwearentry.name and cyberwear.notes == cyberwearentry.notes:
            position = index
    if position != -1:
        mook_cyberwear[index] = cyberwearentry
        cyberwear_listbox.delete(position)
        cyberwear_listbox.insert(position, cyberwearname)
    else:
        mook_cyberwear.append(cyberwearentry)
        cyberwear_listbox.insert(tk.END, cyberwearname)
    cyberwearnotes_entry.delete(0,'end')
    cyberwearquantity_combo.current(0)

def cyberwearremove():
    global mook_cyberwear
    selected_indices = cyberwear_listbox.curselection()
    for i in selected_indices:
        mook_cyberwear.pop(i)
        cyberwear_listbox.delete(i)

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

# Declare and load databases
mookdb = orm.orm("cpr.mooks")
mooktypedb = orm.orm("cpr.mook_type")
typedb = orm.orm("cpr.type")
weapondb = orm.orm("cpr.weapons")
skilldb = orm.orm("cpr.skills")
equipmentdb = orm.orm("cpr.equipment")
cyberweardb = orm.orm("cpr.cyberwear")
armourdb = orm.orm("cpr.armour")
weaponqualitydb = orm.orm("cpr.weapon_quality")
mookstatdb = orm.orm("cpr.mook_stat")
mookheadarmourdb = orm.orm("cpr.mook_head_armour")
mookbodyarmourdb = orm.orm("cpr.mook_body_armour")
mookweapondb = orm.orm("cpr.mook_weapon")
mookskilldb = orm.orm("cpr.mook_skill")
mookequipmentdb = orm.orm("cpr.mook_equipment")
mookcyberweardb = orm.orm("cpr.mook_cyberwear")
statsdb = orm.orm("cpr.stats")

mooktype_v = tk.StringVar()
mooktype_combo = ttk.Combobox(win, width = 20, textvariable = mooktype_v)
mooktype = mooktypedb.find("name") 
mooktypes = []
for mook in mooktype:
    mooktypes.append(mook[0])
mooktype_combo['values'] = mooktypes
mooktype_combo['state'] = 'readonly'
mooktype_combo.current(0)
mooktype_combo.place(x=560, y=15)
mooktype_label = tk.Label(win, text="Mook Type:", font=("Arial", 12), bg='#fff', fg='#000')
mooktype_label.place(x=440, y=15)
type_label = tk.Label(win, text="Type:", font=("Arial", 12), bg='#fff', fg='#000')
type_label.place(x=10, y=15)
type_v = tk.StringVar()
type_v.trace_add('write', change_type)
type_combo = ttk.Combobox(win, width = 5, textvariable = type_v)
mastertypes = typedb.find("name") 
# mastertypes = []
# for master in mastertype:
#     mastertypes.append(master[0])
type_combo['values'] = mastertypes
type_combo['state'] = 'readonly'
type_combo.current(0)
type_combo.place(x=100, y=15)
name_label = tk.Label(win, text="Name:", font=("Arial", 12), bg='#fff', fg='#000')
name_label.place(x=10, y=55)
mookname_entry = tk.Entry(win, width=20, font=("Arial", 12), bg='#fff', fg='#000')
mookname_entry.place(x=100, y=55)
rep_label = tk.Label(win, text="Rep:", font=("Arial", 12), bg='#fff', fg='#000')
rep_label.place(x=310, y=55)
rep_v = tk.StringVar() 
rep_combo = ttk.Combobox(win, width = 2, textvariable = rep_v) 
rep_combo['values'] = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
rep_combo['state'] = 'readonly'
rep_combo.current(0)
role_entry = tk.Entry(win, width=35, font=("Arial", 12), bg='#fff', fg='#000')
role_entry.insert(0, "none")
role_entry.place(x=100, y=82)
role_label = tk.Label(win, text="Role Ability:", font=("Arial", 12), bg='#fff', fg='#000')
role_label.place(x=10, y=82)
location_label = tk.Label(win, text="Location:", font=("Arial", 12), bg='#fff', fg='#000')
location_label.place(x=310, y=110)
location_entry = tk.Entry(win, width=20, font=("Arial", 12), bg='#fff', fg='#000')
location_entry.place(x=435, y=110)

seriouslywoundedlabel = tk.Label(win, text="SERIOUSLY WOUNDED", font=("Arial", 8, "bold"), bg='#fff', fg='#000', wraplength=100, justify="left")
seriouslywoundedlabel.place(x=510, y=47)
mookseriouslywounded_label = tk.Label(win, text="10", font=("Arial", 12), bg='#fff', fg='#000')
mookseriouslywounded_label.place(x=640, y=55)
deathsavelabel = tk.Label(win, text="DEATH SAVE", font=("Arial", 8, "bold"), bg='#fff', fg='#000', wraplength=100, justify="left")
deathsavelabel.place(x=510, y=85)
mookdeathsave_label = tk.Label(win, text="2", font=("Arial", 12), bg='#fff', fg='#000')
mookdeathsave_label.place(x=640, y=82)
hplabel = tk.Label(win, text="HP", font=("Arial", 14, "bold"), bg='#fff', fg='#000')
hplabel.place(x=687, y=36)
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
will_value.trace_add('write', calc_hp)
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
body_value.trace_add('write', calc_hp)
body_combo = ttk.Combobox(win, width = 2, textvariable = body_value)
body_combo['values'] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]
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
armour_label = tk.Label(win, text="ARMOR", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
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
canvas.create_text(26, 264, text="HEAD", font=("Arial", 10, "bold"), fill='#ffffff', angle=90, anchor="w")
canvas.create_text(26, 308, text="BODY", font=("Arial", 10, "bold"), fill='#ffffff', angle=90, anchor="w")
# SP labels
headsp_label = tk.Label(win, text="4", font=("Arial", 10, "bold"), bg='#fff', fg='#000')
headsp_label.place(x=335, y=232)
bodysp_label = tk.Label(win, text="4", font=("Arial", 10, "bold"), bg='#fff', fg='#000')
bodysp_label.place(x=335, y=280)
# armour combo boxes
armours = armourdb.find("name")
armour_names = []
for armour in armours:
    armour_names.append(armour[0]) 
headsp_var = tk.StringVar()
headsp_var.trace_add('write', change_armour)
bodysp_var = tk.StringVar()
bodysp_var.trace_add('write', change_armour)
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
# tech upgrade checkboxes
headtup_var = tk.IntVar()
headtup_check = tk.Checkbutton(win, text="Tech Upgraded", variable=headtup_var, onvalue=1, offvalue=0, bg='#fff', fg='#000')
headtup_check.place(x=400, y=232)
bodytup_var = tk.IntVar()
bodytup_check = tk.Checkbutton(win, text="Tech Upgraded", variable=bodytup_var, onvalue=1, offvalue=0, bg='#fff', fg='#000')
bodytup_check.place(x=400, y=280)
# weapon divider
rectangle = canvas.create_rectangle(15, 320, 135, 345, fill="#a32", outline="#a32", width=3)
# weapon cut out
canvas.create_line(131, 317, 151, 347, fill="#fff", width=7)
# weapon Divider
canvas.create_line(15, 347, 818, 347, fill="#000", width=2)
weapon_label = tk.Label(win, text="WEAPONS", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
weapon_label.place(x=15, y=320)
# weapon controls
weapons = weapondb.find("name")
qualities = weaponqualitydb.find("name")
weapon_list = []
for weapon in weapons:
    weapon_list.append(weapon[0])
weapon_listbox = tk.Listbox(win, height=3, width=20, font=("Arial", 12), bg='#fff', fg='#000')
weapon_listbox.place(x=10, y=360)
weapon_scrollbar = ttk.Scrollbar(win, orient="vertical", command=weapon_listbox.yview)
weapon_listbox['yscrollcommand'] = weapon_scrollbar.set
weapon_scrollbar.pack(side="right", fill="y")
weapon_scrollbar.place(x=192, y=360, height=61)
# Weapon Combos
weapon_quality = weaponqualitydb.find("name")
weaponquality_value = tk.StringVar()
weaponquality_combo = ttk.Combobox(win, width = 20, textvariable = weaponquality_value)
weaponquality_combo['values'] = weapon_quality
weaponquality_combo['state'] = 'readonly'
weaponquality_combo.current(0)
weaponquality_combo.place(x=230, y=380)
weaponquality_label = tk.Label(win, text="Weapon Quality", font=("Arial", 10), bg='#fff', fg='#000')
weaponquality_label.place(x=230, y=355)
weapons = weapondb.find("name")
weapon_names = []
for weapon in weapons:
    weapon_names.append(weapon[0])
weapon_value = tk.StringVar()
weapon_combo = ttk.Combobox(win, width = 20, textvariable = weapon_value)
weapon_combo['values'] = weapon_names
weapon_combo['state'] = 'readonly'
weapon_combo.current(0)
weapon_combo.place(x=400, y=380)
weaponname_label = tk.Label(win, text="Weapon Name", font=("Arial", 10), bg='#fff', fg='#000')
weaponname_label.place(x=400, y=355)
weaponadd_button = tk.Button(win, text="Add", font=("Arial", 10), bg='#a32', fg='#fff', command=weaponadd)
weaponadd_button.place(x=600, y=380)
weaponremove_button = tk.Button(win, text="Remove", font=("Arial", 10), bg='#a32', fg='#fff', command=weaponremove)
weaponremove_button.place(x=650, y=380)
# skills divider
rectangle = canvas.create_rectangle(15, 428, 135, 453, fill="#a32", outline="#a32", width=3)
# skills cut out
canvas.create_line(131, 425, 151, 455, fill="#fff", width=7)
# skills Divider
canvas.create_line(15, 455, 818, 455, fill="#000", width=2)
skilllabel = tk.Label(win, text="SKILL BASES", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
skilllabel.place(x=15, y=428)
# skills
display_skills = []
skill_list_items =tk.Variable(win, value=display_skills)
skills_listbox = tk.Listbox(win, listvariable=skill_list_items, height=8, width=20, font=("Arial", 12), bg='#fff', fg='#000')
skills_listbox.bind("<<ListboxSelect>>", on_skill_select) 
skills_listbox.place(x=10, y=460)
skills_scrollbar = ttk.Scrollbar(win, orient="vertical", command=skills_listbox.yview)
skills_listbox.configure(yscrollcommand=skills_scrollbar.set)
skills_scrollbar.pack(side="right", fill="y")
skills_scrollbar.place(x=192, y=460, height=155)
# Skills combo
skills = skilldb.find("name", "", "", "name")
skill_names = []
for skill in skills:
    skill_names.append(skill[0])
skill_name = tk.StringVar()
skill_combo = ttk.Combobox(win, width = 25, textvariable = skill_name)
skill_combo['values'] = skill_names
skill_combo['state'] = 'readonly'
skill_combo.current(0)
skill_combo.place(x=230, y=500)
skillname_label = tk.Label(win, text="Skill Name", font=("Arial", 10), bg='#fff', fg='#000')
skillname_label.place(x=230, y=475)
skill_value = tk.StringVar()
skillvalue_combo = ttk.Combobox(win, width = 2, textvariable = skill_value)
skillvalue_combo['values'] = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
skillvalue_combo['state'] = 'readonly'
skillvalue_combo.current(0)
skillvalue_combo.place(x=425, y=500)
skillvalue_label = tk.Label(win, text="Value", font=("Arial", 10), bg='#fff', fg='#000')
skillvalue_label.place(x=425, y=475)
skillnotes_label = tk.Label(win, text="Notes", font=("Arial", 10), bg='#fff', fg='#000')
skillnotes_label.place(x=230, y=535)
skillnotes_entry = tk.Entry(win, width=30, font=("Arial", 10), bg='#fff', fg='#000')
skillnotes_entry.place(x=280, y=535)
skilladd_button = tk.Button(win, text="Add", font=("Arial", 10), bg='#a32', fg='#fff', command=skilladd)
skilladd_button.place(x=600, y=500)
skillremove_button = tk.Button(win, text="Remove", font=("Arial", 10), bg='#a32', fg='#fff', command=skillremove)
skillremove_button.place(x=650, y=500)
# equipment divider
rectangle = canvas.create_rectangle(15, 620, 135, 645, fill="#a32", outline="#a32", width=3)
# equipment cut out
canvas.create_line(131, 617, 151, 643, fill="#fff", width=7)
# equipment Divider
canvas.create_line(15, 647, 818, 647, fill="#000", width=2)
equiplabel = tk.Label(win, text="EQUIPMENT", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
equiplabel.place(x=15, y=620)
# equipment
equipment = equipmentdb.find("name", "display", "y", "name")   
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
# equipment combo
# equipment = db.orderedselectedfindall(EQUIPMENTDB, "name", "display", "y", "name")
equipment_names = []
for equip in equipment:
    equipment_names.append(equip[0])
equipment_value = tk.StringVar()
equipment_combo = ttk.Combobox(win, width = 20, textvariable = equipment_value)
equipment_combo['values'] = equipment_names
equipment_combo['state'] = 'readonly'
equipment_combo.current(0)
equipment_combo.place(x=230, y=680)
equipmentname_label = tk.Label(win, text="Equipment Name", font=("Arial", 10), bg='#fff', fg='#000')
equipmentname_label.place(x=230, y=655)
equipmentquantity_label = tk.Label(win, text="Quantity", font=("Arial", 10), bg='#fff', fg='#000')
equipmentquantity_label.place(x=425, y=655)
equipment_quantityvalue = []
for i in range(1, 101):
    equipment_quantityvalue.append(i)
equipment_quantity = tk.StringVar()
equipmentquantity_combo = ttk.Combobox(win, width = 2, textvariable = equipment_quantity)
equipmentquantity_combo['values'] = equipment_quantityvalue
equipmentquantity_combo['state'] = 'readonly'
equipmentquantity_combo.current(0)
equipmentquantity_combo.place(x=425, y=680)
equipmentnotes_label = tk.Label(win, text="Notes", font=("Arial", 10), bg='#fff', fg='#000')
equipmentnotes_label.place(x=230, y=710)
equipmentnotes_entry = tk.Entry(win, width=30, font=("Arial", 10), bg='#fff', fg='#000')
equipmentnotes_entry.place(x=280, y=710)
equipmentadd_button = tk.Button(win, text="Add", font=("Arial", 10), bg='#a32', fg='#fff', command=equipmentadd)
equipmentadd_button.place(x=600, y=680)
equipmentremove_button = tk.Button(win, text="Remove", font=("Arial", 10), bg='#a32', fg='#fff', command=equipmentremove)
equipmentremove_button.place(x=650, y=680)
# Cyberwear divider
rectangle = canvas.create_rectangle(15, 735, 135, 760, fill="#a32", outline="#a32", width=3)
# Cyberwear cut out
canvas.create_line(131, 732, 151, 758, fill="#fff", width=7)
# Cyberwear Divider
canvas.create_line(15, 762, 818, 762, fill="#000", width=2)
cyberlabel = tk.Label(win, text="CYBERWEAR", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
cyberlabel.place(x=15, y=732)
# Cyberwear
cyberwear_list_items =tk.Variable()
cyberwear_listbox = tk.Listbox(win, listvariable=cyberwear_list_items, height=4, width=20, font=("Arial", 12), bg='#fff', fg='#000')
cyberwear_listbox.place(x=10, y=770)
cyberwear_scrollbar = ttk.Scrollbar(win, orient="vertical", command=cyberwear_listbox.yview)
cyberwear_listbox.configure(yscrollcommand=cyberwear_scrollbar.set)
cyberwear_scrollbar.pack(side="right", fill="y")
cyberwear_scrollbar.place(x=192, y=770, height=79)
# Cyberwear combo
cyberwear = cyberweardb.find("name", "", "", "name")
cyberwear_names = []
for cyber in cyberwear:
    cyberwear_names.append(cyber[0])
cyberwear_value = tk.StringVar()
cyberwear_combo = ttk.Combobox(win, width = 20, textvariable = cyberwear_value)
cyberwear_combo['values'] = cyberwear_names
cyberwear_combo['state'] = 'readonly'
cyberwear_combo.current(0)
cyberwear_combo.place(x=230, y=800)
cyberwearname_label = tk.Label(win, text="Cyberwear Name", font=("Arial", 10), bg='#fff', fg='#000')
cyberwearname_label.place(x=230, y=775)
cyberwearquantity_label = tk.Label(win, text="Quantity", font=("Arial", 10), bg='#fff', fg='#000')  
cyberwearquantity_label.place(x=425, y=775)
cyberwear_quantity = tk.StringVar()
cyberwearquantity_combo = ttk.Combobox(win, width = 2, textvariable = cyberwear_quantity)
cyberwearquantity_combo['values'] = [1,2]
cyberwearquantity_combo['state'] = 'readonly'
cyberwearquantity_combo.current(0)
cyberwearquantity_combo.place(x=425, y=800)
cyberwearnotes_label = tk.Label(win, text="Notes", font=("Arial", 10), bg='#fff', fg='#000')
cyberwearnotes_label.place(x=230, y=830)
cyberwearnotes_entry = tk.Entry(win, width=30, font=("Arial", 10), bg='#fff', fg='#000')
cyberwearnotes_entry.place(x=280, y=830)
cyberwearadd_button = tk.Button(win, text="Add", font=("Arial", 10), bg='#a32', fg='#fff', command=cyberwearadd)
cyberwearadd_button.place(x=600, y=800)
cyberwearremove_button = tk.Button(win, text="Remove", font=("Arial", 10), bg='#a32', fg='#fff', command=cyberwearremove)
cyberwearremove_button.place(x=650, y=800)
# buttons
save_button = tk.Button(win, text="SAVE", font=("Arial", 12, "bold"), bg='#a32', fg='#fff', command=save)
save_button.place(x=10, y=855)
clear_button = tk.Button(win, text="CLEAR", font=("Arial", 12, "bold"), bg='#a32', fg='#fff', command=clear)
clear_button.place(x=100, y=855)

clear()

win.mainloop()