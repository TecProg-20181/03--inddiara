import random
import string

WORDLIST_FILENAME = "palavras.txt"
GUESSES_EASY = 14
GUESSES_MEDIUM = 8
GUESSES_HARD = 5


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    try:
        inFile = openFile(WORDLIST_FILENAME)
    except IOError:
        print "Could not read file:", WORDLIST_FILENAME
        print "Exiting ..."
        exit()

    line = inFile.readline()
    wordlist = string.split(line)
    print " ", len(wordlist), "words loaded.\n"
    return random.choice(wordlist)


def openFile(fileName):
    inFile = open(fileName, 'r', 0)

    return inFile


def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True


def getGuessedWord():
    guessed = ''
    return guessed


def getAvailableLetters():
    available = string.ascii_lowercase
    return available


def printMenu(secretWord):
    levelIsNotValid = True
    print '\nChoose level:'
    while(levelIsNotValid):
        print '1 - Easy'
        print '2 - Medium'
        print '3 - Hard\n'
        try:
            level = input()
        except NameError:
            print "Level must be a number"
            level = 0

        if(level == 1 or level == 2 or level == 3):
            levelIsNotValid = False
        else:
            print "\nPlease, choose a valid level:"

    print 'I am thinking of a word that is', len(secretWord), ' letters long.\n'
    print '------------------------------------------------\n'

    return level



def updateAvailable(available, lettersGuessed):
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
    return available


def checkGuessed(lettersGuessed, secretWord):
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_'
    return guessed


def checkWin(secretWord, lettersGuessed):
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print 'Congratulations, you won!'
    else:
        print '\nSorry, you ran out of guesses. The word was ', secretWord, '.'

# New functionality to verify mode game chosen by the user {easy, medium, hard}
def mode(level):

    if level == 1:
        guesses = GUESSES_EASY
    elif level == 2:
        guesses = GUESSES_MEDIUM
    elif level == 3:
        guesses = GUESSES_HARD
    else:
        guesses = GUESSES_MEDIUM
    return guesses


def checkLetterInSecretWord(secretWord, lettersGuessed, guesses):
    while isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print '\nYou have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        updateAvailable(available, lettersGuessed)

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:
            guessed = checkGuessed(lettersGuessed, secretWord)

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = checkGuessed(lettersGuessed, secretWord)

            print '\nGood Guess: ', guessed
        else:
            guesses -= 1
            lettersGuessed.append(letter)

            guessed = checkGuessed(lettersGuessed, secretWord)

            print 'Oops! That letter is not in my word: ',  guessed
        print '\n---------------------------------------------\n'

    else:
        checkWin(secretWord, lettersGuessed)


def startGame():
    continuePlay = True
    while continuePlay:

        lettersGuessed = []

        secretWord = loadWords().lower()

        level = printMenu(secretWord)

        guesses = mode(level)

        checkLetterInSecretWord(secretWord, lettersGuessed, guesses)

        continuePlay = menu()

# New functionality for the user to decide what to do after the end of the game
def menu():
    optionIsNotValid = True
    while(optionIsNotValid):
        print 'Press 1 to play again'
        try:
            option = input('Press 2 to exit\n')
        except NameError:
            print "\nOption must be a number"
            option = 0
        if option == 1:
            return True
        elif option == 2:
            return False
        else:
            print "\nChoose a valid number"
            optionIsNotValid = True

def hangman():

    # Calling function to print menu
    print 'Welcome to the game, Hangam!'
    finish = False
    while finish == False:
        finish = startGame()


hangman()
