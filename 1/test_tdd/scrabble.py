import random
import string

# initialise with string of 7 letters
# method to check submitted word can be made from tiles
# a method to return score
# a method to use methods above to check if word is valid
# if it is, return score for that word

class Scrabble():
    def __init__(self):
        self.get_rnd_string()

    def check_word(self):
        word = input("Check word: ")

    def get_rnd_string(self, tiles=7):
        self.tiles = tiles
        rnd_string = ''
        for a in range(tiles):
            rnd_string += random.choice(string.ascii_uppercase)
        # print(rnd_string)
        print(rnd_string)
        return rnd_string

    def return_score(self, word):
        self.word = word
        total_score = 0
        score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}
        for letter in word:
            for scores in score.keys():
                if scores == letter:
                    total_score += score[scores]
        print(total_score)
        return total_score


    def check_if_valid(self):
        print()

s = Scrabble()