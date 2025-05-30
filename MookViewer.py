import tkinter as tk
import databaseTools
import numbers
import mook
import tkinter as tk
from tkinter import ttk 
import math

# TODO add type combo box for type (mook, NPC, PC)
# TODO potential add combo box for mook type (mook, hardened mook, etc)

MOOKDB = "cpr.mooks"
MOOKTYPEDB = "cpr.mook_type"
TYPEDB = "cpr.type"
WEAPONDB = "cpr.weapons"
SKILLDB = "cpr.skills"
EQUIPMENTDB = "cpr.equipment"
CYBERWEARDB = "cpr.cyberwear"
ARMOURDB = "cpr.armour"
WEAPONQUALITYDB = "cpr.weapon_quality"
MOOKSTATDB = "cpr.mook_stat"
MOOKHEADARMOURDB = "cpr.mook_head_armour"
MOOKBODYARMOURDB = "cpr.mook_body_armour"
MOOKWEAPONDB = "cpr.mook_weapon"
MOOKSKILLDB = "cpr.mook_skill"
MOOKEQUIPMENTDB = "cpr.mook_equipment"
MOOKCYBERWEARDB = "cpr.mook_cyberwear"
STATSDB = "cpr.stats"

weaponlist = []

def loadbasemook(id, newmook):
    # complexity 20/15
    mookentry = dbt.find(MOOKDB, "id", str(id))[0]
    attributes = dbt.describe(MOOKDB)
    for index,attribute in enumerate(attributes):  
        if isinstance(mookentry[index], numbers.Number):
            value = mookentry[index]
            if attribute[0] == "mook_type":
                temptype = dbt.find(MOOKTYPEDB,"id", str(value))
                newmook.mooktype = temptype[0][1]
            if attribute[0] == "type" and value != "1":
                temptype = dbt.find(TYPEDB,"id", str(value))
                newmook.mooktype = temptype[0][1]
            if attribute[0] == "rep":
                newmook.rep = mookentry[index]
        else:
            if attribute[0] == "name":
                newmook.name = mookentry[index]
            if attribute[0] == "location":
                newmook.location = mookentry[index]
            if attribute[0] == "role":
                newmook.role = mookentry[index]
    return newmook

def loadmookarmour(id, newmook):
    headarm = dbt.find(MOOKHEADARMOURDB,"mookid", str(id))
    harmourtype = dbt.find(ARMOURDB,"id", str(headarm[0][2]))
    bodyarm = dbt.find(MOOKBODYARMOURDB,"mookid", str(id))
    barmourtype = dbt.find(ARMOURDB,"id", str(bodyarm[0][2]))
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
    newmook.headarmour = [headarmourname, str(headsp)]
    newmook.bodyarmour = [bodyarmourname, str(bodysp)]
    newmook.armourmodifier = int(barmourtype[0][3])
    return newmook

def loadmookstats(id, newmook):
    stats = dbt.find(MOOKSTATDB, "mookid", str(id))
    stattitles = dbt.findall(STATSDB)
    mookstats = {}
    for index,stat in enumerate(stats):
        mod = 0
        for stattitle in stattitles:
            if stattitle[0] == stat[2]:
                statname = stattitle[1]
                if stattitle[2] == "y":
                    mod = 1
            statvalue = stat[3]
        if(mod == 1 and newmook.armourmodifier != 0):
            modvalue = int(statvalue) - int(newmook.armourmodifier)
            mookstats[statname] = str(stat[3]) + " (" + str(modvalue) + ")"
        else:
            mookstats[statname] = stat[3]
    newmook.stats = mookstats
    return newmook

def loadmookweapons(id, newmook):
    # complexity 22/15
    weapontypes = dbt.findall(WEAPONDB)
    qualitytypes = dbt.findall(WEAPONQUALITYDB)
    weapons = dbt.find(MOOKWEAPONDB,"mookid", str(id))
    weaponlist = []
    for index, weapon in enumerate(weapons):
        for weapontype in weapontypes:
            if weapontype[0] == weapon[2]:
                for quality in qualitytypes:
                    if quality[0] == weapon[3]:
                        if quality[0] != 1:
                            weaponname = quality[1] + " Quality " + weapontype[1]
                        else :
                            weaponname = weapontype[1]
                        weaponlist.append(weaponname)
    newmook.weapons = weaponlist
    return newmook

def loadmookskills(id, newmook):
    mookskills = {}
    skilltitles = dbt.findall(SKILLDB)
    skills = dbt.find(MOOKSKILLDB,"mookid", str(id))
    for index,skill in enumerate(skills):
        for skilltitle in skilltitles:
            if skilltitle[0] == skill[2]:
                if newmook.armourmodifier != 0 and skilltitle[5] == "y":
                    value = skill[3] + " (" + str(int(skill[3]) - int(newmook.armourmodifier)) + ")"
                else:
                    value = skill[3]
                if skill[4] != None and skill[4] != "":
                    key = str(skilltitle[1]) + " (" + skill[4] + ")" 
                else:
                    key = skilltitle[1]
                mookskills[key] = value
    newmook.skills = mookskills
    return newmook

