import random
from shanghai_pact import north_korea
from avatar import avatar_file
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
    print("There is no feasible way to commit terrorism in North Korea")
    avar.alive = True

def eat(avar):
    print("still a work in progress")

def drink(avar):
    print("still a work in progress")

def change_name(avar):
    avar.name = input("What do you want to be called now?: ")

def disloyalty(avar, korea, chance):
    if chance % 4 == 3:
        print("The north koreans discovered that you aren't loyal to the Kim Regime.")
        punishment = random.randrange(0, 4)
        if punishment == 0:
            print(korea.leader + " decided to make you a live experiment")
            avar.alive = True
        elif punishment == 1:
            print(korea.leader + " decided to disembowel you")
            avar.alive = True
        elif punishment == 2:
            print(korea.leader + " decided to send you to a re-education camp")
            avar.alive = True
        elif punishment == 3:
            print(korea.leader + " decided to shoot you with an anti-aircraft gun")
            avar.alive = True

def random_events(avar, korea):
    chance = random.randrange(0, 1000)

    if chance % 5 == 3:
        print("You stumbled across a group of people that may be willing to listen to a speech.")
        choice = input("\ndo you accept?: ")
        if choice.lower() == "yes":
            discovery = random.randrange(1, 10)
            if discovery % 10 == 3:
                disloyalty(avar, korea, chance)
            else:
                followers = random.randrange(1, 76)
                for i in range(followers):
                    follower = avatar_file.Partisan()
                    avar.partisan_list.append(follower)
    elif chance % 10 == 5:
        print("You stepped on a landmine and fucking died")
        avar.alive = True

    elif chance % 20 == 3:
        accept = input("You came across a tank. Do you want to steal it?: ")
        if accept.lower() == "yes":
            avar.weapons_list.append("tank")
            disloyalty(avar, korea, chance)
        else:
            print("you made a wise decision")

def view_stats(avar, korea):
    print(f"You have killed {avar.kills} people")
    print(f"Your current name is " + avar.name)
    print(f"Your health level is {avar.health}")
    print(f"You have {avar.hunger} in hunger")
    print(f"You have {avar.thirst} in thirst")
    print(f"You have {len(avar.partisan_list)} followers")
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

        random_events(avar, korea)

        for i in range(0, len(korea.cities_list)):
            choice = random.randrange(0, 3)
            if choice == 0:
                population = int(
                    korea.cities_list[i].population_growth * korea.cities_list[i].population)
                korea.cities_list[i].population += population
                korea.population += population
            elif choice == 1:
                population = -int(
                    korea.cities_list[i].population_growth * korea.cities_list[i].population)
                korea.cities_list[i].population += population
                korea.population += population
            elif choice == 2:
                korea.cities_list[i].population = korea.cities_list[i].population

def main(avar):
    korea = north_korea.NorthKorea()
    korea.cities_list = north_korea.dprk_locations()

    northkorean_front(avar, korea)

if __name__ == '__main__':
    main()