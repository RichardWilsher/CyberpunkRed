import databaseTools
import numbers
import mook
import tkinter as tk
from tkinter import ttk 
from PIL import ImageTk, Image

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
            if attribute[0] == "headsp" or attribute[0] == "bodysp":
                armourtype = dbt.find("cpr.armour","id", str(value))
                armourmodifier = int(armourtype[0][3])
                if attribute[0] == "headsp":
                    mookheadarmour =  [armourtype[0][1], armourtype[0][2]]
                else :
                    mookbodyarmour = [armourtype[0][1], armourtype[0][2]]
            if attribute[0] == "rep":
                rep = mookentry[index]
        else:
            if attribute[0] == "name":
                mookname = mookentry[index]
            if attribute[0] == "location":
                mooklocation = mookentry[index]

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
    mookweapons = {}
    weaponTypes = dbt.findall("cpr.weapons")
    qualityTypes = dbt.findall("cpr.weapon_quality")
    weapons = dbt.find("cpr.mook_weapon","mookid", str(id))
    for index,weapon in enumerate(weapons):
        for weaponType in weaponTypes:
            if weaponType[0] == weapon[2]:
                for quality in qualityTypes:
                    if quality[0] == weapon[3]:
                        if quality[0] != 1:
                            weaponname = quality[1] + " Quality " + weaponType[1]
                        else :
                            weaponname = weaponType[1]
                        dice = str(weaponType[2])
                        rof = weaponType[3]
                        mookweapons[weaponname] = [dice,rof]
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
    newmook = mook.mook(mookname, mooktype, rep, mookheadarmour, mookbodyarmour, mookstats, mookweapons, mookrole, mookskills, mookequipment, mookcyberwear, mooklocation, will, body, armourmodifier)
    return newmook

def display_mook(mookposition):
    mooks[mookposition].display()

def get_index(*arg):
    # display_mook(mookchoosen.current())
    mookrole_label['text'] = mooks[mookchoosen.current()].getRole()
    mookrep_label['text'] = mooks[mookchoosen.current()].getRep()
    mookseriouslywounded_label['text'] = mooks[mookchoosen.current()].getSeriouslyWounded()
    mookdeathsave_label['text'] = mooks[mookchoosen.current()].getDeathSave()
    mookhp_label['text'] = mooks[mookchoosen.current()].getHP()
    stats = mooks[mookchoosen.current()].getStats()
    mookint_label['text'] = stats.get('Int')
    mookref_label['text'] = stats.get('Ref')
    if len(stats.get('Ref')) > 2:
        mookref_label.place(x=101, y=128)
    else:
        mookref_label.place(x=115, y=128)
    mookdex_label['text'] = stats.get('Dex')
    if len(stats.get('Dex')) > 2:
        mookdex_label.place(x=185, y=128)
    else:
        mookdex_label.place(x=200, y=128)
    mooktech_label['text'] = stats.get('Tech')
    mookcool_label['text'] = stats.get('Cool')
    mookluck_label['text'] = stats.get('Luck')
    mookwill_label['text'] = stats.get('Will')
    mookmove_label['text'] = stats.get('Move')
    if len(stats.get('Move')) > 2:
        mookmove_label.place(x=570, y=128)
    else:
        mookmove_label.place(x=580, y=128)
    mookbody_label['text'] = stats.get('Body')
    mookemp_label['text'] = stats.get('Emp')
    count = 1
    for x,y in mooks[mookchoosen.current()].getWeapons().items():
        if count == 1:
            mookweapon1name_label['text'] = x
            mookweapon1rof_label['text'] = y[1]
            mookweapon1damage_label['text'] = y[0] + "D6"
        if count == 2:
            mookweapon2name_label['text'] = x
            mookweapon2rof_label['text'] = y[1]
            mookweapon2damage_label['text'] = y[0] + "D6"  
        count += 1
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
            
dbt = databaseTools.databaseTools()
mooks = []
mooktable = dbt.find("cpr.mooks", "type", "1")
# mooktable = dbt.findall("cpr.mooks")

for index,entry in enumerate(mooktable):
    mooks.append(loadmooks(index+1))

dbt.close()

win = tk.Tk()
win.geometry("753x508")
win.title("Cyberpunk Red Mook Viewer")

background_image = Image.open("background.jpg")
background = ImageTk.PhotoImage(background_image)
image_label = tk.Label(win , image = background)
image_label.place(x = 0 , y = 0)

