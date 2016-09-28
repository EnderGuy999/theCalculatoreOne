AddingStarfish = False


def Starfish():
    global AddingStarfish
    AddingStarfish = True

    while AddingStarfish is True:
        addingFunction()


def addingFunction():
    global AddingStarfish

    print("This is the addition function.")
    print("Now put in the first number you want to add and press enter.")
    Seal = input()

    print("Now put in the second number you want to add and press enter.")
    seaLion = input()

    try:
        print(round(float(Seal) + float(seaLion), 1))
        print("Do you want to add again.(Yes or No)")
        hermitCrab = input().lower()

        if "y" in hermitCrab:
            return

        elif "n" in hermitCrab:
            AddingStarfish = False

        else:
            print("I assumed you said yes.")
            return

    except (TypeError, ValueError):
        print("You have entered a character or word that is not a number, please try again.")
        addingFunction()

