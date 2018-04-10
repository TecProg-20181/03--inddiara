import random
import string

WORDLIST_FILENAME = "palavras.txt"


def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = openFile(WORDLIST_FILENAME)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print " ", len(wordlist), "words loaded.\n"
    return random.choice(wordlist)


def openFile(fileName):
    # inFile: file
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
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase

    return available


def printMenu(secretWord):
    # print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.\n'
    print '------------------------------------------------\n'


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
        print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


def ifif():
    guesses = 8
    lettersGuessed = []

    secretWord = loadWords().lower()

    printMenu(secretWord)

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

    print('Press 1 to play again')
    option = raw_input('Press 2 to exit\n')
    if option == '1':
        return False
    elif option == '2':
        return True
    else:
        quit()


def hangman():

    # Calling function to print menu
    print 'Welcome to the game, Hangam!'
    finish = False
    while finish == False:
        finish = ifif()


hangman()
