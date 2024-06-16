import tkinter as tk
import databaseTools
import numbers
import mook
import tkinter as tk
from tkinter import ttk 

weaponlist = []

def loadmooks(id):
    mookentry = dbt.find("cpr.mooks", "id", str(id))[0]
    attributes = dbt.describe("cpr.mooks")
    armourmodifier = 0
    mooktype = ''
    for index,attribute in enumerate(attributes):  
        if isinstance(mookentry[index], numbers.Number):
            value = mookentry[index]
            if attribute[0] == "mook_type":
                temptype = dbt.find("cpr.mook_type","id", str(value))
                mooktype = temptype[0][1]
            if attribute[0] == "type":
                if value != "1":
                    temptype = dbt.find("cpr.type","id", str(value))
                    mooktype = temptype[0][1]
            if attribute[0] == "rep":
                rep = mookentry[index]
        else:
            if attribute[0] == "name":
                mookname = mookentry[index]
            if attribute[0] == "location":
                mooklocation = mookentry[index]
    headarm = dbt.find("cpr.mook_head_armour","mookid", str(id))
    harmourtype = dbt.find("cpr.armour","id", str(headarm[0][2]))
    bodyarm = dbt.find("cpr.mook_body_armour","mookid", str(id))
    barmourtype = dbt.find("cpr.armour","id", str(bodyarm[0][2]))
    if headarm[0][3] == "y":
        headsp = int(harmourtype[0][2]) + 1
        headarmourname = "(TUp) " + harmourtype[0][1]
    else:
        headsp = harmourtype[0][2]
        headarmourname = harmourtype[0][1]
    if bodyarm[0][3] == "y":
        bodyarmourname = "(TUp) " +barmourtype[0][1]
        bodysp = int(barmourtype[0][2]) + 1
    else:
        bodysp = barmourtype[0][2]
        bodyarmourname = barmourtype[0][1]
    mookheadarmour = [headarmourname, str(headsp)]
    mookbodyarmour = [bodyarmourname, str(bodysp)]
    armourmodifier = int(barmourtype[0][3])

    stats = dbt.find("cpr.mook_stat", "mookid", str(id))
    statTitles = dbt.findall("cpr.stats")
    mookstats = {}
    for index,stat in enumerate(stats):
        mod = 0
        for statTitle in statTitles:
            if statTitle[0] == stat[2]:
                statName = statTitle[1]
                if statTitle[1] == "Will":
                    will = stat[3]
                if statTitle[1] == "Body":
                    body = stat[3]  
                if statTitle[2] == "y":
                    mod = 1
            statvalue = stat[3]
        if(mod == 1 and armourmodifier != 0):
            modvalue = int(statvalue) - int(armourmodifier)
            mookstats[statName] = str(stat[3]) + " (" + str(modvalue) + ")"
        else:
            mookstats[statName] = stat[3]
    weaponTypes = dbt.findall("cpr.weapons")
    qualityTypes = dbt.findall("cpr.weapon_quality")
    weapons = dbt.find("cpr.mook_weapon","mookid", str(id))
    weaponlist = []
    for index,weapon in enumerate(weapons):
        for weaponType in weaponTypes:
            if weaponType[0] == weapon[2]:
                for quality in qualityTypes:
                    if quality[0] == weapon[3]:
                        if quality[0] != 1:
                            weaponname = quality[1] + " Quality " + weaponType[1]
                        else :
                            weaponname = weaponType[1]
                        weaponlist.append(weaponname)
    roleTitle = dbt.findall("cpr.roles")
    roles = dbt.find("cpr.mook_role","mookid", str(id))
    mookrole = ''
    mookskills = {}
    for index,role in enumerate(roles):
        for roleTitle in roleTitle:
            if roleTitle[0] == role[2]:
                mookrole = roleTitle[2]
                if role[2] != 1:
                    mookroleskill = role[3]
                    if role[4] != None:
                        mookroleskill += " (" + role[4] + ")"
                    mookskills[roleTitle[1]] = mookroleskill
    skillTitles = dbt.findall("cpr.skills")
    skills = dbt.find("cpr.mook_skill","mookid", str(id))
    for index,skill in enumerate(skills):
        for skillTitle in skillTitles:
            if skillTitle[0] == skill[2]:
                if armourmodifier != 0 and skillTitle[5] == "y":
                    value = skill[3] + " (" + str(int(skill[3]) - int(armourmodifier)) + ")"
                else:
                    value = skill[3]
                if skill[4] != None:
                    key = str(skillTitle[1]) + " (" + skill[4] + ")" 
                else:
                    key = skillTitle[1]
                mookskills[key] = value
    equipmentTable = dbt.findall("cpr.equipment")
    equipment = dbt.find("cpr.mook_equipment","mookid", str(id))
    mookequipment = []
    for index,equipment in enumerate(equipment):
        for equipmentTitle in equipmentTable:
            if equipmentTitle[0] == equipment[2]:
                printStr = equipmentTitle[2]
                if equipment[3] != '0':
                    printStr += " x" + str(equipment[3])
                if equipment[4] != None:
                    printStr += " (" + str(equipment[4]) + ")"
                mookequipment.append(printStr)
    cyberwearTable = dbt.findall("cpr.cyberwear")
    cyberwear = dbt.find("cpr.mook_cyberwear","mookid", str(id))
    mookcyberwear = []
    for index,cyberwear in enumerate(cyberwear):
        for cyberwearTitle in cyberwearTable:
            if cyberwearTitle[0] == cyberwear[2]:
                printStr = cyberwearTitle[2]
                if cyberwear[3] != '0':
                    printStr += " x" + str(cyberwear[3])
                if cyberwear[4] != None:
                    printStr += " (" + str(cyberwear[4]) + ")"
                mookcyberwear.append(printStr)
    newmook = mook.mook(mookname, mooktype, rep, mookheadarmour, mookbodyarmour, mookstats, weaponlist, mookrole, mookskills, mookequipment, mookcyberwear, mooklocation, will, body, armourmodifier)
    return newmook

