# TITLE: Rock Paper Scissors Simulation
# DESCRIPTION: An interactive game interface testing custom user inputs against computerized probabilistic choices using the Python random utility model.
# LIMITATIONS: Typing Vulnerability: If a player misspells a tool element (e.g., typing 'rockk'), the code silently falls through directly to the invalid input handler without giving a retry opportunity. | Repetitive Conditional Matrix: Writing explicit evaluations for all 9 game state variations creates highly verbose, repetitive logic.
# CHALLENGE: Reduce the 9 conditional state blocks down to a dynamic mathematical mapping array or nested collection evaluation structure to cleanly declare winners.

import random

tools = ["rock", "paper", "scissor"]

user = input("Enter rock, paper, or scissor: ").strip().lower()

computer = random.choice(tools)

print(f"You chose: {user}")
print(f"Computer chose: {computer}")

if computer == "rock" and user == "rock":
    print("Tie!")
elif computer == "rock" and user == "scissor":
    print("Computer wins!")
elif computer == "rock" and user == "paper":
    print("User wins!")

elif computer == "paper" and user == "rock":
    print("Computer wins!")
elif computer == "paper" and user == "scissor":
    print("User wins!")
elif computer == "paper" and user == "paper":
    print("Tie!")

elif computer == "scissor" and user == "rock":
    print("User wins!")
elif computer == "scissor" and user == "scissor":
    print("Tie!")
elif computer == "scissor" and user == "paper":
    print("Computer wins!")

else:
    print("Invalid input! Please check your spelling.")