# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if secretWord == '':
        return True
    elif secretWord[0] in lettersGuessed:
        return True and isWordGuessed(secretWord[1:], lettersGuessed)
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters_left = string.ascii_lowercase
    for letter in letters_left:
        if letter in lettersGuessed:
            letters_left = letters_left.replace(letter, '')
    return letters_left
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", len(secretWord), "letters long."
    print "------------"
    turns = 0
    lettersGuessed = ''
    while isWordGuessed(secretWord, lettersGuessed) == False and turns < 8:
        print "You have", 8 - turns, "guesses left."
        print "Available letters:", getAvailableLetters(lettersGuessed)
        guess = str(raw_input("Please guess a letter: ")).lower()
        if guess in lettersGuessed:
            guessed_word = getGuessedWord(secretWord, lettersGuessed)
            print "Oops! You've already guessed that letter:", guessed_word
            print "------------"
            print "You have", 8 - turns, "guesses left."
            print "Available letters:", getAvailableLetters(lettersGuessed)
            guess = str(raw_input("Please guess a letter: ")).lower()
        elif guess in secretWord:
            lettersGuessed += guess
            guessed_word = getGuessedWord(secretWord, lettersGuessed)
            print "Good guess:", guessed_word
        else:
            lettersGuessed += guess
            guessed_word = getGuessedWord(secretWord, lettersGuessed)
            print "Oops! That letter is not in my word:", guessed_word
            turns += 1
        print "------------"
    if isWordGuessed(secretWord, lettersGuessed) == False and turns == 8:
        print "Sorry, you ran out of guesses. The word was", secretWord + "."
    elif isWordGuessed(secretWord, lettersGuessed) == True:
        print "Congratulations, you won!"


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
secretWord = 'sea'
hangman(secretWord)