SubtractingStarfish = False


def Seahorse():
    global SubtractingStarfish
    SubtractingStarfish = True
    while SubtractingStarfish is True:
        Oyster()


def Oyster():
    global SubtractingStarfish
    print("This is the subtracting function.")
    print("Now put in the first number you want to subtract and press enter.")
    Coral = input()
    print("Now put in the second number you want to subtract and press enter.")
    SeaCucumber = input()
    print(round(float(Coral) - float(SeaCucumber), 1))
    print("Do you want to subtract again.(Yes or No)")
    Angelfish = input().lower()
    if "y" in Angelfish:
        return
    elif "n" in Angelfish:
        SubtractingStarfish = False
    else:
        print("I assumed you said yes.")
        return