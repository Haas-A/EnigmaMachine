#Main Methods of the Enigma Machine
from Plugboard import Plugboard
from Scrambler import Scrambler
# import Scrambler


print("Select an Enigma method:")
type = input("1. File Auto Encrypt\n2. File Auto Decrypt\n3. Old School Encrypt and Decrypt\n")

if type == 1:
    fileAutoEncrypt()
elif type == 2:
    fileAutoDecrypt()
elif type == 3:
    oldSchool()
else:
    error("Invalid Input")

def fileAutoEncrypt():
    filename = input("Enter the filename of the message to encrypt (file.txt):\n")
    file = open(filename, "r")
    diskOneSetting = input("Which disk would you like to use for disk 1:\n")
    diskTwoSetting = input("Which disk would you like to use for disk 2:\n")
    diskThreeSetting = input("Which disk would you like to use for disk 3:\n")


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
