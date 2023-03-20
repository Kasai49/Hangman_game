from english_words import get_english_words_set
import random

def get_random_english_word():
    web2lowerset = get_english_words_set(['web2'], lower=True)
    data = list(web2lowerset)
    return list(data[random.randint(0,len(data)-1)])

def difficulty():
    x = input("Choose your difficulty: Easy[1] Normal[2] Hard[3] :   ")
    if x == 1:
        return 10
    elif x == 2:
        return 7
    elif x == 3:
        return 5

def startoverlay(word,lives):
    string = ""
    for i in word:
        string = string +"_ "
    print (string + "        remaining lives " + str(lives))


startoverlay(get_random_english_word(),difficulty())



    