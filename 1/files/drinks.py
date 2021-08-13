import os

parent_dir = os.path.dirname(__file__)
filepath = parent_dir + "/drinks.txt"

def add_to_order(filepath, item):
    try:
        with open(filepath, 'a') as file:
            file.write(item + '\n')
    except FileNotFoundError:
        print("File not found")
        raise


def read_from_order(filepath, item):
    try:
        with open(filepath) as file:
            drinklist = file.readlines()
            clean_list = []
            for drink in drinklist:
                clean_list.append(drink.strip('\n'))
            if item in clean_list:
                print(item + ' is available')
            else:
                print(item + ' is not available')
    except FileNotFoundError as errmsg:
        print(errmsg)


# add_to_order(filepath, 'Martini')
read_from_order(filepath, 'Mojito')
read_from_order(filepath, 'Bottle')
read_from_order(filepath, 'Orange')
read_from_order(filepath, 'Orange juice')
read_from_order(filepath, 'Tea')