import datetime


def feedback():
    spaceCounter = 0
    inputFeedback = input("Do you want to give feedback.(yes or no)\n")
    if "y" in inputFeedback:
        name = input("Would you please put your username.\n")
        feedbackText = input("Type your thoughts now.\n")

        #   parce data with return every 15 spaces.
        for i, q in enumerate(feedbackText):
            if q == " ":
                spaceCounter += 1
            if spaceCounter == 15:
                feedbackText[i] = "\n"

        print(feedbackText)

        nameFile = name + "_" + str(datetime.datetime.now()) + ".txt"

        # if nameFile exists:
        #   ERROR file already exists
        #   quit()
        # else:
        #   feedbackFile = open(nameFile)

        feddbackFile = open(nameFile)



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