mookrole_label = tk.Label(win, text="Mook Role", font=("Arial", 12), bg='#fff', fg='#000')
mookrole_label.place(x=80, y=66)
mookrep_label = tk.Label(win, text="rep", font=("Arial", 12), bg='#fff', fg='#000')
mookrep_label.place(x=435, y=25)
mookseriouslywounded_label = tk.Label(win, text="sw", font=("Arial", 12), bg='#fff', fg='#000')
mookseriouslywounded_label.place(x=580, y=25)
mookdeathsave_label = tk.Label(win, text="ds", font=("Arial", 12), bg='#fff', fg='#000')
mookdeathsave_label.place(x=580, y=66)
mookhp_label = tk.Label(win, text="hp", font=("Arial", 26, "bold"), bg='#fff', fg='#000')
mookhp_label.place(x=687, y=33)
intlabel = tk.Label(win, text="INT ", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
intlabel.place(x=10, y=128)
mookint_label = tk.Label(win, text="int", font=("Arial", 12), bg='#fff', fg='#000')
mookint_label.place(x=46, y=129)
reflabel = tk.Label(win, text="REF ", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
reflabel.place(x=63, y=128)
mookref_label = tk.Label(win, text="ref", font=("Arial", 12), bg='#fff', fg='#000')
mookref_label.place(x=115, y=129)
dexlabel = tk.Label(win, text="DEX ", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
dexlabel.place(x=140, y=128)
mookdex_label = tk.Label(win, text="dex", font=("Arial", 12), bg='#fff', fg='#000')
mookdex_label.place(x=200, y=129)
techlabel = tk.Label(win, text="TECH", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
techlabel.place(x=225, y=128)
mooktech_label = tk.Label(win, text="tech", font=("Arial", 12), bg='#fff', fg='#000')
mooktech_label.place(x=280, y=129)
coollabel = tk.Label(win, text="COOL", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
coollabel.place(x=300, y=128)
mookcool_label = tk.Label(win, text="cool", font=("Arial", 12), bg='#fff', fg='#000')
mookcool_label.place(x=355, y=129)
willlabel = tk.Label(win, text="WILL", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
willlabel.place(x=375, y=128)
mookwill_label = tk.Label(win, text="will", font=("Arial", 12), bg='#fff', fg='#000')
mookwill_label.place(x=424, y=129)
lucklabel = tk.Label(win, text="LUCK", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
lucklabel.place(x=446, y=128)
mookluck_label = tk.Label(win, text="0", font=("Arial", 12), bg='#fff', fg='#000')
mookluck_label.place(x=500, y=129)
movelabel = tk.Label(win, text="MOVE", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
movelabel.place(x=515, y=128)
mookmove_label = tk.Label(win, text="move", font=("Arial", 12), bg='#fff', fg='#000')
mookmove_label.place(x=580, y=129)
bodylabel = tk.Label(win, text="BODY", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
bodylabel.place(x=610, y=128)
mookbody_label = tk.Label(win, text="body", font=("Arial", 12), bg='#fff', fg='#000')
mookbody_label.place(x=663, y=129)
emplabel = tk.Label(win, text="EMP", font=("Arial", 12, "bold"), bg='#bbb', fg='#000')
emplabel.place(x=680, y=128)
mookemp_label = tk.Label(win, text="emp", font=("Arial", 12), bg='#fff', fg='#000')
mookemp_label.place(x=725, y=129)
mookweapon1name_label = tk.Label(win, text="w1", font=("Arial", 12), bg='#fff', fg='#000')
mookweapon1name_label.place(x=20, y=186)
mookweapon1rof_label = tk.Label(win, text="rof", font=("Arial", 12), bg='#fff', fg='#000')
mookweapon1rof_label.place(x=361, y=186)
mookweapon1damage_label = tk.Label(win, text="dmg", font=("Arial", 12), bg='#fff', fg='#000')
mookweapon1damage_label.place(x=441, y=186)
mookweapon2name_label = tk.Label(win, text="w2", font=("Arial", 12), bg='#fff', fg='#000')
mookweapon2name_label.place(x=20, y=219)
mookweapon2rof_label = tk.Label(win, text="rof", font=("Arial", 12), bg='#fff', fg='#000')
mookweapon2rof_label.place(x=361, y=219)
mookweapon2damage_label = tk.Label(win, text="dmg", font=("Arial", 12), bg='#fff', fg='#000')
mookweapon2damage_label.place(x=441, y=219)
mookarmourhead_label = tk.Label(win, text="head", font=("Arial", 12), bg='#fff', fg='#000')
mookarmourhead_label.place(x=522, y=186)
mookarmourheadsp_label = tk.Label(win, text="spec", font=("Arial", 12), bg='#fff', fg='#000')
mookarmourheadsp_label.place(x=698, y=186)
mookarmourbody_label = tk.Label(win, text="body", font=("Arial", 12), bg='#fff', fg='#000')
mookarmourbody_label.place(x=522, y=219)
mookarmourbodysp_label = tk.Label(win, text="spec", font=("Arial", 12), bg='#fff', fg='#000')
mookarmourbodysp_label.place(x=698, y=219)
mookskills_label = tk.Label(win, text="skills", font=("Arial", 9), wraplength=733, justify="left", bg='#fff', fg='#000')
mookskills_label.place(x=10, y=270)
mookequipment_label = tk.Label(win, text="equipment", font=("Arial", 9), wraplength=733, justify="left", bg='#fff', fg='#000')
mookequipment_label.place(x=10, y=368)
mookcyberwear_label = tk.Label(win, text="cyberwear", font=("Arial", 9), wraplength=733, justify="left", bg='#fff', fg='#000')
mookcyberwear_label.place(x=10, y=450)

n = tk.StringVar() 
mookchoosen = ttk.Combobox(win, width = 27, textvariable = n) 
n.trace_add('write', get_index) 

mooklist = []
for mook in mooks:
    mooklist.append(mook.getName())

mookchoosen['values'] = tuple(mooklist) 
mookchoosen['state'] = 'readonly'

mookchoosen.pack()

mookchoosen.current(0)
mookchoosen.place(x=80, y=25)

win.mainloop()
            