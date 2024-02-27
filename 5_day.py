# Password Generator
import random
import string


print("PyPassword Generator")
all_letters = list(string.ascii_letters)
letters = int(input("How many letters would you like in your password?\n"))

all_symbols = list("$%#@!%^&$%#@!%^&$%#@!%^&$%#@!%^&$%#@!%^&$%#@!%^&")  #
symbols = int(input("How many symbols would you like?\n"))

all_numbers = list(string.digits)
numbers = int(input("How many numbers would you like?\n"))

# Generate password
password = []
if letters != 0:
    rand_letters = random.sample(all_letters, letters)
    password.append(rand_letters)
if symbols != 0:
    rand_symbols = random.sample(all_symbols, symbols)
    password.append(rand_symbols)
if numbers != 0:
    rand_numbers = random.sample(all_numbers, numbers)
    password.append(rand_numbers)

# Shuffle password
password = [item for sublist in password for item in sublist]
random.shuffle(password)

print("There is your password!")
print(''.join(password))



