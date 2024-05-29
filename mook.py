import math

class mook(object):
    name = ''
    type = ""
    generic = ""
    rep = ""
    headarmour = []
    bodyarmour = []
    stats = {}
    weapons = {}
    role = ''
    skills = {}
    equipment = []
    cyberwear = []
    location = ""
    hp = 0
    seriouslywounded = 0
    deathsave = 0
    armourmodifier = 0


    def __init__(self, name, type, rep, generic, headarmour, bodyarmour, stats, weapons, role, skills, equipment, cyberwear, location, will, body, armourmodifier):
        self.name = name
        self.type = type
        self.generic = generic
        self.headarmour = headarmour
        self.bodyarmour = bodyarmour
        self.stats = stats
        self.weapons = weapons
        self.equipment = equipment
        self.cyberwear = cyberwear
        self.rep = rep
        self.location = location
        self.role = role
        self.skills = skills
        self.hp = 10 + (5 *(math.ceil((int(body) + int(will))/2)))
        self.seriouslywounded = math.ceil(self.hp/2)
        self.deathsave = body
        self.armourmodifier = armourmodifier

    def display(self):
        print("Name : " + self.name)
        print("Type: " +self.type)
        print("Reputation: " + self.rep)
        print("Role: " + self.role)
        print("Hit Points: " + str(self.hp))
        print("Seriously Wounded: " + str(self.seriouslywounded))
        print("Death Save: " + str(self.deathsave))
        print("Head Armour: " + self.headarmour[0] + " SP: " + self.headarmour[1])
        print("Body Armour: " + self.bodyarmour[0] + " SP: " + self.bodyarmour[1])
        print("Stats:")
        for x,y in self.stats.items():
            print(x,y)
        print("Weapons:")
        for x,y in self.weapons.items():
            print(x," Damage: ",y[0], "D6 ROF: ", y[1])
        print("Skills:")
        for x,y in self.skills.items():
            print(x,y)
        print("Equipment:")
        for x in self.equipment:
            print(x)
        print("Cyberwear:")
        for x in self.cyberwear:
            print(x)
        print("Location : " + self.location)

    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getRep(self):
        return self.rep
    
    def getHeadArmour(self):
        return self.headarmour
    
    def getBodyArmour(self):
        return self.bodyarmour
    
    def getStats(self):
        return self.stats
    
    def getWeapons(self):
        return self.weapons
    
    def getRole(self):
        return self.role
    
    def getSkills(self):
        return self.skills
    
    def getEquipment(self):
        return self.equipment
    
    def getCyberwear(self):
        return self.cyberwear
    
    def getLocation(self):
        return self.location
    
    def getHP(self):
        return self.hp
    
    def getSeriouslyWounded(self):
        return self.seriouslywounded
    
    def getDeathSave(self):
        return self.deathsave
    
    def getArmourModifier(self):
        return self.armourmodifier
    
    def getGeneric(self):
        return self.generic
    
    def getskills(self):
        return self.skills
    
    def getEquipment(self):
        return self.equipment
    
    def getCyberwear(self):
        return self.cyberwear
    
    def getLocation(self):
        return self.location
    
    def getWeapons(self):
        return self.weapons
    
    def getRole(self):
        return self.role    
