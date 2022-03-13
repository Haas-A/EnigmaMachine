#File with the Scrambler class used in Main.py

#The plugboard class will switch the letters in the message according to the letters to be switched.
#lettersToSwitch will contain the letters to switch in the format ("AB", "EY", etc.)
#message will be a list of strings, each string being a line in the message

class Scrambler():
    setting = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ""
    settingOne = "KLHYTQJCBXPADVGZOMFUNIESRW"
    settingTwo = "UPBKFOYZDEWRIAHQVJNCMXGTSL"
    settingThree = "EKOAZRMTCNIXDBYUPHGWQSFLJV"

    def __init__(self, selectedScramblerSetting):
        self.setting = selectedScramblerSetting
        if selectedScramblerSetting == 1:
            self.key = self.settingOne
        elif selectedScramblerSetting == 2:
            self.key = self.settingTwo
        elif selectedScramblerSetting == 3:
            self.key = self.settingThree

    def scramble(self, lines):
        scrambledLines = ""
        for line in lines:
            scrambledLine = ""
            for letter in line:
                print(letter)
                if letter in self.alphabet:
                    index = self.alphabet.index(letter)
                    scrambledLine = scrambledLine + self.key[index]
                else:
                    scrambledLine = scrambledLine + letter
            scrambledLines = scrambledLines + scrambledLine
        return scrambledLines

    def unscramble(self, lines):
        unScrambledLines = ""
        for line in lines:
            unScrambledLine = ""
            for letter in line:
                if letter in self.key:
                    index = self.key.index(letter)
                    unScrambledLine = unScrambledLine + self.alphabet[index]
                else:
                    unScrambledLine = unScrambledLine + letter
            unScrambledLines = unScrambledLines + unScrambledLine
        return unScrambledLines
#ABCDEFGHIJKLMNOPQRSTUVWXYZ






