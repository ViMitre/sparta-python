import random
from termcolor import colored
from wordlist import word_list
from hangman_ascii import *
import time

print(colored("----------==========>>>>>>>>>>HANGMAN V1.2.54.353453546653612452<<<<<<<<<<==========----------", "blue"))
print("Loading, please wait...")
for p in range(101):
    print('\r{}%'.format(p), end='')
    time.sleep(0.02)
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
    return hidden_word


def strike(num):
    num = str(num)
    with open("hangman_ascii/hangman_ascii_" + num + ".txt") as f:
        print(f.read())
        print()


game = True
word = select_word()
hidden_word = "_" * len(word)
used_letters = []
strikes = 10


def start(*multiargs):
    if game:
        global word
        word = select_word()
        global hidden_word
        hidden_word = "_" * len(word)
        global used_letters
        used_letters = []
        global strikes
        strikes = 10


start(select_word(), "_" * len(word), [], 10)

while game:
    prompt = True
    strike(strikes)
    print(colored(hidden_word, 'cyan'))
    if used_letters:
        print(colored("Used letters: " + str(used_letters)[1:-1], 'yellow'))
    while prompt:
        letter = input("Letter: ").upper()
        if letter.isalpha() and len(letter) == 1:
            prompt = False
        else:
            print("Please enter a single letter")
    if letter in word and letter not in used_letters:
        hidden_word = reveal(hidden_word, letter, check_char(letter, word))
        used_letters.append(letter)
        used_letters.sort()
    elif letter not in word:  # and letter not in used_letters:
        used_letters.append(letter)
        strikes -= 1
        if strikes == 0:
            strike(strikes)
            print(colored("HANG IN THERE...", 'red'))
            print("The word was " + word)
            select = input("Do you want to play again? [y/n]")
            if select.lower() == "y":
                start(select_word(), "_" * len(word), [], 10)
            else:
                print("Thanks for playing!")
                game = False

    if "_" not in hidden_word:
        print(colored(hidden_word, 'green'))
        print(colored("Congratulations!", 'green'))
        select = input("Do you want to play again? [y/n]")
        if select.lower() == "y":
            start(select_word(), "_" * len(word), [], 10)
        else:
            print("Thanks for playing!")
            game = False
