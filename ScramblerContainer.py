#Holds Scramblers and rotates them for the user

from Scrambler import Scrambler

class ScramblerContainer:
    first = None
    second = None
    third = None
    scrambledMessage = ""

    def setScramblers(self, fScrambler, sScrambler, tScrambler):
        self.first = fScrambler
        self.second = sScrambler
        self.third = tScrambler

    def type(self, lines):
        firstRotationCounter = 0
        secondRotationCounter = 0
        thirdRotationCounter = 0
        for line in lines:
            for letter in line:
                isLetter, scrambledLetter = self.first.scramble(letter)
                if isLetter == 1:
                    firstRotationCounter = firstRotationCounter + 1
                    self.first.rotate()
                    isLetter, scrambledLetter = self.second.scramble(scrambledLetter)
                    isLetter, scrambledLetter = self.third.scramble(scrambledLetter)
                    self.scrambledMessage = self.scrambledMessage + scrambledLetter
                if firstRotationCounter == 26:
                    self.second.rotate()
                    firstRotationCounter = 0
                    secondRotationCounter = secondRotationCounter + 1
                if secondRotationCounter == 26:
                    self.third.rotate()
                    secondRotationCounter = 0
                    thirdRotationCounter = thirdRotationCounter + 1
                if thirdRotationCounter == 26:
                    thirdRotationCounter = 0

    def printMessage(self):
        counter = 0
        for letter in self.scrambledMessage:
            if counter < 4:
                counter = counter + 1
                print(letter,end="")
            elif counter == 4:
                counter = 0
                print(letter,end=" ")

    def decrypt(self, lines):
        firstRotationCounter = 0
        secondRotationCounter = 0
        thirdRotationCounter = 0
        for line in lines:
            for letter in line:
                #TODO
                #Adjust the following code to decrypt, rather than encrypt.
                isLetter, scrambledLetter = self.third.unscramble(letter)
                if isLetter == 1:
                    firstRotationCounter = firstRotationCounter + 1
                    isLetter, scrambledLetter = self.second.unscramble(scrambledLetter)
                    isLetter, scrambledLetter = self.first.unscramble(scrambledLetter)
                    self.scrambledMessage = self.scrambledMessage + scrambledLetter
                    self.first.rotate()
                if firstRotationCounter == 26:
                    self.second.rotate()
                    firstRotationCounter = 0
                    secondRotationCounter = secondRotationCounter + 1
                if secondRotationCounter == 26:
                    self.third.rotate()
                    secondRotationCounter = 0
                    thirdRotationCounter = thirdRotationCounter + 1
                if thirdRotationCounter == 26:
                    thirdRotationCounter = 0
