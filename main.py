
# -*- coding: utf-8 -*-
"""
Edmond Tongyou
CPSC 223P-01
Thu April 6, 2021
tongyouedmond@fullerton.edu
"""

import random

# Global variable for alphabet available
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"

# Hangman class.
class Hangman:
    
    def __init__(self, word, triesAllowed):
        self.__word__ = word
        self.__triesAllowed__ = triesAllowed
        self.__displayWord__ = []
        self.__lettersUsed__ = ""
        for index in range(len(self.__word__)):
            self.__displayWord__ += "-"

    # Loops through the word to check if the letter is in it.
    # If it's found then it will replace the index in displayWord
    # which corresponds with the index found.
    def Guess(self, letter):
        letterFound = False
        if len(letter) != 1:
            print("Please enter only one letter.")
            return False
        if letter not in ASCII_LOWERCASE:
            print("Please enter a letter you haven't already used.")
            return False

        else:
            for index in range(len(self.__word__)):
                if letter in self.__word__[index]:
                    self.__displayWord__[index] = letter 
                    letterFound = True

        self.__lettersUsed__ += letter

        if not letterFound:
            self.__triesAllowed__ -= 1
            return False

        else:
            return True

    # Returns the number of tries left.
    def GetNumTriesLeft(self):
        return self.__triesAllowed__
    
    # Returns the displayed word.
    def GetDisplayWord(self):
        strDisplayWord = ''.join(self.__displayWord__)
        return strDisplayWord

    # Returns the letters used in order of guessed letters.
    def GetLettersUsed(self):
        return self.__lettersUsed__

    def GetGameResult(self):
        """Return True if all letters have been guessed. False otherwise"""
        if self.GetNumTriesLeft() == 0:
            print("You Lost.")
            return True

        if self.__word__ == self.GetDisplayWord():
            print("You Won!")
            return True

        else:
            return False

    # Returns ASCII Art of Gallows current state
    def DrawGallows(self):
        tries = 8 - self.GetNumTriesLeft()
        gallowsList = []
        guesses = [" |   |",
                   " |   0", 
                   " |  /",
                   " |  /|",
                   " |  /|\\",
                   " |   U",
                   " |  /",
                   " |  / \\"]

        

        for index in range(0, 8):
            if index < tries:
                if (index == 2 and tries > 3) or (index == 3 and tries > 4) or (index == 6 and tries > 7):
                    continue
                else:
                    gallowsList.append(guesses[index])

            else:
                gallowsList.append(" |")

        print("-----|")
        for x in range(0, len(gallowsList)):
            print(gallowsList[x])
        print("---")

if __name__=="__main__":
    # Read all the words from the hangman_words.txt file
    wordFile = open("hangman_words.txt", "r")
    wordFileText = wordFile.read()
    wordFile.close()
    
    # Seed the random number generator with current system time
    random.seed()
    
    # Converts the wordFileText from a file to a list, then
    # picks a random number to select the word to choose for
    # the hangman game.
    wordList = wordFileText.split()
    randomIndex = random.randint(1, 222773)

    
    # Instantiate a game using the Hangman class with 8 tries
    newGame = Hangman(wordList[randomIndex], 8)

    # Use a while loop to play the game
    while newGame.GetGameResult() is False:
        print(newGame.GetNumTriesLeft())
        print("Please guess a character that you haven't already guessed.")
        print(ASCII_LOWERCASE)
        print(newGame.GetDisplayWord())
        letter = input()
        newGame.Guess(letter)
        ASCII_LOWERCASE = ASCII_LOWERCASE.replace(letter, "")
        newGame.DrawGallows()
        print("")

    print("The word was " + newGame.__word__)