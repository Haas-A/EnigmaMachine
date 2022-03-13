#File for Plugboard class

#The plugboard class will switch the letters in the message according to the letters to be switched.
#lettersToSwitch will contain the letters to switch in the format ("AB", "EY", etc.)
#message will be a list of strings, each string being a line in the message

class Plugboard():
    plugSwitches = {}
    lettersToSwitch = []
    def __init__(self, lettersToSwitch):
        plugSwitch = {}
        for pair in lettersToSwitch:
            letOne = pair[0]
            letTwo = pair[1]
            self.plugSwitches[letOne] = letTwo
            self.plugSwitches[letTwo] = letOne
        plugSwitches = plugSwitch
    def switch(self, message):
        switchedMessage = ""
        for line in message:
            switchedLine = ""
            for letter in line:
                if letter in self.plugSwitches:
                    switchedLine = switchedLine + self.plugSwitches[letter]
                else:
                    switchedLine = switchedLine + letter
            switchedMessage = switchedMessage + switchedLine
        return switchedMessage
    #class here
#yo
