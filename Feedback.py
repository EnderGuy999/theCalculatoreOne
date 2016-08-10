import os


def feedback():
    inputFeedback = input("Do you want to give feedback.(yes or no)\n")
    if "y" in inputFeedback:
        feedbackText = input("Type your thoughts now.\n")
        newFolder = r'C:\Program Files\feedback'
        if not os.path.exists(newFolder):
            os.makedirs(newFolder)
        #   parce data with return every 15 words.
        #   store parced data in text document.
        #   close out of document and program.
        return
    elif "n" in inputFeedback:
        return
    else:
        return