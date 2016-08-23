import datetime


def feedback():
    inputFeedback = input("Do you want to give feedback.(yes or no)\n")
    if "y" in inputFeedback:
        name = input("Would you please put your username.\n")
        feedbackText = input("Type your thoughts now.\n")
        nameFile = name + "_" + str(datetime.datetime.now())

        #   if nameFile exists:
        #       ERROR file already exists
        #       quit()
        #   else:
        #       create the file with the name being nameFile

        #   parce data with return every 15 spaces.
        # parceData()

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
