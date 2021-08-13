import os

parent_dir = os.path.dirname(__file__)
filepath = parent_dir + "/order.txt"


def add_to_order(filepath, item):
    try:
        with open(filepath, 'a') as file:
            file.write(item + '\n')
    except FileNotFoundError:
        print("File not found")
        raise

def write_to_order(filepath, item):
    try:
        with open(filepath, 'w') as file:
            file.write(item + '\n')
    except FileNotFoundError:
        print("File not found")
        raise

# add_to_order(filepath, 'Eggs on toast')
# add_to_order(filepath, 'Quich')
write_to_order('Zeeshan', 'Eggs on toast')
write_to_order('Sacha', 'Quich')

# '''
# Read from a drinks_order.txt
# Check if items are available in the txt
# '''