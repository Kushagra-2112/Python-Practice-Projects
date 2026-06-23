# TITLE: Caesar Cipher Encryptor Engine
# DESCRIPTION: A programmatic cryptographic function that applies positional text rotation mathematics against a defined alphabetical array list.
# LIMITATIONS: Space Elimination Flaw: Passing string arguments containing multi-word spacing, numerical codes, or special symbols triggers index position errors because they aren't tracked inside your alphabet array structure. | Redundant Global References: The structure uses globally defined scope inputs right inside inner computational logic layers rather than maintaining pure procedural functions.
# CHALLENGE: Restructure the computational loop to look for symbols or spaces, skipping positional index modifications if an unfamiliar character is encountered, so it outputs symbols safely without breaking.

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Enter encrypt or decrypt").strip().lower()
original_text = input("Enter text").lower()
shift = int(input("Enter shifting no"))


def ceasar_cipher(original_text,shift,direction):

    if direction == "encrypt":
        cipher_text = "" 

        for letter in original_text:
            shifted_positon = alphabets.index(letter) + shift
            shifted_positon = shifted_positon % len(alphabets)
            cipher_text += alphabets[shifted_positon]

        print(f"Here is enrypted result: {cipher_text}")
     

    if direction == "decrypt":
        cipher_text = "" 

        for letter in original_text:
            shifted_positon = alphabets.index(letter) - shift
            shifted_positon = shifted_positon % len(alphabets)
            cipher_text += alphabets[shifted_positon]

        print(f"Here is decrypted result: {cipher_text}")

print(f"original_text was {original_text}")
ceasar_cipher(original_text, shift, direction)



