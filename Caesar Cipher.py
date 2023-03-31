alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(txt, sft):
    encoded_text = ''
    for letter in txt:
        position = alphabet.index(letter)
        new_position = position + sft
        encoded_text += alphabet[new_position]
    print(encoded_text)


def decode(txt, sft):
    decoded_text = ''
    for letter in txt:
        position = alphabet.index(letter)
        new_position = position - sft
        decoded_text += alphabet[new_position]
    print(decoded_text)


if direction == "encode":
    encode(text, shift)
elif direction == "decode":
    decode(text, shift)
else:
    print("Sorry your choice is not understandable.")
