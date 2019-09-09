import math

def enterName():
    userName = input("Enter your name: ").strip()
    print(f"Oh hi there {userName}!\n")

def enterInt():
    integer = input("Please enter an integer: ")
    print(f"{int(math.floor(float(integer)))} is a nice number!\n")

def enterValidInt():
    while True:
        try:
            userInt = int(input("Enter an integer: "))
            if userInt < 0:
                print("Sorry that is less than 0")
            else:
                break;
        except:
            print("Sorry that is not an integer")
    return userInt

def intOperations():
    intOne = enterValidInt()
    intTwo = enterValidInt()
    answer = None
    while answer is None:
        showOperations()
        userChoice = input("What choice would you like >> ").strip().upper()
        if userChoice == "A":
            answer = intOne+intTwo
        elif userChoice == "B":
            answer = intOne-intTwo
        elif userChoice == "C":
            answer = intOne*intTwo
        elif userChoice == "D":
            answer = intOne/intTwo
        elif userChoice == "E":
            answer = intOne%intTwo
        elif userChoice == "F":
            answer = intOne//intTwo
        else:
            print("Sorry that option is not valid!\n")
        print(f"Here is your answer {answer}")

def showOperations():
    print("A] Add {+}")
    print("B] Subtract {-}")
    print("C] Multiply {*}")
    print("D] Divide {/}")
    print("E] Modulo {%}")
    print("F] Integer Division {//}")

def showOptions():
    print("A] Enter name")
    print("B] Enter int")
    print("C] Enter valid tnt")
    print("D] Operate two valid integers")
    print("X] Exit")