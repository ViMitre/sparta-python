import time

prompt = True
print("----------==========>>>>>>>>>>FIZZBUZZ V1.2.54353453.546653612452<<<<<<<<<<==========----------")
print("Loading, please wait...")
for p in range(101):
    print('\r{}%'.format(p), end='')
    time.sleep(0.02)
print("\nWelcome to FIZZBUZZ!\n -Select the maximum number")
while prompt:
    max = input("Max number: ")
    if max.isdigit():
        max = int(max)
        if max > 0:
            prompt = False
        else:
            print("Please enter a positive number")
    else:
        print("Please enter a valid number")

select = input("Would you like to select FIZZ/FUZZ numbers? [y/n]")
if select.lower() == "y":
    prompt = True
    while prompt:
        fizz = input("FIZZ number: ")
        if fizz.isdigit():
            fizz = int(fizz)
            if fizz > 0:
                prompt = False
            else:
                print("Please enter a positive number")
        else:
            print("Please enter a valid number")

    prompt = True
    while prompt:
        buzz = input("BUZZ number: ")
        if buzz.isdigit():
            buzz = int(buzz)
            if buzz > 0:
                prompt = False
            else:
                print("Please enter a positive number")
        else:
            print("Please enter a valid number")
elif select.lower() == 'n':
    fizz = 3
    buzz = 5
else:
    print("Please select y/n")
for i in range(1, max + 1):
    if i % fizz == 0 and i % buzz == 0:
        print("FIZZBUZZ")
    elif i % fizz == 0:
        print("FIZZ")
    elif i % buzz == 0:
        print("BUZZ")
    else:
        print(i)

