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

    def scramble(self, letter):
        result = 0
        index = 0
        if letter in self.alphabet:
            result = 1
            index = self.alphabet.index(letter)
        return result, self.key[index]

    def unscramble(self, lines):
        #TODO
        #Remake the unscramble method to unscramble the message one letter at a time.

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

    def rotate(self):
        self.key = self.key[1:25] + self.key[0]

#ABCDEFGHIJKLMNOPQRSTUVWXYZ






