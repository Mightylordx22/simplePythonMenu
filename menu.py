import sys
from functions import *
def menu ():
    while True:
        showOptions()
        userInput = input("Please select an option >> ").strip().upper()
        if userInput == "A":
            enterName()
        elif userInput == "B":
            enterInt()
        elif userInput == "C":
            userInt = enterValidInt()
            print(f"{userInt} is a nice number!\n")
        elif userInput == "D":
            intOperations()
        elif userInput == "X":
            sys.exit()
        else:
            print("Sorry that option is not valid!\n")