# Mail Merging
PLACEHOLDER = '[name]'

with open('./Input/Letters/starting_letter.txt', 'r') as file:
    starting_letter = file.read()

with open('./Input/Names/invited_names.txt', 'r') as file:
    names = [name.strip() for name in file.readlines()]


for name in names:
    ready_to_send = starting_letter.replace(PLACEHOLDER, name)
    with open(f'./Output/ReadyToSend/letter_for_{name}', 'w') as file:
        file.write(ready_to_send)
