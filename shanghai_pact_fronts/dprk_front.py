import random

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
    #if new_nation == 5:
        #dutch_front.main(avar)


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

def view_stats(avar, korea):
    print(f"You have killed {avar.kills} people")
    print(f"Your current name is " + avar.name)
    print(f"Your health level is {avar.health}")
    print(f"You have {avar.hunger} in hunger")
    print(f"You have {avar.thirst} in thirst")
    print(f"The nation you currently reside in has a population of {korea.population}")

def northkorean_front(avar, korea):
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
        print(f"\nIt is {korea.year}.")
        korea.year += 1
        print(korea.cities_list[current_city].description)

        for i in range(len(choices)):
            print(choices[i])
        first_choice = int(input("what is your choice 1-8?: "))
        if first_choice == 1:

            for i in range(len(directions)):
                print(directions[i])
            second_choice = int(input("what direction do you choose? 1 - 8: "))

            if second_choice == 1:
                next_city = korea.cities_list[current_city].north
                if korea.cities_list[current_city].north is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 2:
                next_city = korea.cities_list[current_city].north_east
                if korea.cities_list[current_city].north_east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 3:
                next_city = korea.cities_list[current_city].east
                if korea.cities_list[current_city].east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")

                else:
                    current_city = next_city

            elif second_choice == 4:
                next_city = korea.cities_list[current_city].south_east
                if korea.cities_list[current_city].south_east is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 5:
                next_city = korea.cities_list[current_city].south
                if korea.cities_list[current_city].south is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 6:
                next_city = korea.cities_list[current_city].south_west
                if korea.cities_list[current_city].south_west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 7:
                next_city = korea.cities_list[current_city].west
                if korea.cities_list[current_city].west is None:
                    print("Oh no...You can't go that way. Read the directions!!!")
                else:
                    current_city = next_city

            elif second_choice == 8:
                next_city = korea.cities_list[current_city].north_west
                if korea.cities_list[current_city].north_west is None:
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
            view_stats(avar, korea)

def main():

    northkorean_front()