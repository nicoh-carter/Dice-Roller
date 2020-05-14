import random


print("This is a dice simulator\n")
userInput = "y"
while (userInput == "y"):
    roll = random.randint(1, 6)
    if (roll == 1):
        print("[-----------]\n|           |\n|     0     |\n|           |\n[-----------]\n")
    elif (roll == 2):
        print("[-----------]\n|           |\n|   0   0   |\n|           |\n[-----------]\n")
    elif (roll == 3):
        print("[-----------]\n|     0     |\n|     0     |\n|     0     |\n[-----------]\n")
    elif (roll == 4):
        print("[-----------]\n|   0   0   |\n|           |\n|   0   0   |\n[-----------]\n")
    elif (roll == 5):
        print("[-----------]\n|   0   0   |\n|     0     |\n|   0   0   |\n[-----------]\n")
    elif (roll == 6):
        print("[-----------]\n|   0   0   |\n|   0   0   |\n|   0   0   |\n[-----------]\n")
    print("Press y to roll again: ")
    userInput = input()

print("The program is terminating...")
