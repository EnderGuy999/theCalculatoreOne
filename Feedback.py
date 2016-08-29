import datetime
import getpass
import os


def feedback():
    spaceCounter = 0
    inputFeedback = input("Do you want to give feedback.(yes or no)\n")
    if "y" in inputFeedback:
        name = input("Would you please put your username.\n")
        feedbackText = input("Type your thoughts now.\n")

        feedbackFolderName = "C:/Users/" + getpass.getuser() + "/Desktop/FeedbackFolder/"
        if not os.path.exists(feedbackFolderName):
            os.makedirs(feedbackFolderName)

        #   parce data with return every 15 spaces.
        for i, q in enumerate(feedbackText):
            if q == " ":
                spaceCounter += 1
            if spaceCounter == 15:
                feedbackText[i] = "\n"

        theDate = str(datetime.datetime.now())
        theDate = theDate.replace(".", "_")
        theDate = theDate.replace(":", "_")
        theDate = theDate.replace(" ", ",")
        nameFile = name + "_" + theDate + ".txt"

        # for u, m in enumerate(nameFile):
        #     if m == " ":
        #         nameFile[u] = "_"

        # if nameFile exists:
        #   ERROR file already exists
        #   quit()
        # else:
        #   feedbackFile = open(nameFile)
        feddbackFile = open(feedbackFolderName + nameFile, "w")

        #   store parced data in text document.
        #   goesInFile = parcedData

        #   close out of document and program.
        #   file.close
        #   quit

        return
    elif "n" in inputFeedback:
        return
    else:
        return
