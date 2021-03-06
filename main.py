import sys
import traceback
from Feedback import feedback
from addingStuff import Starfish
from subtractingStuff import Seahorse


def intruck():
    print("***************************************************")
    print("* Type the number for the corresponding function. *")
    print("* 1: +                                            *")
    print("* 2: -                                            *")
    print("* 3: Quit                                         *")
    print("***************************************************")
    imputHandle()


def imputHandle():
    try:
        Jellyfish = input()

        if Jellyfish == "1":
            Starfish()

        elif Jellyfish == "2":
            Seahorse()

        elif Jellyfish == "3":
            feedback()
            sys.exit()

        elif Jellyfish == "":
            print("\n")
            imputHandle()

        else:
            print(str(Jellyfish) + " is not a valid command plz try again.")

    except SystemExit:
        quit()

    except (OSError, TypeError):
        traceback.print_exc()
        quit()

while True:
    intruck()
