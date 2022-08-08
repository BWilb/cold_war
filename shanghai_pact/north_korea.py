class NorthKorea:
    def __init__(self):
        #individual characteristics of north_korea
        self.leader = "Kim il Sung"
        self.troops = []
        self.tanks = []
        self.nuclear_bombs = 20
        self.cities_list = []
        #bigger picture characteristics
        self.army_loyalty = 100
        self.stability = 0.75
        self.population = 0
        self.year = 1960
        #inheritance of the country
        self.inheritors = ["kim jong-il", "kim jong-un"]

class NorthKoreanCities:
    def __init__(self, north, north_east, east, south_east, south, south_west, west, north_west, population, growth):
        self.north = north
        self.north_east = north_east
        self.east = east
        self.south_east = south_east
        self.south = south
        self.south_west = south_west
        self.west = west
        self.north_west = north_west
        self.description = None
        self.population = population
        self.growth = growth

def dprk_locations():
    # only city you're allowed to visit.
    cities = []
    pyongyang = NorthKoreanCities(3, None, None, None, 1, None, None, None, 650000, 0.0564)
    pyongyang.description = f"Welcome to Pyongyang. You are never going to visit any other city if you misbehave, else" \
                            f"you will be shot.\nCurrent population: {pyongyang.population}."
    cities.append(pyongyang)
    #south of Pyongyang
    haeju = NorthKoreanCities(0, None, None, None, None, None, None, None, 325000, 0.0453)
    haeju.description = f"Welcome to Haeju. You have successfully earned the trust of the kim regime.\n" \
                        f"Go N to Pyongyang or SE to Kaesong."
    cities.append(haeju)
    kaesong = NorthKoreanCities(None, None, None, None, None, None, None, 1, 550000, 0.0654)
    kaesong.description = "Welcome to Kaesong, where you will hear the dastardly capitalist south blaring its music.\n" \
                          "Go NW to Haeju."
    cities.append(kaesong)
    #north of pyongyang

    kusong = NorthKoreanCities(None, None, None, None, 0, None, None, None, 245000, 0.0256)
    kusong.description = "Welcome to kusong. Go S to Pyongyang"
    cities.append(kusong)

    chongjin = NorthKoreanCities(None, None, None, None, None, 3, None, None, 670000, 0.067)
    chongjin.description = "Welcome to Chongjin. Go SW to Kusong."
    cities.append(chongjin)

    return cities