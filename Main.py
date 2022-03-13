#Main Methods of the Enigma Machine
from Plugboard import Plugboard
from Scrambler import Scrambler
# import Scrambler

switchLetters = ["AB", "CD"]
board = Plugboard(switchLetters)
disk = Scrambler(1)

message = "ABCD \n ABCD"
newLine = board.switch(message)
scrambledLine = disk.scramble(message)
print(message)
print(scrambledLine)
unscrambledLine = disk.unscramble(scrambledLine)
print(unscrambledLine)
# print(message)
# print(newLine)


