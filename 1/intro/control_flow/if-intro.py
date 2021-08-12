prompt = True
while prompt:
    age = input("Age: ")
    if age.isdigit():
        if 0 < int(age) < 120:
            age = int(age)
            prompt = False
        else:
            print("Please enter a valid age")
    else:
        print("Please enter a valid number")

prompt = True

while prompt:
    try:
        film = str.upper(input("Film cert (U, PG, 12, 15, 18: "))
        if film not in ["U", "PG", "12", "15", "18"]:
            print("Please enter a valid film cert")
            continue
        else:
            break
    except ValueError:
        print("Sorry")


if 15 <= age < 18:
    if film == "PG":
        print("You can watch it")
    elif film == "12":
        print("You can watch it")
    elif film == "15":
        print("You can watch it")
    elif film == "18":
        print("You can't watch it")
    else:
        print("You can watch it")
elif 12 <= age < 15:
    if film == "PG":
        print("Ask your parents")
    elif film == "12":
        print("You can watch it")
    elif film == "15":
        print("You can't watch it")
    elif film == "18":
        print("You can't watch it")
    else:
        print("You can watch it")
elif age < 12:
    if film == "PG":
        print("Ask your parents")
    elif film == "12":
        print("You can't watch it")
    elif film == "15":
        print("You can't watch it")
    elif film == "18":
        print("You can't watch it")
    else:
        print("You can watch it")
else:
    print("You can watch it")

