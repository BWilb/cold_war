from avatar import avatar_file
from nato_fronts import us_front
from nato_fronts import dutch_front
from shanghai_pact_fronts import dprk_front

#this entire file steers where the game and your path

def main():
    avar = avatar_file.Avatar()
    print("Hello " + avar.name + ".\nYou have been resurrected in the year 1960. The Cold War has been"
                                 " underway for 15 years now.\nTensions between NATO, Warsaw Pact, and Shanghai Pact"
                                 "are at an all time high.\nYou can choose any side and either help them or fuck with them.\n")
    #beginning of
    name_change = input("Your name is currently " + avar.name + ". Would you like to change it?: ")
    if name_change.lower() == "yes":
        avar.name = input("Good choice. What would you like to change your name to?: ")
        print(avar.name + " it is")
    elif name_change.lower() == "no":
        print("good luck")
    else:
        print("This is a yes or no question. Don't be stupid.")

    nato = ["1. Britain", "2. France", "3. West Germany", "4. Belgium", "5. Netherlands",
            "6. Italy", "7. Turkey", "8. United States"]

    warsaw_pact = ["1. Soviet Union", "2. DRG", "3. Romania", "4. Hungary", "5. Poland", "6. Czechoslovakia"]

    shanghai_pact = ["1. China", "2. North Korea", "3. Mongolia", "4. Vietnam", "5. Cambodia"]

    non_alligned = ["1. Egypt", "2. India", "3. Indonesia", "4. Mexico"]

    side = input("Do you choose NATO, the Warsaw Pact, or the Shanghai Pact?: ")
    if side.lower() == "nato":
        print("\nAvailable NATO nations....")
        for i in range(len(nato)):
            print(nato[i])
        user_choice = int(input("which nation do you choose based off the numbers?: "))
        if user_choice == 1:
            #british_front.main()
            print("option not available")
        elif user_choice == 2:
            #french_front.main()
            print("option not available")
        elif user_choice == 3:
            #west_german_front.main()
            print("option not available")
        elif user_choice == 4:
            #belgian_front.main()
            print("option not available")
        elif user_choice == 5:
            dutch_front.main(avar)
            print("option not available")
        elif user_choice == 6:
            #italian_front.main()
            print("option not available")
        elif user_choice == 7:
            #turkish_front.main()
            print("option not available")
        elif user_choice == 8:
            us_front.main(avar)

    elif side.lower() == "warsaw pact":
        print("\nAvailable Warsaw Pact nations")
        for i in range(len(warsaw_pact)):
            print(warsaw_pact[i])
        user_choice = int(input("which nation do you choose?: "))
        if user_choice == 1:
            #ussr_front.main()
            print("option not available")
        elif user_choice == 2:
            #drg_front.main()
            print("option not available")
        elif user_choice == 3:
            #czechoslovakian_front.main()
            print("option not available")
        elif user_choice == 4:
            #hungarian_front.main()
            print("option not available")
        elif user_choice == 5:
            #romanian_front.main()
            print("option not available")
        elif user_choice == 6:
            #polish_front.main()
            print("option not available")

    elif side.lower() == "Shanghai pact":
        print("\nAvailable shanghai Pact nations")
        print("None available at current time")
        for i in range(len(shanghai_pact)):
            print(shanghai_pact[i])
        user_choice = int(input("which nation do you choose?: "))
        #if user_choice == 1:
        #    chinese_front.main()
        if user_choice == 2:
            dprk_front.main()
        #elif user_choice == 3:
        #    mongolian_front.main()
        #elif user_choice == 4:
        #    vietnamese_front.main()
        #elif user_choice == 5:
        #    cambodian_front.main()

if __name__ == '__main__':
    main()