# Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


while True:
    choice_1 = input("left or right?\n")
    choice_1 = choice_1.lower()
    match choice_1:
        case "right":
            print("Game over")
            break
        case "left":
            pass

    choice_2 = input("There is a lake, do you want to swim or wait for the boat?\n")
    choice_2 = choice_2.lower()
    match choice_2:
        case "swim":
            print("Game over")
            break
        case "wait":
            pass

    print("You arrive to castle with 3 doors.")
    print("One door is red, one is blue and last one is yellow.")
    choice_3 = input("Which one do you choose?\n")
    choice_3 = choice_3.lower()

    match choice_3:
        case "red":
            print("Game over")
            break
        case "blue":
            print("Game over")
            break
        case "yellow":
            print("You win!")
            break

