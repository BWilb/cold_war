import random
class Avatar:
    def __init__(self):
        #arbitrary characteristics of avatar(changeable characteristics)
        self.name = "Adolf Hitler"
        self.hunger = 0
        self.thirst = 0
        self.health = 500
        self.alive = False
        #mental characteristics
        self.paranoia = 0
        self.intelligence = 0
        self.awareness = 100
        #power building characteristics
        self.partisan_list = []
        self.weapons_list = []
        #stats
        self.kills = 0
        self.partisans_killed = 0
        #for election purposes
        self.year = 1960
        #random events
        self.randomness = 0

class Partisan:
    def __init__(self):
        #health of partisan
        self.health = 300
        #how indoctrinated they are. This can fluctuate
        self.indoctrinated = 0
        #How powerful this individual is
        self.attack = random.randrange(0, 100)