def loadmookequipment(id, newmook):
    # complexity 16/15
    equipmenttable = dbt.findall(EQUIPMENTDB)
    equipment = dbt.find(MOOKEQUIPMENTDB,"mookid", str(id))
    mookequipment = []
    for index, equipment in enumerate(equipment):
        for equipmenttitle in equipmenttable:
            if equipmenttitle[0] == equipment[2]:
                printstr = equipmenttitle[2]
                if equipment[3] != '0' and equipment[3] != '1':
                    printstr += " x" + str(equipment[3])
                if equipment[4] != None and equipment[4] != "":
                    printstr += " (" + str(equipment[4]) + ")"
                mookequipment.append(printstr)
    newmook.equipment = mookequipment
    return newmook

def loadmookcyberwear(id, newmook):
    # complexity 16/15
    cyberweartable = dbt.findall(CYBERWEARDB)
    cyberwear = dbt.find(MOOKCYBERWEARDB,"mookid", str(id))
    mookcyberwear = []
    for index, cyberwear in enumerate(cyberwear):
        for cyberweartitle in cyberweartable:
            if cyberweartitle[0] == cyberwear[2]:
                printstr = cyberweartitle[2]
                if cyberwear[3] != '0' and cyberwear[3] != '1':
                    printstr += " x" + str(cyberwear[3])
                if cyberwear[4] != None and cyberwear[4] != "":
                    printstr += " (" + str(cyberwear[4]) + ")"
                mookcyberwear.append(printstr)
    newmook.cyberwear = mookcyberwear
    return newmook

def loadmooks(id):
    newmook = mook.mook("", "", 0, {}, {}, {}, [], "", {}, [], [], "", 0, id)
    newmook = loadbasemook(id, newmook)
    newmook = loadmookarmour(id, newmook)
    newmook = loadmookstats(id, newmook)
    newmook = loadmookweapons(id, newmook)
    newmook = loadmookskills(id, newmook)
    newmook = loadmookequipment(id, newmook)
    newmook = loadmookcyberwear(id, newmook)
    return newmook

def display_mook(mookposition):
    mooks[mookposition].display()

def get_index(*arg):
    mookrole_label['text'] = mooks[mookchoosen.current()].role
    mookrep_label['text'] = mooks[mookchoosen.current()].rep
    hp = mooks[mookchoosen.current()].gethp()
    seriouslywounded = math.ceil(hp/2)
    mookseriouslywounded_label['text'] = seriouslywounded
    mookdeathsave_label['text'] = mooks[mookchoosen.current()].stats.get('Body')
    mookhp_label['text'] = hp
    stats = mooks[mookchoosen.current()].stats
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
    weaponlist = mooks[mookchoosen.current()].weapons
    mookweaponchoosen['value'] = tuple(weaponlist)
    mookweaponchoosen.current(0)
    mookarmourhead_label['text'] = mooks[mookchoosen.current()].headarmour[0]
    mookarmourheadsp_label['text'] = mooks[mookchoosen.current()].headarmour[1]
    mookarmourbody_label['text'] = mooks[mookchoosen.current()].bodyarmour[0]
    mookarmourbodysp_label['text'] = mooks[mookchoosen.current()].bodyarmour[1]
    mookskilllist = mooks[mookchoosen.current()].skills
    count = 1
    mookskilldisplay = ''
    for x,y in mookskilllist.items():
        mookskilldisplay += x + " " + y
        if count != len(mookskilllist):
            mookskilldisplay += " • "
        count += 1
    mookskills_label['text'] = mookskilldisplay
    mookequipmentlist = mooks[mookchoosen.current()].equipment
    count = 1
    mookequipmentdisplay = ''
    for x in mookequipmentlist:
        mookequipmentdisplay += x
        if count != len(mookequipmentlist):
            mookequipmentdisplay +=  " • "
        count += 1
    if mookequipmentdisplay == '':
        mookequipmentdisplay = "None"
    mookequipment_label['text'] = mookequipmentdisplay
    mookcyberwearlist = mooks[mookchoosen.current()].cyberwear
    count = 1
    mookcyberwaredisplay = ''
    for x in mookcyberwearlist:
        mookcyberwaredisplay += x
        if count != len(mookcyberwearlist):
            mookcyberwaredisplay += " • "
        count += 1
    if mookcyberwaredisplay == '':
        mookcyberwaredisplay = "None"
    mookcyberwear_label['text'] = mookcyberwaredisplay
            
def get_weapons(*arg):
    tempweaponname = mookweaponchoosen.get()
    strippoor = tempweaponname.lstrip("Poor Quality ")
    weaponname = strippoor.lstrip("Excelent Quality ")
    weaponprofile = dbt.find(WEAPONDB, "name", weaponname)[0]
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
mooktable = dbt.find(MOOKDB, "type", "1")
# mooktable = dbt.findall(MOOKDB)

# for index,entry in enumerate(mooktable):
#     mooks.append(loadmooks(index+1))
for i in range(len(mooktable)):
    mooks.append(loadmooks(mooktable[i][0]))
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
    mooklist.append(mook.name)

mookchoosen['values'] = tuple(mooklist) 
mookchoosen['state'] = 'readonly'
mookchoosen.current(0)

win.mainloop()