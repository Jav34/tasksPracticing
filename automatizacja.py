import os

def createDirectory(name):
    try:
        os.mkdir(os.path.expanduser("~/desktop/%s" % name))

    except FileExistsError:
        pass


def formatFileOuput(labels, inputData, filePath):
    if not os.stat(filePath).st_size:
        fileOutput = "1. "

    else:
        with open(filePath, "r") as fileHandle:
            fileLines = fileHandle.read().splitlines()
            fileOutput = "%i. " % (int(fileLines[len(fileLines) - 2][0]) + 1)

    for iterator, label in enumerate(labels):
        fileOutput += "%s: %s " % (label, inputData[iterator])

    fileOutput += "\n"

    return fileOutput


def saveToFile(directoryName, fileName):
    folderPath = os.path.expanduser("~/desktop/%s" % (directoryName))
    filePath = os.path.join(folderPath, fileName)

    inputLabels = [
        "Tytuł książki",
        "Autor",
        "Rok wydania"
    ]

    userInput = [""] * len(inputLabels)
    fileOutput = ""

    with open(filePath, "a+") as fileHandle:
        for i in range(len(inputLabels)):
            userInput[i] = input(inputLabels[i] + ": ")

        fileHandle.write(formatFileOuput(inputLabels, userInput, filePath))


folderName = "Twoja biblioteka"
fileName = "Biblioteka Książek.txt"



createDirectory(folderName)
saveToFile(folderName, fileName)