def display_mook(mookposition):
    mooks[mookposition].display()

def get_index(*arg):
    mookrole_label['text'] = mooks[mookchoosen.current()].getRole()
    mookrep_label['text'] = mooks[mookchoosen.current()].getRep()
    mookseriouslywounded_label['text'] = mooks[mookchoosen.current()].getSeriouslyWounded()
    mookdeathsave_label['text'] = mooks[mookchoosen.current()].getDeathSave()
    mookhp_label['text'] = mooks[mookchoosen.current()].getHP()
    stats = mooks[mookchoosen.current()].getStats()
    mookint_label['text'] = stats.get('Int')
    mookref_label['text'] = stats.get('Ref')
    mookdex_label['text'] = stats.get('Dex')
    mooktech_label['text'] = stats.get('Tech')
    mookcool_label['text'] = stats.get('Cool')
    mookluck_label['text'] = stats.get('Luck')
    mookwill_label['text'] = stats.get('Will')
    mookmove_label['text'] = stats.get('Move')
    mookbody_label['text'] = stats.get('Body')
    mookemp_label['text'] = stats.get('Emp')
    global weaponlist
    weaponlist = mooks[mookchoosen.current()].getWeapons()
    mookweaponchoosen['value'] = tuple(weaponlist)
    mookweaponchoosen.current(0)
    mookarmourhead_label['text'] = mooks[mookchoosen.current()].getHeadArmour()[0]
    mookarmourheadsp_label['text'] = mooks[mookchoosen.current()].getHeadArmour()[1]
    mookarmourbody_label['text'] = mooks[mookchoosen.current()].getBodyArmour()[0]
    mookarmourbodysp_label['text'] = mooks[mookchoosen.current()].getBodyArmour()[1]
    mookskilllist = mooks[mookchoosen.current()].getSkills()
    count = 1
    mookskilldisplay = ''
    for x,y in mookskilllist.items():
        mookskilldisplay += x + " " + y
        if count != len(mookskilllist):
            mookskilldisplay += " • "
        count += 1
    mookskills_label['text'] = mookskilldisplay
    mookequipmentlist = mooks[mookchoosen.current()].getEquipment()
    count = 1
    mookequipmentdisplay = ''
    for x in mookequipmentlist:
        mookequipmentdisplay += x
        if count != len(mookequipmentlist):
            mookequipmentdisplay +=  " • "
        count += 1
    mookequipment_label['text'] = mookequipmentdisplay
    mookcyberwearlist = mooks[mookchoosen.current()].getCyberwear()
    count = 1
    mookcyberwaredisplay = ''
    for x in mookcyberwearlist:
        mookcyberwaredisplay += x
        if count != len(mookcyberwearlist):
            mookcyberwaredisplay += " • "
        count += 1
    mookcyberwear_label['text'] = mookcyberwaredisplay
            
