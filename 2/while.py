# x = 1
#
# while x < 10:
#     print(f"x is currently {x}")
#     if x == 4:
#         break
#     x += 1

prompt = True

while prompt:
    age = input("Age: ")
    if age.isdigit():
        if int(age) < 120:
            age = int(age)
            prompt = False
        else:
            print("")
    else:
        print("Please provide age with numbers")
