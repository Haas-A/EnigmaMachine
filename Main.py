#Main Methods of the Enigma Machine
from Plugboard import Plugboard
from Scrambler import Scrambler
# import Scrambler

switchLetters = ["AB", "CD"]
board = Plugboard(switchLetters)
disk = Scrambler(1)

message = "ABCD \n HI"
newLine = board.switch(message)
scrambledLine = disk.scramble(message)
print("Orginal Message:")
print(message)
print("Plugged Message:")
print(newLine)
unPluggedLine = board.switch(newLine)
print("UnPluggedMessage")
print(unPluggedLine)
# print("Scrambled Message:")
# print(scrambledLine)
# unscrambledLine = disk.unscramble(scrambledLine)
# print("Unscrambled Scrambled Message:")
# print(unscrambledLine)
# print(message)
# print(newLine)


