SubtractingStarfish = False


def Seahorse():
    global SubtractingStarfish
    SubtractingStarfish = True
    while SubtractingStarfish is True:
        subtractingFuncion()


def subtractingFuncion():
    global SubtractingStarfish
    print("This is the subtracting function.")
    print("Now put in the first number you want to subtract and press enter.")
    Coral = input()

    print("Now put in the second number you want to subtract and press enter.")
    SeaCucumber = input()

    try:
        print(round(float(Coral) - float(SeaCucumber), 1))
        print("Do you want to subtract again.(Yes or No)")
        Angelfish = input().lower()

    except TypeError:
        print("You have entered a character or word that is not a number, please try again.")
        subtractingFuncion()

    if "y" in Angelfish:
        return
    elif "n" in Angelfish:
        SubtractingStarfish = False
    else:
        print("I assumed you said yes.")
        return