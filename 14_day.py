# Higher Lower Game
import random
from data_day_14 import data


def take_account():
    return random.choice(data)


def game():
    print("Welcome to Higher Lower Game")
    score = 0
    A = take_account()
    B = take_account()
    while score >= 0:
        print(f"\nCompare A: {A['name']}, a {A['description']}, from {A['country']}")
        print('VS')
        print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if A['follower_count'] > B['follower_count']:
            winner = "A"
        else:
            winner = "B"

        if guess == winner:
            score += 1
            print(f"\nCorrect, your score is {score}")
            A = B
            B = take_account()
        else:
            print(f"\nSorry, that's wrong. Final score: {score}")
            break


game()
