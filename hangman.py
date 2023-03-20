from english_words import get_english_words_set
import random

def easy_words():
    data = open("1-1000.txt","r").read().split()
    return list(data[random.randint(0,len(data)-1)])
    """
    It opens the file, reads it, splits it into a list, and then returns a random word from that list
    :return: A list of random words from the file.
    """


def all_words():
    web2lowerset = get_english_words_set(['web2'], lower=True)
    data = list(web2lowerset)
    return list(data[random.randint(0,len(data)-1)])
    """
    It takes a list of words from the web2 dictionary, converts them to lowercase, and returns a random
    word from the list
    :return: A random word from the web2lowerset
    """



def difficulty():
    x = int(input("Choose your difficulty: Easy[1] Normal[2] Hard[3] :   "))
    if x == 1:
        return 10
    elif x == 2:
        return 7
    elif x == 3:
        return 5
    else:
        print ("Enter a number from 1 to 3")
        difficulty()
    """
    It asks the user to choose a difficulty level, and returns the number of guesses they get based on
    their choice.
    :return: The number of guesses the user has.
    """



def startoverlay(word):
    lst = []
    for i in word:
        lst.append("_")
    return lst
    """
    It takes a word and returns a list of underscores the same length as the word
    
    :param word: The word that the user is trying to guess
    :return: A list of underscores the same length as the word.
    """


def game(word,lives,shown):
    checker = 0
    print (("".join(shown)) + "        remaining lives " + str(lives))
    guess = input("Enter your Guess: ")
    if guess == ("".join(word)):
        print("YOU WON")
        again()
    else:
        for nr, i in enumerate(word):
            if i == guess:
                shown[nr] = i
                checker += 1
        
        if checker > 0:
            if word == shown:
                print("YOU WON")
                again()
            else:
                game(word,lives,shown)
        else:
            lives -= 1
            if lives == 0:
                print("you lost the word you were looking for was: " + ("".join(word)))
                again()
            else:    
                game(word,lives,shown)
    """
    It takes a word, the number of lives, and a list of underscores as input, and then it prints the
    word with underscores, asks the user to guess a letter, and then it checks if the letter is in the
    word, and if it is, it replaces the underscores with the letter, and if it isn't, it subtracts a
    life
    
    :param word: the word to be guessed
    :param lives: the number of lives the player has
    :param shown: the word with the letters that have been guessed
    """


def again():
    again = input("do you want to play again?(y/n)\n")
    if again == "y":
        startgame()
    elif again == "n":
        print("thank you for playing")
    else:
        print("please enter 'y' if you want to play again or 'n' if you dont want to play another game: ")
    """
    If the user enters 'y' then the game will start again, if the user enters 'n' then the game will
    end, if the user enters anything else then the user will be asked to enter 'y' or 'n' again.
    """



def startgame():
    words = input("do you want to play with common english words[1] or do you want to play with all english words[2]: ")
    if words == "1":
        word = easy_words()
    elif words == "2":
        word = all_words()
    else: print("please enter a number: 1 for common words, 2 for all words")
    game(word,difficulty(),startoverlay(word))
    """
    It asks the user if they want to play with common words or all words, then it asks them what
    difficulty they want to play on, then it starts the game.
    """
    

startgame()