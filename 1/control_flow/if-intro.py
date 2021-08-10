while True:
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Please enter a valid number")
    if age < 0:
        print("Please enter a valid number")
        continue
    else:
        break

while True:
    try:
        film = str.upper(input("Film cert (U, PG, 12, 15, 18: "))
        if film not in ["U", "PG", "12", "15", "18"]:
            print("Please enter a valid film cert")
            continue
        else:
            break
    except ValueError:
        print("Sorry")


if age >= 15 and age < 18:
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
elif age >= 12 and age < 15:
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

