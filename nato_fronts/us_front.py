import random
from avatar import avatar_file
from nato import united_states
from nato_fronts import dutch_front

#===============================================================================
#main piece of game
def defection(avar):
    print("You chose to defect")
    nations = ["1. Britain(in progress)", "2. France(in progress)", "3. West Germany(in progress)", "4. Belgium(in progress)",
               "5. Netherlands",
               "6. Italy(in progress)", "7. Turkey(in progress)", "8. United States", "9. Soviet Union(in progress)",
               "10. DRG(in progress)",
               "11. Romania(in progress)", "12. Hungary(in progress)", "13. Poland(in progress)",
               "14. Czechoslovakia(in porgess)",
               "15. China(in progress)", "16. North Korea(in progress)", "17. Mongolia(in porgess)", "18. Vietnam(in por)",
               "19. Cambodia(in por)"]

    for i in range(0, len(nations)):
        print(nations[i])

    new_nation = input("Which nation do you choose? 1-19: ")
    if new_nation == 5:
        dutch_front.main(avar)


def begin_rebellion(avar):
    if len(avar.partisan_list) <= 50:
        print("You are not capable of beginning a rebellion")
    else:
        print("The rebellion has begun")

def commit_terror(avar):
    print("still a work in terror")

def eat(avar):
    print("still a work in progress")

def drink(avar):
    print("still a work in progress")

def change_name(avar):
    print("still a work in progress")

def view_stats(avar, us):
    print(f"You have killed {avar.kills} people")
    print(f"Your current name is " + avar.name)
    print(f"Your health level is {avar.health}")
    print(f"You have {avar.hunger} in hunger")
    print(f"You have {avar.thirst} in thirst")
    print(f"The nation you currently reside in has a population of {us.population}")

def us_elections(us):
    candidates = [["Lyndon B. Johnson", "Barry M. Goldwater"], ["Richard Nixon", "Hubert Humphrey"],
                          ["Richard Nixon", "George McGovern"], ["Jimmy Carter", "Gerald Ford"], ["Ronald Reagan", "Jimmy Carter"],
                          ["Ronald Reagan", "Walter F. Mondale"], ["George Bush", "Michael S. Dukakis"], ["William Clinton", "George Bush"],
                          ["William Clinton", "Robert Dole"], ["George W. Bush", "Albert Gore"], ["George W. Bush", "John F. Kerry"],
                          ["Barack H. Obama", "John McCain"], ["Barack Obama", "Mitt Romney"], ["Donald Trump", "Hillary Clinton"],
                          ["Joe Biden", "Donald Trump"]]
    #method designed to elect a new president automatically after years
    vote_total = 0

    #variables based on choices
    choice_one = 0
    choice_two = 0

    #year increased by half every go around
    if us.year % 4 == 0:
        print(f"It is election time in the united states. The year is {us.year}.")

        for i in range(0, int(us.population / 25)):
            chance = random.randrange(0, 2)
            if chance == 0:
                choice_one += 1
            elif chance == 1:
                choice_two += 1
            vote_total += 1
            print(f"votes cast: {vote_total}")

        if choice_one > choice_two:
            us.leader = candidates[us.election][0]
            print(f"The winner of the {us.year} presidential election is " + us.leader)

        elif choice_one < choice_two:
            us.leader = candidates[us.election][1]
            print(f"The winner of the {us.year} presidential election is " + us.leader)

        else:
            us.stablility -= 0.1
            us.leader = candidates[us.election][0]
            print(f"There was no clear winner to the {us.year} Presidential election.")
            print("Congress elected " + us.leader + " to the presidency.")

        us.election += 1
        us.year += 1


def us_front(avar, us):
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
        print(f"\nIt is {us.year}.")
        us.year += 1
        print(us.cities_list[current_city].description)

        for i in range(len(choices)):
            print(choices[i])
        first_choice = int(input("what is your choice 1-8?: "))
        if first_choice == 1:

            for i in range(len(directions)):
                print(directions[i])
            second_choice = int(input("what direction do you choose? 1 - 8: "))

            if second_choice == 1:
                next_city = us.cities_list[current_city].north
                if us.cities_list[current_city].north is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 2:
                next_city = us.cities_list[current_city].north_east
                if us.cities_list[current_city].north_east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 3:
                next_city = us.cities_list[current_city].east
                if us.cities_list[current_city].east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")

                else:
                    current_city = next_city

            elif second_choice == 4:
                next_city = us.cities_list[current_city].south_east
                if us.cities_list[current_city].south_east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 5:
                next_city = us.cities_list[current_city].south
                if us.cities_list[current_city].south is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 6:
                next_city = us.cities_list[current_city].south_west
                if us.cities_list[current_city].south_west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 7:
                next_city = us.cities_list[current_city].west
                if us.cities_list[current_city].west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 8:
                next_city = us.cities_list[current_city].north_west
                if us.cities_list[current_city].north_west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city
            avar.thirst += random.randrange(0, 10)
            avar.hunger += random.randrange(0, 5)

        elif first_choice == 2:
            defection(avar)
        elif first_choice == 3:
            begin_rebellion(avar)
        elif first_choice == 4:
            commit_terror(avar)
        elif first_choice == 5:
            eat(avar)
        elif first_choice == 6:
            drink(avar)
        elif first_choice == 7:
            change_name(avar)
        elif first_choice == 8:
            view_stats(avar, us)

        for i in range(0, len(us.cities_list)):
            choice = random.randrange(0, 3)
            if choice == 0:
                population = int(
                    us.cities_list[i].population_growth * us.cities_list[i].population)
                us.cities_list[i].population += population
                us.population += population
            elif choice == 1:
                population = -int(
                    us.cities_list[i].population_growth * us.cities_list[i].population)
                us.cities_list[i].population += population
                us.population += population
            elif choice == 2:
                us.cities_list[i].population = us.cities_list[i].population

            us_elections(us)

            if us.stablility < 0.2:
                print("The United States has become too unstable of a nation.\n"
                      "Time to defect to a different nation!!!")
                defection(avar, us)

#===============================================================================
#initial piece of american front

def initial_stats(us):
    for i in range(random.randrange(500000, 2000000)):
        soldier = united_states.AmericanSoldier()
        us.troops.append(soldier)
    for i in range(random.randrange(2000, 16000)):
        m60 = united_states.M60()
        us.tanks.append(m60)
    for i in range(random.randrange(200, 600)):
        magach = united_states.Magach()
        us.tanks.append(magach)
    for i in range(len(us.cities_list)):
        us.population += us.cities_list[i].population

def main(avar):
    us = united_states.UnitedStates()
    us.cities_list = united_states.us_locations()
    initial_stats(us)

    us_front(avar, us)
if __name__ == '__main__':
    main()