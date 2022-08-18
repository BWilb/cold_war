class France:
    def __init__(self):
        #arbitrary characteristics
        self.leader = "Phillip Petain"
        self.troop_list = []
        self.tank_list = []
        self.nuclear_weapons = 300
        #bigger picture characteristics
        self.cities_list = []
        self.population = 0
        self.current_city = 0
        '''Political situation of France'''
        self.stability = 100
        self.democratic_support = 93
        self.facist_support = 3
        self.communist_support = 4
        self.year = 1960

class FrenchSoldier:
    def __init__(self):
        self.health = 150

class AMX:
    #MBT of France around 1960
    def __init__(self):
        self.health = 250
        self.firepower = 25

class FrenchCities:
    def __init__(self, north, north_east, east, south_east, south, south_west, west, north_west, population, population_growth):
        self.north = north
        self.north_east = north_east
        self.east = east
        self.south_east = south_east
        self.south = south
        self.south_west = south_west
        self.west = west
        self.north_west = north_west
        self.population = population
        self.growth = population_growth
        self.description = None

def french_cities():
    cities = []
    paris = FrenchCities(None, None, None, 1, None, 2, None, None, 7411000, 0.0176)
    paris.description = "Welcome to the beautiful city of Paris. Go SE to Lyon or SW to Bordeaux."
    cities.append(paris)
    lyon = FrenchCities(None, 4, None, 5, None, None, None, None, 904000, 0.0331)
    lyon.description = "Welcome to Lyon, the birthplace of Phillipe Petain. Go NE to Strasbourg or NW to Paris."
    cities.append(lyon)
    bordeaux = FrenchCities(None, 0, 5, 3, None, None, None, None, 495000, 0.0206)
    bordeaux.description = f"Welcome to Bordeaux. Population: {bordeaux.population}. Go SE to Toulouse, N to Paris, or NE to Lyon."
    cities.append(bordeaux)
    toulouse = FrenchCities(None, 1, 5, None, None, None, None, 2, 347000, 0.0420)
    toulouse.description = f"Welcome to Toulouse. Population: {toulouse.population}. Go NW to Bordeaux, W to Nice, or NE to Lyon."
    cities.append(toulouse)
    strasbourg = FrenchCities(None, None, None, None, None, 1, None, 0, 298000, 0.0205)
    strasbourg.description = f"Welcome to a franco-german city. Population: {strasbourg.population}. Go NW to Paris or SW to Lyon."
    cities.append(strasbourg)
    nice = FrenchCities(None, None, None, None, None, None, 3, 1, 495000, 0.0313)
    nice.description = f"Welcome to Nice. Poulation: {nice.population}. Go NW to Lyon or W to Toulouse."
    cities.append(nice)
    return cities