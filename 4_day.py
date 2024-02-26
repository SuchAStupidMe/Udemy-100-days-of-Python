# Rock, Paper, Scissors
from random import randint


game = {
    0: "Rock",
    1: "Paper",
    2: "Scissors",
    3: "Rock",
    4: "Paper",
    5: "Scissors"
}

user_choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

computer_choice = randint(0, 2)
print(f"Computer chose {game[computer_choice]}")

if computer_choice == user_choice:
    print("It's a draw!")

elif game[computer_choice + 1] == game[user_choice]:
    print("You win")

elif game[computer_choice + 2] == game[user_choice]:
    print("Computer wins!")



