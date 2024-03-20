# NATO Phonetic Alphabet
import pandas as pd


nato_csv = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}
print(nato_dict)

user_word = input('Type your word: ')
print([nato_dict[letter.capitalize()] for letter in user_word])
