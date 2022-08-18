import random
from nato import france

def dutch_front(avar, french):
    current_city = 0
    choices = ["\n1. Move",
               "2. Defect to a different nation",
               "3. Overthrow the current administration",
               "4. Commit an act of terrorism",
               "5. Eat",
               "6. Drink",
               "7. Change your name",
               "8. View Stats\n"]

    directions = ["\n1. north",
                  "2. north east",
                  "3. east",
                  "4. south east",
                  "5. south",
                  "6. south_west",
                  "7. west",
                  "8. north west\n"]

    while not avar.alive:
        print(f"It is {french.year}.")
        print("\n" + french.cities_list[current_city].description)

        for i in range(len(choices)):
            print(choices[i])
        first_choice = int(input("what is your choice 1-8?: "))
        if first_choice == 1:

            for i in range(len(directions)):
                print(directions[i])
            second_choice = int(input("what direction do you choose? 1 - 8: "))

            if second_choice == 1:
                next_city = french.cities_list[current_city].north
                if french.cities_list[current_city].north is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 2:
                next_city = french.cities_list[current_city].north_east
                if french.cities_list[current_city].north_east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 3:
                next_city = french.cities_list[current_city].east
                if french.cities_list[current_city].east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")

                else:
                    current_city = next_city

            elif second_choice == 4:
                next_city = french.cities_list[current_city].south_east
                if french.cities_list[current_city].south_east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 5:
                next_city = french.cities_list[current_city].south
                if french.cities_list[current_city].south is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 6:
                next_city = french.cities_list[current_city].south_west
                if french.cities_list[current_city].south_west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 7:
                next_city = french.cities_list[current_city].west
                if french.cities_list[current_city].west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 8:
                next_city = french.cities_list[current_city].north_west
                if french.cities_list[current_city].north_west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city
            avar.thirst += random.randrange(0, 10)
            avar.hunger += random.randrange(0, 5)

def initial_stats(french):
    #establishes the infantry of france
    for i in range(0, random.randrange(150000, 250000)):
        soldier = france.FrenchSoldier()
    #creates tank brigades for france
    for i in range(0, random.randrange(100, 700)):
        mbt = france.AMX()
        french.tank_list.append(mbt)
    #establishes the national population of france
    for i in range(len(france.french_cities())):
        french.population += french.cities_list[i].population

def main():
    french = france.France()
    french.cities_list = france.french_cities()
    initial_stats(french)

if __name__ == '__main__':
    main()