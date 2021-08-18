import json

first_pet = {
    "name": "Rupert",
    "animal": "Goldfish"
}

# print(first_pet, type(first_pet))
#
# first_pet_string = json.dumps(first_pet)
#
# print(first_pet_string, type(first_pet_string))
#
# with open('first_pet_file.json', 'w') as jsonfile:
#     json.dump(first_pet, jsonfile)

with open("new_animal.json", 'r') as jsonfile:
    monstrosity = json.load(jsonfile)

print(monstrosity, type(monstrosity))
print(monstrosity["sound"])

json_string = '{"name": "Viktor", "Age": 29}'
json_dict = json.loads(json_string)

print(json_dict, type(json_dict))