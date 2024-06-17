from dataclasses import dataclass

@dataclass
class weapon:
    name : str
    quality : str
    qualityvalue : int
    damage : int
    rof : int
    dbposition : int