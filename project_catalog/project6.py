# TITLE: Dynamic Hangman Word Game
# DESCRIPTION: A word-guessing game that picks random secrets from a word bank array, tracking matches using index arrays and tracking incorrect states.
# LIMITATIONS: Lack of Life/Attempt Tracking: The game runs on an infinite guessing loop until the player wins, meaning the user can never lose. | Space/Character Crashes: If a hidden word containing spaces or numbers is ever added, guessing characters gets blocked.
# CHALLENGE: Create a `lives = 6` integer counter variable that decreases every time the user guesses a wrong letter, triggering a 'Game Over' when it hits 0.

import random 
print("Start")



words = ["Dragon","Action","Karma","Star","Sky"]
computer_generate = random.choice(words).strip().lower()
print(computer_generate) #Remove it while playing so it's inivisible

placeholder = []
for i in computer_generate:
    placeholder.append("_")

print(placeholder)


while "_" in placeholder:
    user_choose_letter = input("Enter the letter").strip().lower()

    guess_correct = False
    for index ,letter in enumerate(computer_generate):
        if letter == user_choose_letter:
            placeholder[index] = user_choose_letter
            guess_correct = True

    if not guess_correct:
        print("Wrong")

    print(placeholder)

print("You Won!!")
       
