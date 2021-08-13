import os

parent_dir = os.path.dirname(__file__)
# print(parent_dir)
filepath = parent_dir + "/order.txt"
file = open(filepath)

# data = file.read()
# print(data, type(data))
#
# data = file.read()
# print(data, type(data))

# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)
# data = file.readline()
# print(data)

data = file.readlines()
print(data)

line_1 = data[0].strip('\n')
line_2 = data[1].strip('\n')
line_3 = data[2].strip('\n')

print(line_1)
print(line_2)
print(line_3)

clean_data = []

for entry in data:
    clean_data.append(entry.strip('\n'))

print(clean_data)

data = [order.strip('\n') for order in data]

print(data)

data = list(map(lambda x: x.strip('\n'), file.readlines()))
print(data)


file.close()

with open(filepath) as file:
    data = list(map(lambda x: x.strip('\n'), file.readlines()))
    print(data)