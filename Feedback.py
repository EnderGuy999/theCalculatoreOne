import datetime
import getpass
import os


def feedback():
    spaceCounter = 0
    pFeedback = ""
    inputFeedback = input("Do you want to give feedback.(yes or no)\n")
    if "y" in inputFeedback:
        name = input("Would you please put your username.\n")
        feedbackText = input("Type your thoughts now.\n")

        feedbackFolderName = "C:/Users/" + getpass.getuser() + "/Desktop/FeedbackFolder/"
        if not os.path.exists(feedbackFolderName):
            os.makedirs(feedbackFolderName)

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

        theDate = str(datetime.datetime.now())
        theDate = theDate.replace(".", "_")
        theDate = theDate.replace(":", "_")
        theDate = theDate.replace(" ", ",")
        nameFile = name + "_" + theDate + ".txt"

        fewebackFile = open(feedbackFolderName + nameFile, "w")

        fewebackFile.write(pFeedback)

        fewebackFile.close()
        return
    elif "n" in inputFeedback:
        return
    else:
        return
