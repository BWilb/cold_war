class DRG:
    def __init__(self):
        #arbitrary characteristics of East Germany
        self.socialist_leader = "Walter Ulbricht"
        self.leader = ""
        #bigger picture characteristics
        '''politics'''
        self.political_party = "Socialist Unity Party of Germany"
        self.party_popularity = 100
        self.stability = 1.00
        self.other_parties = ["CDU", "LDPD", "DBD", "NDPD"]
        '''regarding population'''
        self.cities_list = []
        self.population = 0
        '''regarding military'''
        self.troop_list = []
        self.tank_list = []

class T80:
    def __init__(self):
        self.health = 450
        self.firepower = 50


class EastGermanCities:
    def __init__(self, north, ne, e, se, s, sw, w, nw, population, population_growth):
        self.north = north
        self.north_east = ne
        self.east = e
        self.south_east = se
        self.south = s
        self.south_west = sw
        self.west = w
        self.north_west = nw
        self.description = None
        self.population = population
        self.growth = population_growth

def egerman_cities():
    commie_cities = []

    east_berlin = EastGermanCities(None, None, None, None, None, None, None, None, 3000000, 0.034)
    east_berlin.description = f"Welcome to East Berlin, Population: {east_berlin.population}. You better enjoy the stay."

    commie_cities.append(east_berlin)


    return commie_cities