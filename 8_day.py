# Caesar Cypher
def encode(text, shift):
    encoded_text = []
    for letter in text:
        shifted_letter = alphabet[alphabet.index(letter) + shift]
        encoded_text.append(shifted_letter)
    return ''.join(encoded_text)


def decode(text, shift):
    decoded_text = []
    for letter in text:
        shifted_letter = alphabet[alphabet.index(letter) - shift]
        decoded_text.append(shifted_letter)
    return ''.join(decoded_text)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


while True:
    action = input("Do you want to encode(0) or decode(1) text?: ")
    text = list(input("Type your text: "))
    shift = int(input("Choose the shift: "))
    if action == '0':
        print(f"Your encoded text is {encode(text, shift)}")
    elif action == '1':
        print(f"Your decoded text is {decode(text, shift)}")
