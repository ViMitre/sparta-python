sre = ["Sacha", "Viktor", "Amy"]

print(sre[1])
sre.append("Zeeshan")
print(sre)
sre.append("Viktor")
print(sre)
an_item = sre.pop(3)
print(f"{an_item} was removed")
print(sre)

print(sre.count("Viktor"))
print(sre.index("Viktor"))

sre.sort()
print(sre)

# Tuples

essentials = ("bread", "milk", "chocolate", "cheese")
print(essentials)
