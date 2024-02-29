# Hangman
from random import choice


word_list = ["aardvark", "baboon", "camel"]

chosen_word = choice(word_list)
split_word = [letter for letter in chosen_word]
display = ["_" for letter in range(len(chosen_word))]

lives = 3

while "_" in display:
    if lives == 0:
        print("Oops, you lost")
        break

    if "_" in display:
        guess = input("Guess the letter: ").lower()
        if guess in split_word:
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if guess == letter:
                    display[position] = letter
            print(' '.join(display))

        else:
            print("Oops, wrong letter")
            lives -= 1
            print(' '.join(display))

if "_" not in display:
    print("You win!")





