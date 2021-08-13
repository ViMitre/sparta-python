import random
import string
import enchant


# initialise with string of 7 letters
# method to check submitted word can be made from tiles
# a method to return score
# a method to use methods above to check if word is valid
# if it is, return score for that word

class Scrabble():
    def __init__(self, tiles):
        self.get_rnd_string(tiles)

    def check_word(self, tiles_lst):
        word = input("Check word: ").upper()
        checked_word = ''
        for letter in word:
            if letter not in tiles_lst:
                checked_word = ''
                break
            else:
                tiles_lst.remove(letter)
                checked_word = word
        self.return_score(checked_word)

    def get_rnd_string(self, tiles):
        self.tiles = tiles
        tiles_lst = []
        for a in range(tiles):
            tiles_lst.append(random.choice(string.ascii_uppercase))
        print(tiles_lst)
        self.check_word(tiles_lst)
        return tiles_lst

    def return_score(self, word):
        total_score = 0
        score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                 "x": 8, "z": 10}
        for letter in word:
            total_score += score[letter.lower()]
        print(total_score)
        return total_score

    def check_if_valid(self, word):
        d = enchant.Dict("en_US")
        d.check(word)
        pass


s = Scrabble(10)