def get_weapons(*arg):
    tempweaponname = mookweaponchoosen.get()
    strippoor = tempweaponname.lstrip("Poor Quality ")
    weaponname = strippoor.lstrip("Excelent Quality ")
    weaponprofile = dbt.find("cpr.weapons", "name", weaponname)[0]
    rof_label['text'] = weaponprofile[3]
    damage_label['text'] = weaponprofile[2] + "D6"


# Build UI        
win = tk.Tk()
win.title("Cyberpunk Red Mook Viewer")
canvas = tk.Canvas(win, width=830, height=645, bg="white")

# Shadow Box
rectangle = canvas.create_rectangle(9, 9, 829, 644, fill="#ddd", outline="#ddd", width=2)
# Border Box
rectangle = canvas.create_rectangle(5, 5, 825, 640, fill="white", outline="#ccc", width=2)
# Name Box
rectangle = canvas.create_rectangle(15, 15, 400, 65, fill="white", outline="#a32", width=3)
# Rep Box
rectangle = canvas.create_rectangle(405, 15, 500, 65, fill="white", outline="#a32", width=3)
# Role Box
rectangle = canvas.create_rectangle(15, 70, 500, 120, fill="white", outline="#a32", width=3)
# Seriously Wounded Box
canvas.create_line(505, 15, 665, 15, fill="#a32", width=3)
canvas.create_line(505, 65, 690, 65, fill="#a32", width=3)
canvas.create_line(505, 15, 505, 65, fill="#a32", width=3)
canvas.create_line(665, 15, 690, 65, fill="#a32", width=3)
# Death Save Box
canvas.create_line(505, 70, 691, 70, fill="#a32", width=3)
canvas.create_line(505, 120, 719, 120, fill="#a32", width=3)
canvas.create_line(505, 70, 505, 120, fill="#a32", width=3)
canvas.create_line(691, 70, 719, 120, fill="#a32", width=3)
# HP Label Box
canvas.create_line(670, 15, 725, 120, width=2)
canvas.create_line(725, 15, 725, 120, width=2)
canvas.create_line(670, 15, 725, 15, width=2)
# HP Box
canvas.create_line(726, 15, 813, 15, width=3, fill="#a32")
canvas.create_line(726, 120, 813, 120, width=3, fill="#a32")
canvas.create_line(813, 15, 813, 120, width=3, fill="#a32")
# Stats Label Box
rectangle = canvas.create_rectangle(15, 130, 90, 154, fill="#a32", outline="#a32", width=3) 
# Stats cut out
canvas.create_line(85, 125, 95, 140, fill="#fff", width=7)
# Stats Divider
canvas.create_line(15, 157, 818, 157, fill="#000", width=2)
# Weapon Label Box
rectangle = canvas.create_rectangle(15, 185, 110, 210, fill="#a32", outline="#a32", width=3)
# Weapon cut out
canvas.create_line(103, 175, 120, 203, fill="#fff", width=7)
# Weapon Divider
canvas.create_line(15, 213, 550, 213, fill="#000", width=2)
#armor label Box
rectangle = canvas.create_rectangle(555, 185, 640, 210, fill="#a32", outline="#a32", width=3)
# armor cut out
canvas.create_line(632, 175, 649, 203, fill="#fff", width=7)
# armor Divider
canvas.create_line(555, 213, 818, 213, fill="#000", width=2)
# head armor Box
rectangle = canvas.create_rectangle(555, 217, 566, 260, fill="#a32", outline="#a32", width=3)
# body armor Box
rectangle = canvas.create_rectangle(555, 264, 566, 306, fill="#a32", outline="#a32", width=3)
#head armour Boxes
rectangle = canvas.create_rectangle(565, 217, 740, 260, fill="#fff", outline="#a32", width=3)
rectangle = canvas.create_rectangle(745, 217, 815, 260, fill="#fff", outline="#a32", width=3)
# body armour Boxes
rectangle = canvas.create_rectangle(565, 264, 740, 306, fill="#fff", outline="#a32", width=3)
rectangle = canvas.create_rectangle(745, 264, 815, 306, fill="#fff", outline="#a32", width=3)
# weapon header Boxes
rectangle = canvas.create_rectangle(15, 219, 415, 259, fill="#a32", outline="#a32", width=3)
rectangle = canvas.create_rectangle(420, 219, 465, 259, fill="#a32", outline="#a32", width=3)
rectangle = canvas.create_rectangle(470, 219, 547, 259, fill="#a32", outline="#a32", width=3)
# weapon Boxes
rectangle = canvas.create_rectangle(15, 265, 415, 305, fill="#fff", outline="#a32", width=3)
rectangle = canvas.create_rectangle(420, 265, 465, 305, fill="#fff", outline="#a32", width=3)
rectangle = canvas.create_rectangle(470, 265, 547, 305, fill="#fff", outline="#a32", width=3)
# skills label Box
rectangle = canvas.create_rectangle(15, 313, 135, 338, fill="#a32", outline="#a32", width=3)
# skills cut out
canvas.create_line(131, 310, 151, 340, fill="#fff", width=7)
# skills Divider
canvas.create_line(15, 340, 818, 340, fill="#000", width=2)
# gear header Box
rectangle = canvas.create_rectangle(15, 455, 95, 480, fill="#a32", outline="#a32", width=3)
# gear cut out
canvas.create_line(91, 452, 111, 482, fill="#fff", width=7)
# gear Divider
canvas.create_line(15, 482, 818, 482, fill="#000", width=2)
# cyberwear header Box
rectangle = canvas.create_rectangle(15, 550, 135, 575, fill="#a32", outline="#a32", width=3)
# cyberwear cut out
canvas.create_line(130, 545, 145, 570, fill="#fff", width=7)
# cyberwear Divider
canvas.create_line(15, 576, 818, 576, fill="#000", width=2)

