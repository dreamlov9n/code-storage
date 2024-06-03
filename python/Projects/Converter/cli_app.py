#fun fact: i made the gui version first. and yes i could make a bash version but i suck at bash
#----------------------------------------
print("Welcome to converter! Convert your funny stuff here.")
#----------------------------------------
entry=float(input("Type in your number: "))
#----------------------------------------
print("Convert type? For example:")
print("mm -> cm ; cm -> m ; m -> km ; km -> cm ; mm -> mm")
ChosenItem = str(input("Your choice : "))

print("Proceeding with calculation..\n")
enteredNum = float(entry)

# mm
if ChosenItem == "mm -> mm":
    print("Output: " + str(enteredNum) + "mm")

if ChosenItem == "mm -> cm":
    print("Output: " + str(enteredNum / 10) + "cm")

if ChosenItem == "mm -> m":
    print("Output: " + str(enteredNum / 1000) + "m")

if ChosenItem == "mm -> km":
    print("Output: " + str(enteredNum / 1000000) + "km")

#cm
if ChosenItem == "cm -> mm":
    print("Output: " + str(enteredNum * 10) + "mm")

if ChosenItem == "cm -> cm":
    print("Output: " + str(enteredNum) + "cm")

if ChosenItem == "cm -> m":
    print("Output: " + str(enteredNum / 100) + "m")

if ChosenItem == "cm -> km":
    print("Output: " + str(enteredNum / 100000) + "km")

#m
if ChosenItem == "m -> mm":
    print("Output: " + str(enteredNum * 1000) + "mm")

if ChosenItem == "m -> cm":
    print("Output: " + str(enteredNum * 10) + "cm")

if ChosenItem == "m -> m":
    print("Output: " + str(enteredNum) + "m")

if ChosenItem == "m -> km":
    print("Output: " + str(enteredNum / 1000) + "km")

#km
if ChosenItem == "km -> mm":
    print("Output: " + str(enteredNum * 1000000) + "mm")

if ChosenItem == "km -> cm":
    print("Output: " + str(enteredNum * 100000) + "cm")

if ChosenItem == "km -> m":
    print("Output: " + str(enteredNum * 1000) + "m")

if ChosenItem == "km -> km":
    print("Output: " + str(enteredNum) + "km")


