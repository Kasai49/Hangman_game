from english_words import get_english_words_set
import random

def easy_words():
    data = open("1-1000.txt","r").read().split()
    return list(data[random.randint(0,len(data)-1)])

def all_words():
    web2lowerset = get_english_words_set(['web2'], lower=True)
    data = list(web2lowerset)
    return list(data[random.randint(0,len(data)-1)])

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

def startoverlay(word):
    lst = []
    for i in word:
        lst.append("_")
    return lst


def game(word,lives,shown):
    checker = 0
    print ("".join(shown) + "        remaining lives " + str(lives))
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
                print("you lost")
                again()
            else:    
                game(word,lives,shown)

def again():
    again = input("do you want to play again?(y/n)\n")
    if again == "y":
        startgame()
    elif again == "n":
        print("thank you for playing")
    else:
        print("please enter 'y' if you want to play again or 'n' if you dont want to play another game: ")

def startgame():
    words = input("do you want to play with common english words[1] or do you want to play with all english words[2]: ")
    if words == "1":
        word = easy_words()
    elif words == "2":
        word = all_words()
    else: print("please enter a number: 1 for common words, 2 for all words")
    print("".join(word))
    game(word,difficulty(),startoverlay(word))
    


startgame()
    