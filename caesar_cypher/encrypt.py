# encrypt process
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text,shift_amount):
    cypher_text = ""
    for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            # this makes sure that we are always in the range of list
            shifted_position = shifted_position % len(alphabet)
            cypher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cypher_text}")

encrypt(text,shift)



