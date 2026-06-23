# TITLE: PyPassword Generator Engine
# DESCRIPTION: A randomized cryptographic token creator that aggregates array elements across variant safe schemas (characters, symbols, and integers) before applying an in-place structural shuffle.
# LIMITATIONS: Index Array Bounds Errors: If a user specifies a target length of 0 across all characters, the script runs successfully but produces an empty, highly insecure null output string. | Weak Randomization Entropy: The system uses standard pseudo-random number generation modules (`random`), which are not cryptographically secure for real-world application deployments.
# CHALLENGE: Integrate a verification rule checking that the requested password configuration contains at least 8 characters, or transition the compilation sequence from `random` to the production-grade `secrets` module.


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?")) 
nr_symbols = int(input(f"How many symbols would you like?"))
nr_numbers = int(input(f"How many numbers would you like?"))

password_list = []

for i in range(nr_letters):
    password_list.append(random.choice(letters))

for i in range(nr_symbols):
    password_list.append(random.choice(symbols))

for i in range(nr_numbers):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your secure password is: {password}")
