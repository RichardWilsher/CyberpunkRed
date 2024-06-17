from dataclasses import dataclass
import math

@dataclass
class mook:
    name: str
    mooktype: str
    rep: int
    headarmour: dict
    bodyarmour: dict
    stats: dict
    weapons: dict
    role: str
    skills: dict
    equipment: list
    cyberwear: list
    location: str
    armourmodifier: int
    id : int
    def gethp(self):
        return 10 + (5 *(math.ceil((int(self.stats.get('Body')) + int(self.stats.get('Will')))/2))) 