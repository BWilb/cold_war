from avatar import avatar_file
from nato import netherlands
import random

def defection(avar):
    print("You chose to defect")

def begin_rebellion(avar):
    print("you chose to rebel")

def commit_terror(avar):
    print("you chose to commit terror")

def eat(avar):
    print("you chose to eat")

def drink(avar):
    print("you chose to drink")

def change_name(avar):
    print("you decided to change your name")

def view_stats(avar, dutch):
    print(f"You have killed {avar.kills} people")
    print(f"Your current name is " + avar.name)
    print(f"Your health level is {avar.health}")
    print(f"You have {avar.hunger} in hunger")
    print(f"You have {avar.thirst} in thirst")
    print(f"The nation you currently reside in has a population of {dutch.population}")

#main chunk of game
def dutch_front(avar, dutch):
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
        print("\n" + dutch.cities_list[current_city].description)

        for i in range(len(choices)):
            print(choices[i])
        first_choice = int(input("what is your choice 1-8?: "))
        if first_choice == 1:

            for i in range(len(directions)):
                print(directions[i])
            second_choice = int(input("what direction do you choose? 1 - 8: "))

            if second_choice == 1:
                next_city = dutch.cities_list[current_city].north
                if dutch.cities_list[current_city].north is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 2:
                next_city = dutch.cities_list[current_city].north_east
                if dutch.cities_list[current_city].north_east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 3:
                next_city = dutch.cities_list[current_city].east
                if dutch.cities_list[current_city].east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")

                else:
                    current_city = next_city

            elif second_choice == 4:
                next_city = dutch.cities_list[current_city].south_east
                if dutch.cities_list[current_city].south_east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 5:
                next_city = dutch.cities_list[current_city].south
                if dutch.cities_list[current_city].south is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 6:
                next_city = dutch.cities_list[current_city].south_west
                if dutch.cities_list[current_city].south_west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 7:
                next_city = dutch.cities_list[current_city].west
                if dutch.cities_list[current_city].west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 8:
                next_city = dutch.cities_list[current_city].north_west
                if dutch.cities_list[current_city].north_west is None:
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
            view_stats(avar, dutch)

        for i in range(0, len(dutch.cities_list)):
            choice = random.randrange(0, 3)
            population = 0
            print(choice)
            if choice == 0:
                population = int(
                    dutch.cities_list[i].population_growth * dutch.cities_list[i].population)
                dutch.cities_list[i].population += population
                dutch.population += population
                print(dutch.cities_list[i].description)
            elif choice == 1:
                population = -int(
                    dutch.cities_list[i].population_growth * dutch.cities_list[i].population)
                dutch.cities_list[i].population += population
                dutch.population += population
            elif choice == 2:
                dutch.cities_list[i].population = dutch.cities_list[i].population

#===============================================================================
#beginning of dutch front

def initial_stats(dutch):
    for i in range(random.randrange(250000, 500000)):
        soldier = netherlands.DutchSoldier()
        dutch.troop_list.append(soldier)
    for i in range(len(dutch.cities_list)):
        dutch.population += dutch.cities_list[i].population

def main():
    avar = avatar_file.Avatar()
    dutch = netherlands.Netherlands()
    dutch.cities_list = netherlands.dutch_cities()
    initial_stats(dutch)

    dutch_front(avar, dutch)