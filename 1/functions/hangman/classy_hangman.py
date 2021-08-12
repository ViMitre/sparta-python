import random
from termcolor import colored
from wordlist import word_list
from hangman_ascii import *
import time

print(colored("----------==========>>>>>>>>>>HANGMAN V1.2.54.353453546653612452<<<<<<<<<<==========----------", "blue"))
print("Loading, please wait...")
for p in range(101):
    print('\r{}%'.format(p), end='')
    # time.sleep(0.02)
print("\nWelcome to Hangman!")


class Hangman:
    def __init__(self, used_letters=[], strikes=10):
        self.word = self.select_word()
        self.used_letters = used_letters
        self.strikes = strikes


    def select_word(self):
        return random.choice(word_list)

    def check_char(self, char, word):
        lst = []
        y = 0
        for x in word:
            if x == char:
                lst.append(y)
            y += 1
        return lst

    def reveal(self, hidden_word, char, lst):
        for x in lst:
            hidden_word = hidden_word[:x] + char + hidden_word[x + 1:]
        return hidden_word

    def strike(self, num):
        num = str(num)
        with open("hangman_ascii/hangman_ascii_" + num + ".txt") as f:
            print(f.read())
            print()


word = "asdfqwer"
game = Hangman(word, "_" * len(word), [], 10)
print(game.hidden_word)
