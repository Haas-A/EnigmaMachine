#File for Plugboard class

#The plugboard class will switch the letters in the message according to the letters to be switched.
#lettersToSwitch will contain the letters to switch in the format ("AB", "EY", etc.)
#message will be a list of strings, each string being a line in the message

class Plugboard(lettersToSwitch):
    plugSwitches = {}
    def __init__(self, lettersToSwitch, Lines):
        for pair in lettersToSwitch:
            letOne = pair[0]
            letTwo = pair[1]
            plugSwitches[letOne] = letTwo
            plugSwitches[letTwo] = letOne
    def switch(self, message):
        switchedMessage = []
        for line in message:
            switchedLine = ""
            for letter in line:
                if letter in plugSwitches:
                    switchedLine = switchedLine + plugSwitches[letter]
                else:
                    switchedLine = switchedLine + letter
            switchedMessage = switchedMessage + switchedLine + "\n"
        return switchedMessage
    #class here
#yo
