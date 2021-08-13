import os

parent_dir = os.path.dirname(__file__)
# print(parent_dir)
filepath = parent_dir + "/order.txt"
# filepath = parent_dir + "\wrong.txt"

try:
    with open(filepath, 'r') as file: # r = read mode
        data = file.read()
    print(data)
except FileNotFoundError as errmsg:
    print("ERROR")
    print(errmsg)
    data = []
    raise
except IndexError as errmsg:
    print("Other error")
    print(errmsg)
finally:
    print("Happens whether there is an error or not")


