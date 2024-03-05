# Number Guessing Game
from random import randint


def game():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose between 'easy' or 'hard' difficulty.\n").lower()
    match difficulty:
        case "easy":
            attempts = 10
        case "hard":
            attempts = 5

    random_number: int = randint(1, 100)
    guess = 0

    while attempts != 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            break
        elif guess > random_number:
            print("Too high.")
            attempts -= 1
        elif guess < random_number:
            print("Too low.")
            attempts -= 1

        if attempts != 0:
            print("Guess again.")

    if attempts == 0 and guess != random_number:
        print("You weren't able to guess the number and run out of guesses.")
    elif attempts != 0:
        print("Congrats!You win!")


game()
