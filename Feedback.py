import datetime
import getpass
import os

def giveName():
    # dirtyName = input("Would you please put your username.\n")
    # if filterChars(dirtyName, ("/", "\\", ":", "*", "?", "|", "<", ">")):
    #     giveName()
    #     pass
    # cleanName = dirtyName
    cleanName = input("Would you please put your username.\n")
    return cleanName


def feedback():
    spaceCounter = 0
    pFeedback = ""
    inputFeedback = input("Do you want to give feedback.(yes or no)\n")
    if "y" in inputFeedback:
        name = ""
        while filterChars(name, ("/", "\\", ":", "*", "?", "|", "<", ">")) or not name:
            name = giveName()

        feedbackText = input("Type your thoughts now.\n")

        #   parce data with return every 15 spaces.
        for i in feedbackText:
            if i == " ":
                if spaceCounter == 15:
                    pFeedback += "\n"
                    spaceCounter = 0
                else:
                    spaceCounter += 1
                    pFeedback += i

            else:
                pFeedback += i

        MKTXTFILE(name, pFeedback)

        return
    elif "n" in inputFeedback:
        return
    else:
        print("You have entered a something that doesn't have a y/n in it, please try again.")
        feedback()


def filterChars(text, Forb):
    for x in text:
        if x in Forb:
            print("Your Have Entered One Or More Forbiden Characters Please Try Again. List(/\:*?|<>)")
            #return error
            return True
    #no error
    return False


def MKTXTFILE(name = "DEFAULT", message = "NO MESSAGE WAS GIVEN TO PROGRAM!!"):

    feedbackFolderName = "C:/Users/" + getpass.getuser() + "/Desktop/FeedbackFolder/"

    if not os.path.exists(feedbackFolderName):
        os.makedirs(feedbackFolderName)

    theDate = str(datetime.datetime.now())
    theDate = theDate.replace(".", "_")
    theDate = theDate.replace(":", "_")
    theDate = theDate.replace(" ", ",")
    nameFile = str(name) + "_" + theDate + ".txt"

    fewebackFile = open(feedbackFolderName + nameFile, "w")

    fewebackFile.write(message)

    fewebackFile.close()

    fullPath = feedbackFolderName + nameFile

    if os.path.exists(fullPath):
        print("Your feedback has been recorded. Thank you for using my calculator. " + fullPath)
        return

    else:
        print("Opps! Something has gone wrong in " + fullPath)
        raise SystemExit
