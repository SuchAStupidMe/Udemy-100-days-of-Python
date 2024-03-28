# NATO Phonetic Alphabet
import pandas as pd


nato_csv = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}
print(nato_dict)

while True:
    user_word = input('Type your word: ')
    try:
        print([nato_dict[letter.capitalize()] for letter in user_word])
    except KeyError:
        print('Sorry, only letters are allowed')
