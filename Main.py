#Main Methods of the Enigma Machine
from Plugboard import Plugboard
# import Scrambler

switchLetters = ["AB", "CD"]
board = Plugboard(switchLetters)

line = "ABCD"
newLine = board.switch(line)
print(newLine)
