class UnitedStates:
    def __init__(self):
        #individual characteristics of united states
        self.leader = "John F. Kennedy"
        self.troops = []
        self.tanks = []
        self.nuclear_bombs = 4000
        self.cities_list = []
        #bigger picture characteristics
        self.democratic_support = 100
        self.facist_support = 0
        self.communist_support = 0
        self.population = 0
        self.stablility = 1.00
        #election variables
        self.elections = [["Lyndon B. Johnson", "Barry M. Goldwater"], ["Richard Nixon", "Hubert Humphrey"],
                          ["Richard Nixon", "George McGovern"], ["Jimmy Carter", "Gerald Ford"], ["Ronald Reagan", "Jimmy Carter"],
                          ["Ronald Reagan", "Walter F. Mondale"], ["George Bush", "Michael S. Dukakis"], ["William Clinton", "George Bush"],
                          ["William Clinton", "Robert Dole"], ["George W. Bush", "Albert Gore"], ["George W. Bush", "John F. Kerry"],
                          ["Barack H. Obama", "John McCain"], ["Barack Obama", "Mitt Romney"], ["Donald Trump", "Hillary Clinton"],
                          ["Joe Biden", "Donald Trump"]]
        self.year = 1960
        self.election = 0

    def change_leader(self):
        self.leader = input("Who was elected president?: ")

class AmericanSoldier:
    #American soldier
    def __init__(self):
        self.health = 500

class M60:
    #M60 tanks
    def __init__(self):
        self.health = 205
        self.firepower = 45

class Magach:
    #Magach tanks
    def __init__(self):
        self.health = 200
        self.firepower = 40

class M1Abrams:
    #M1 Abrams tanks
    def __init__(self):
        self.health = 300
        self.firepower = 50

class AmericanCities:
    def __init__(self, north, north_east, east, south_east, south, south_west, west, north_west, population, population_growth):
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
        self.population_growth = population_growth