canvas.pack()

# Labels
namelabel = tk.Label(win, text="NAME", font=("Arial", 12, "bold"), bg='#fff', fg='#000')
namelabel.place(x=20, y=27)
rolelabel = tk.Label(win, text="ROLE", font=("Arial", 12, "bold"), bg='#fff', fg='#000')
rolelabel.place(x=20, y=82)
replabel = tk.Label(win, text="REP", font=("Arial", 12, "bold"), bg='#fff', fg='#000')
replabel.place(x=410, y=27)
seriouslywoundedlabel = tk.Label(win, text="SERIOUSLY WOUNDED", font=("Arial", 12, "bold"), bg='#fff', fg='#000', wraplength=100, justify="left")
seriouslywoundedlabel.place(x=510, y=17)
deathsavelabel = tk.Label(win, text="DEATH SAVE", font=("Arial", 12, "bold"), bg='#fff', fg='#000', wraplength=100, justify="left")
deathsavelabel.place(x=510, y=72)
hplabel = tk.Label(win, text="HP", font=("Arial", 14, "bold"), bg='#fff', fg='#000')
hplabel.place(x=687, y=16)
# Value Labels
mookrole_label = tk.Label(win, text="Mook Role", font=("Arial", 12), bg='#fff', fg='#000')
mookrole_label.place(x=80, y=82)
mookrep_label = tk.Label(win, text="rep", font=("Arial", 12), bg='#fff', fg='#000')
mookrep_label.place(x=455, y=25)
mookseriouslywounded_label = tk.Label(win, text="sw", font=("Arial", 12), bg='#fff', fg='#000')
mookseriouslywounded_label.place(x=620, y=25)
mookdeathsave_label = tk.Label(win, text="ds", font=("Arial", 12), bg='#fff', fg='#000')
mookdeathsave_label.place(x=620, y=82)
mookhp_label = tk.Label(win, text="hp", font=("Arial", 26, "bold"), bg='#fff', fg='#000')
mookhp_label.place(x=745, y=40)
# stats label
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
# Stat Value Labels
mookint_label = tk.Label(win, text="2", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mookint_label.place(x=60, y=160)
mookref_label = tk.Label(win, text="2(0)", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mookref_label.place(x=133, y=160)
mookdex_label = tk.Label(win, text="2(0)", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mookdex_label.place(x=218, y=160)
mooktech_label = tk.Label(win, text="2", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mooktech_label.place(x=305, y=160)
mookcool_label = tk.Label(win, text="2", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mookcool_label.place(x=385, y=160)
mookwill_label = tk.Label(win, text="2", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mookwill_label.place(x=465, y=160)
mookluck_label = tk.Label(win, text="2", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mookluck_label.place(x=545, y=160)
mookmove_label = tk.Label(win, text="2(0)", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mookmove_label.place(x=630, y=160)
mookbody_label = tk.Label(win, text="2", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mookbody_label.place(x=725, y=160)
mookemp_label = tk.Label(win, text="2(0)", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
mookemp_label.place(x=790, y=160)
# Weapon Label
weaponlabel = tk.Label(win, text="WEAPONS", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
weaponlabel.place(x=15, y=186)
# armour label
armourlabel = tk.Label(win, text="ARMOR", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
armourlabel.place(x=555, y=186)
# head body shield labels
canvas.create_text(560, 260, text="HEAD", font=("Arial", 10, "bold"), fill='#ffffff', angle=90, anchor="w")
canvas.create_text(560, 306, text="BODY", font=("Arial", 10, "bold"), fill='#ffffff', angle=90, anchor="w")
# weapon headers
weaponheader_label = tk.Label(win, text="WEAPON", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
weaponheader_label.place(x=15, y=235)
rofheader_label = tk.Label(win, text="ROF", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
rofheader_label.place(x=420, y=235)
damageheader_label = tk.Label(win, text="DAMAGE", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
damageheader_label.place(x=470, y=235)
rof_label = tk.Label(win, text="2", font=("Arial", 10), bg='#fff', fg='#000', justify = 'center')
rof_label.place(x=435, y=275)
damage_label = tk.Label(win, text="2", font=("Arial", 10), bg='#fff', fg='#000', justify = 'left')
damage_label.place(x=495, y=275)
# armour headers
mookarmourhead_label = tk.Label(win, text="head", font=("Arial", 12), bg='#fff', fg='#000')
mookarmourhead_label.place(x=570, y=226)
mookarmourheadsp_label = tk.Label(win, text="spec", font=("Arial", 12), bg='#fff', fg='#000')
mookarmourheadsp_label.place(x=748, y=226)
mookarmourbody_label = tk.Label(win, text="body", font=("Arial", 12), bg='#fff', fg='#000')
mookarmourbody_label.place(x=570, y=271)
mookarmourbodysp_label = tk.Label(win, text="spec", font=("Arial", 12), bg='#fff', fg='#000')
mookarmourbodysp_label.place(x=748, y=271)
# skills header label
skilllabel = tk.Label(win, text="SKILL BASES", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
skilllabel.place(x=15, y=313)
# skill label
mookskills_label = tk.Label(win, text="skills", font=("Arial", 10), wraplength=800, justify="left", bg='#fff', fg='#000')
mookskills_label.place(x=15, y=345)
# gear header label
gearlabel = tk.Label(win, text="GEAR", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
gearlabel.place(x=15, y=455)
# gear label
mookequipment_label = tk.Label(win, text="gear", font=("Arial", 10), wraplength=800, justify="left", bg='#fff', fg='#000')
mookequipment_label.place(x=15, y=485)
# cyberwear header label
cyberwearlabel = tk.Label(win, text="CYBERWEAR", font=("Arial", 12, "bold"), bg='#a32', fg='#fff')
cyberwearlabel.place(x=15, y=550)
# cyberwear label
mookcyberwear_label = tk.Label(win, text="cyberwear", font=("Arial", 10), wraplength=800, justify="left", bg='#fff', fg='#000')
mookcyberwear_label.place(x=15, y=580)

#main program start
dbt = databaseTools.databaseTools()
mooks = []
# fill array
mooktable = dbt.find("cpr.mooks", "type", "1")
# mooktable = dbt.findall("cpr.mooks")

for index,entry in enumerate(mooktable):
    mooks.append(loadmooks(index+1))

# weapon combobox
w = tk.StringVar() 
mookweaponchoosen = ttk.Combobox(win, width = 27, textvariable = w) 
w.trace_add('write', get_weapons)
mookweaponchoosen['value'] = tuple(weaponlist)
mookweaponchoosen['state'] = 'readonly'
mookweaponchoosen.place(x=20, y=275)

# name Combobox
n = tk.StringVar() 
mookchoosen = ttk.Combobox(win, width = 27, textvariable = n) 
n.trace_add('write', get_index) 
mookchoosen.place(x=80, y=28)

# name organise
mooklist = []
for mook in mooks:
    mooklist.append(mook.getName())

mookchoosen['values'] = tuple(mooklist) 
mookchoosen['state'] = 'readonly'
mookchoosen.current(0)

win.mainloop()