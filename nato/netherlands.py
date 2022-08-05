class Netherlands:
    def __init__(self):
        #individual characteristics of netherlands
        self.leader = "Juliana"
        self.troop_list = []
        self.cities_list = []
        self.current_city = 0
        #bigger picture characteristics
        self.population = 0
        self.stability = 1.00
        self.senate_members = 150
        self.year = 1960
        self.monarchs = ["Beatrix", "William-Alexander"]

class DutchSoldier:
    def __init__(self):
        self.health = 100

class DutchCities:
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

def dutch_cities():
    cities = []
    amsterdam = DutchCities(None, None, None, 2, None, 1, None, None, 895000, 0.0123)
    amsterdam.description = "Welkom in Amsterdam. Go SE to Utrecht or SW to The Hague."
    cities.append(amsterdam)
    the_hague = DutchCities(None, 0, 2, None, None, None, None, None, 740000, 0.0014)
    the_hague.description = "Welcome to The Hague, Netherlands. Go NE to Amsterdam or E to Utrecht."
    cities.append(the_hague)
    utrecht = DutchCities(None, None, None, None, None, None, 1, 0, 274000, 0.0148)
    utrecht.description = "Welcome to the famous city of Utrecht. Go W to The Hague or NW to Amsterdam."
    cities.append(utrecht)
    return cities