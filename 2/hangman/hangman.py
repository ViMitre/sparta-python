import random
from wordlist import word_list
from hangman_ascii import *
import time

# prompt = True
print("----------==========>>>>>>>>>>HANGMAN V1.2.54353453.546653612452<<<<<<<<<<==========----------")
print("Loading, please wait...")
# for p in range(101):
#     print('\r{}%'.format(p), end='')
#     time.sleep(0.02)
print("\nWelcome to Hangman!")


def select_word():
    return random.choice(word_list)


def check_char(char, word):
    lst = []
    y = 0
    for x in word:
        if x == char:
            lst.append(y)
        y += 1
    return lst


def reveal(hidden_word, char, lst):
    for x in lst:
        hidden_word = hidden_word[:x] + char + hidden_word[x + 1:]
    # print(hidden_word)
    return hidden_word


def strike(num):
    num = str(num)
    with open("hangman_ascii/hangman_ascii_" + num + ".txt") as f:
        print(f.read())




game = True
word = select_word()
print(word)
hidden_word = "_" * len(word)
used_letters = []
strikes = 10

while game:
    # print(hidden_word)
    strike(strikes)
    print(hidden_word)
    letter = input("Letter: ").upper()
    if letter in word and letter not in used_letters:
        hidden_word = reveal(hidden_word, letter, check_char(letter, word))
        used_letters.append(letter)
    elif letter not in word:# and letter not in used_letters:
        used_letters.append(letter)
        strikes -= 1
        if strikes == 0:
            strike(strikes)
            select = input("You got hanged! Do you want to play again? [y/n]")
            if select.lower() == "y":
                word = select_word()
                hidden_word = "_" * len(word)
                used_letters = []
                strikes = 10
            elif select.lower() == "n":
                print("Thanks for playing!")
                game = False
            else:
                print("Please select yes/no [y/n]")

    # print(hidden_word)
    if "_" not in hidden_word:
        game = False
        print("Congrats")

