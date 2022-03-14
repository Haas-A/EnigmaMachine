#Main Methods of the Enigma Machine
from Plugboard import Plugboard
from Scrambler import Scrambler
# import Scrambler

def fileAutoEncrypt():
    print("in function")
    filename = input("Enter the filename of the message to encrypt (file.txt):\n")
    file = open(filename, "r")
    plugs = int(input("How many plugboard switches would you like to use?\n"))
    switchLetters = []
    while plugs > 0:
        pair = input("Enter two letters to switch in the plugboard (AB):\n")
        switchLetters.append(pair)
        plugs = plugs - 1
    board = Plugboard(switchLetters)
    diskOneSetting = int(input("Which disk would you like to use for disk 1 (1-3):\n"))
    diskTwoSetting = int(input("Which disk would you like to use for disk 2 (1-3):\n"))
    diskThreeSetting = int(input("Which disk would you like to use for disk 3 (1-3):\n"))
    diskOne = Scrambler(diskOneSetting)
    diskTwo = Scrambler(diskTwoSetting)
    diskThree = Scrambler(diskThreeSetting)
    lines = file.readlines()
    linesUpper = []
    for eachLine in lines:
        linesUpper.append(eachLine.upper())
    encryptedMessage = board.switch(linesUpper)
    encryptedMessage = diskOne.scramble(encryptedMessage)
    encryptedMessage = diskTwo.scramble(encryptedMessage)
    encryptedMessage = diskThree.scramble(encryptedMessage)
    print(encryptedMessage)
    #TODO: Add the reflector here after creating a reflector class and object
    return

print("Select an Enigma method:")
type = int(input("1. File Auto Encrypt\n2. File Auto Decrypt\n3. Old School Encrypt and Decrypt\n"))

if type == 1:
    fileAutoEncrypt()
elif type == 2:
    fileAutoDecrypt()
elif type == 3:
    oldSchool()
else:
    print("here")
    x=5
    # error("Invalid Input")



def fileAutoDecrypt():
    x = 5

def oldSchool():
    x = 5

#Prints to test the functionality of the different parts of the program
# switchLetters = ["AB", "CD"]
# board = Plugboard(switchLetters)
# disk = Scrambler(1)
# message = "ABCD \n HI"
# newLine = board.switch(message)
# scrambledLine = disk.scramble(message)
# print("Orginal Message:")
# print(message)
# print("Plugged Message:")
# print(newLine)
# unPluggedLine = board.switch(newLine)
# print("UnPluggedMessage")
# print(unPluggedLine)
# print("Scrambled Message:")
# print(scrambledLine)
# unscrambledLine = disk.unscramble(scrambledLine)
# print("Unscrambled Scrambled Message:")
# print(unscrambledLine)
# print(message)
# print(newLine)

#1. File Auto Encrypt
#2. File Auto Decrypt
#3. Old School Encrypt