def us_locations():
    cities = []
    #main capital of United States
    #0
    washington_dc = AmericanCities(None, 7, None, None, 10, None, 26, None, None, 0.0318)
    washington_dc.population = 1823000
    washington_dc.population_growth = 0.0318
    washington_dc.description = f"You are in the political heart of the United States. Population: {washington_dc.population}. " \
                                " Move NE to Philly, S to Richmond, or W to Columbus."
    cities.append(washington_dc)
    #New England capitals
    #1
    augusta = AmericanCities(None, None, None, None, 5, 2, 3, None, 124000, 0.024)
    augusta.description = f"Welcome to Augusta Maine. You should try some lobsta. Population: {augusta.population}. " \
                          f"Go S for Boston, SW to Concord, or W to Montpeiler. Or you can defect to Canada.\n" \
                          f"you could go east to cross the Atlantic(defection). "
    cities.append(augusta)
    #2
    concord = AmericanCities(None, 1, None, 5, 6, None, None, 3, 240000, 0.033)
    concord.description = f"Welcome to Concord, New Hampshire. Population: {concord.population}. " \
                          f"Go NE to Augusta, SE to Boston, S to Hartford, or NW to Montpeiler."
    cities.append(concord)
    #3
    montpeiler = AmericanCities(None, 1, None, 2, 4, None, None, None, 24000, 0.032)
    montpeiler.description = f"Welcome to Montpeiler, Vermont. Population: {montpeiler.population}. " \
                             f"Go NE to Augusta, SE to Concord, S to New York. Go N to defect to Canada"
    cities.append(montpeiler)
    #4
    nyc = AmericanCities(3, 6, None, None, None, 7, None, None, 14164000, 0.02)
    nyc.description = f"Welcome to NYC, the financial hub of the US. Population: {nyc.population}. " \
                      f"Go N to Montpeiler, NE to Hartford, SW to Philly, or E to cross Atlantic(Defection)."
    cities.append(nyc)
    #5
    boston = AmericanCities(1, None, None, None, None, 6, None, 2, 2818000, 0.015)
    boston.description = f"Welcome to Boston, Massachusetts. Population: {boston.population}. " \
                         f"Go N to Augusta, SW to Hartford, NW to Concord, or E to cross Atlantic(defection)."
    cities.append(boston)
    #6
    hartford = AmericanCities(None, 2, None, None, None, 4, None, 3, 485000, 0.03)
    hartford.description = f"Welcome to Hartford Connecticut. Population: {hartford.population}. " \
                           f"Go NE to Boston, SW to New York, NW to Montpeiler."
    cities.append(hartford)
    #east coast
    #7
    philadelphia = AmericanCities(None, 4, None, None, 9, 0, None, None, 3930000, 0.025)
    philadelphia.description = f"Welcome to Philly. Population: {philadelphia.population}. " \
                               f"Go NE to New York, S to Dover, SW to DC."
    cities.append(philadelphia)
    #8
    newark = AmericanCities(4, None, None, None, None, 9, 7, None, 405220, 0.011)
    newark.description = f"Welcome to Newark, New Jersey. Population: {newark.population}. " \
                         f"Go N to New York, W to Philly, or SW to Dover or E to cross the Atlantic."
    cities.append(newark)
    #9
    dover = AmericanCities(7, None, None, None, None, 0, None, None, 80045, 0.02)
    dover.description = f"Welcome to Dover, Delaware. Population: {dover.population}. " \
                        f"Go N to Philly or SW to DC, or E to cross the Atlantic(Defection)."
    cities.append(dover)
    #10
    richmond = AmericanCities(0, None, None, None, None, 11, 12, None, 337000, 0.045)
    richmond.description = f"Welcome to Richmond, Virginia. Population: {richmond.population}. " \
                           f"Go N to DC, SW to Raleigh, or W to Charleston."
    cities.append(richmond)
    #11
    raleigh = AmericanCities(None, 10, None, None, None, None, None, 12, 95000, 0.0526)
    raleigh.description = f"Welcome to Raleigh, N.C. Population {raleigh.population}. " \
                          f"Go NE to Richmond or NW to Charleston, or E to cross the Atlantic(defection)."
    cities.append(raleigh)
    #12
    charleston = AmericanCities(None, 0, 10, 11, None, 16, None, 26, 162000, 0.0318)
    charleston.description = f"Welcome to Charleston, WEST VIRGINA!!!! Population {charleston.population}. \n" \
                             f"Go NE to DC, E to Richmond, SE to Raleigh, SW to Louisville, or NW to Columbus."
    cities.append(charleston)
    #13
    atlanta = AmericanCities(26, 11, None, 14, None, 18, 21, 17, 776000, 0.0438)
    atlanta.description = f"Welcome to Atlanta, Georgia. Population: {atlanta.population}.\n" \
                          f"Go N to Columbus, NE to Raleigh, SE to Jacksonville"
    cities.append(atlanta)
    #14
    jacksonville = AmericanCities(None, None, None, None, None, None, 20, 18, 201300, 0.043)
    jacksonville.description = f"Welcome to Jacksonville, Florida. Population: {jacksonville.population}.\n" \
                               f"Go NW to Montgomery, W to Baton Rouge, or E to cross the Atlantic(defection)"
    cities.append(jacksonville)
    #southern states
    #15
    charleston = AmericanCities(None, 0, 10, 11, None, 16, None, 26, 162000, 0.0318)
    charleston.description = f"Welcome to Charleston, West Virginia. Population: {charleston.population}.\n" \
                             f"Go NE to DC, E to Richmond, SE to Raleigh, or NW to Columbus."
    cities.append(charleston)
    #16
    louisville = AmericanCities(None, 26, None, None, None, 17, None, 28, 610000, 0.0252)
    louisville.description = f"Welcome to Louisville, Kentucky. We're one of the dumb fuck states...YEE YEE.\n" \
                             f"Go NE to Columbus, SW to Nashville, Chicago."
    cities.append(louisville)
    #17
    nashville = AmericanCities(27, 16, None, 13, None, 19, None, 28, 349000, 0.0258)
    nashville.description = f"YEE YEE welcome to Tennessee. Population: {nashville.population}.\n" \
                            f"Go N to Indianapolis, NE to Louisville, SE to Atalnta, SW to Montgomery, or NW to Chicago."
    cities.append(nashville)
    #18
    montgomery = AmericanCities(None, 13, None, None, None, 20, 19, 21, 142000, 0.0143)
    montgomery.description = f"Welcome to Montgomery, Alabama...Wanna go shoot a civil rights leader?\n" \
                             f"Go NE to Atlanta, NW to Little Rock, W to Jackson, or SW to Baton Rouge."
    cities.append(montgomery)
    #19
    jackson = AmericanCities(None, 17, 18, 14, None, 20, None, 21, 148000, 0.027)
    jackson.description = f"Welcome to Jackson Mississippi. Population: {jackson.population}.\n" \
                          f"Go NE to Nashville, E to Montgomery, SE to Jacksonville, SW to Baton Rouge, or NW to Little Rock."
    cities.append(jackson)
    #20
    baton_rouge = AmericanCities(None, 19, 14, None, None, 23, None, 21, 152419, 0.023)
    baton_rouge.description = f"Welcome to the Baton Rouge. Population: {baton_rouge.population}.\n" \
                              f"Go NE to Jackson, E to Jacksonville, SW to Houston, or NW to Little Rick"
    cities.append(baton_rouge)
    #21
    little_rock = AmericanCities(None, 17, 13, 19, None, 23, 22, 35, 186000, 0.0161)
    little_rock.description = f"Welcome to Little Rock. Population: {little_rock.population}.\n" \
                              f"Go NE to Nashville, E to Atlanta, SE to Jackson, SW to Houston, W to Okie city, or NW to Topeka."
    cities.append(little_rock)
    #22
    oklahoma_city = AmericanCities(None, 35, 21, 23, None, None, 24, 36, 431000, 0.0232)
    oklahoma_city.description = f"Welcome to Oklahoma city. Population: {oklahoma_city.population}.\n" \
                                f"Go NE to Topeak, E to L.R., SE to Houston, W to Alberquerque, or NW to Denver."
    cities.append(oklahoma_city)
    #23
    houston = AmericanCities(None, 20, None, None, None, None, None, 36, 1151000, 0.039)
    houston.description = f"Welcome to Houston, Texas...YEE YEE YEE. Population {houston.population}.\n" \
                          f"Go NE to Baton Rouge or NW to Alberquerque."
    cities.append(houston)
    #24
    alberquerque = AmericanCities(36, None, 22, 23, None, 25, None, None, 242000, 0.0211)
    alberquerque.description = f"Welcome to Alberquerque, New Mexico. We're the dumbest state. Population: {alberquerque.population}.\n" \
                               f"Go N to Denver, E to Okie city, SE to Houston, SW to Phoenix."
    cities.append(alberquerque)
    #25
    phoenix = AmericanCities(39, 36, None, None, None, None, 41, None, 558000, 0.0466)
    phoenix.description = f"Welcome to Phoenix. Population: {phoenix.population}.\n" \
                          f"Go N to Salt lake city, NE to Denver, or NW to Las Vegas."
    cities.append(phoenix)
    #Central United States
    #26
    columbus = AmericanCities(None, None, 7, 15, None, 16, 27, 28, 621000, 0.0242)
    columbus.description = f"Welcome to Columbus Ohio. Population: {columbus.population}.n" \
                           f"Go E to Philly, SE to Charleston, SW to Louisville, W to Indy, or NW to Chicago."
    cities.append(columbus)
    #27
    indianapolis = AmericanCities(None, None, 26, None, 16, 29, None, 28, 643000, 0.0239)
    indianapolis.description = f"Welcome to Indianapolis. Population: {indianapolis.population}.\n" \
                               f"Go NW to Chicago, SW to Kansas City, S to Louisville, or E to Columbus."
    cities.append(indianapolis)
    #28
    chicago = AmericanCities(None, None, None, 27, None, None, 30, None, 6183000, 0.0144)
    chicago.description = f"Welcome to the windy city. Population: {chicago.population}.\n" \
                          f"Go SE to Indianapolis or W to Des Moines."
    cities.append(chicago)
    #29
    kansas_city = AmericanCities(None, 30, 27, None, 21, 35, None, None, 925000, 0.0255)
    kansas_city.description = f"Welcome to Kansas City. Population: {kansas_city.population}.\n" \
                              f"Go NE to Des Moines, E to Indianapolis, S to L.R., or SW to Topeka."
    cities.append(kansas_city)
    #30
    des_moines = AmericanCities(31, 28, None, None, None, 29, None, 33, 241000, 0.0126)
    des_moines.description = f"Welcome to Des Moines. Population: {des_moines.population}.\n" \
                             f"Go N to Minneapolis, NE to Chicago, SW to KC, or NW to Pierre."
    cities.append(des_moines)
    #31
    minneapolis = AmericanCities(None, None, None, None, 30, None, 33, None, 1384000, 0.0305)
    minneapolis.description = f"Welcome to Minneapolis. Population: {minneapolis.population}.\n" \
                              f"Go S to Des Moines or W to Pierre."
    cities.append(minneapolis)
    #32
    bismarck = AmericanCities(None, None, None, 31, 33, None, None, None, 32456, 0.025)
    bismarck.description = f"Welcome to Bismarck. Population: {bismarck.population}.\n" \
                           f"Go SE to Minneapolis or S to Pierre."
    cities.append(bismarck)
    #33
    pierre = AmericanCities(32, None, 31, 30, None, 37, None, None, 26539, 0.0124)
    pierre.description = f"Welcome to Pierre. Population: {pierre.population}.\n" \
                         f"Go N to Bismarck, E to Minneapolis, SE to Des Moines, SW to Cheyenne."
    cities.append(pierre)
    #34
    lincoln = AmericanCities(None, 30, None, 35, None, 36, 37, None, 128521, 0.0163)
    lincoln.description = f"Welcome to Lincoln. Population: {lincoln.population}.\n" \
                          f"Go NE to Des Moines, SE to Topeka, SW to Denver, or W to Cheyenne."
    cities.append(lincoln)
    #35
    topeka = AmericanCities(None, 29, None, 21, None, 22, 36, 34, 34565, 0.012)
    topeka.description = f"Welcome to Topeka. Population: {topeka.population}.\n" \
                         f"Go NE to KC, SE to Little Rock, SW to Okie City, W to Denver, or NW to Lincoln."
    cities.append(topeka)
    #Rocky cities
    #36
    denver = AmericanCities(None, None, None, None, None, None, None, None, 809000, 0.0272)
    cities.append(denver)
    #37
    cheyenne = AmericanCities(None, None, None, None, None, None, None, None, 23245, 0.034)
    cities.append(cheyenne)
    #38
    helena = AmericanCities(None, None, None, None, None, None, None, None, 12434, 0.056)
    cities.append(helena)
    #39
    salt_lake_city = AmericanCities(None, None, None, None, None, None, None, None, 45643, 0.032)
    cities.append(salt_lake_city)
    #40
    boise = AmericanCities(None, None, None, None, None, None, None, None, 23453, 0.031)
    cities.append(boise)
    #41
    las_vegas = AmericanCities(None, None, None, None, None, None, None, None, 92000, 0.11)
    cities.append(las_vegas)
    #Western cities
    #42
    seattle = AmericanCities(None, None, None, None, None, None, None, None, 1089000, 0.0332)
    cities.append(seattle)
    #43
    portland = AmericanCities(None, None, None, None, None, None, None, None, 656000, 0.0250)
    cities.append(portland)
    #44
    los_angelos = AmericanCities(None, None, None, None, None, None, None, None, 6530000, 0.0438)
    cities.append(los_angelos)
    #45
    anchorage = AmericanCities(None, None, None, None, None, None, None, None, 169795, 0.011)
    cities.append(anchorage)
    #46
    honolulu = AmericanCities(None, None, None, None, None, None, None, None, 353000, 0.0255)
    cities.append(honolulu)
    return cities