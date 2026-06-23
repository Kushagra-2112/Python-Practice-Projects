# TITLE: Treasure Island Text Adventure
# DESCRIPTION: A branching terminal choice engine using highly nested conditional statements to direct players through a classic choose-your-own-adventure logic tree.
# LIMITATIONS: Infinite Loop Trap: The structure uses an infinite while loop that requires explicit `break` triggers inside every leaf, leaving room for logic leaks if a new branch is added. | Deep Nesting Complexity: The structural design relies heavily on deeply nested `if-elif` statements, which degrades code maintainability as the game map expands.
# CHALLENGE: Restructure the decision maze logic by mapping choices to step functions, reducing nested depth and eliminating the need for a perpetual loop layout.

print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")

while True:
    direction = input("Enter Left or Right: ").strip().lower()

    if direction == "right":
        print("Fall into a hole, Game Over!")
        break 

    elif direction == "left":
        print("Nice Move! You made it safely across.")

        choice = input("Enter swim or wait").strip().lower()

        if choice == "swim":
            print("Attacked by a trout, Game Over")
            break
        elif choice == "wait":
            print("Nice move again, Awesome you are playing")

            door = input("Which door Red/Blue/Yellow").strip().lower()

            if door == "red":
                print("Oops!! Burning , Burned by fire")
                break
            elif door == "blue":
                print("Oops!! Eaten by beasts")
                break
            elif door == "yellow":
                print("you win")
                break
            else:
                print("Damn!! Game Over")
                break
        else:
            print("You stood around too long. Game Over!")
            break

           
    else:
        print("Invalid input! Please type 'Left' or 'Right'.\n")