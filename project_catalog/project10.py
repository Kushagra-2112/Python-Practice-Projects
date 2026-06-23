# TITLE: Casino Blackjack Arcade Game
# DESCRIPTION: A functional card simulation engine implementing casino dealer rules, tracking dynamic hand valuations, and automated dealer execution loops.
# LIMITATIONS: Infinite Deck Tracking: The random selection matrix pulls cards with replacement, meaning the game mimics an infinite deck rather than tracking a standard 52-card exhaustion state. | Ace Valuation Limit: The system statically scores Aces as 11 points instead of dynamically down-grading them to 1 point if the player's score passes a value of 21.
# CHALLENGE: Modify the dynamic arithmetic scoring loop to scan for Aces and drop their value to 1 automatically if the total hand valuation breaks past 21 points to prevent an early bust!

import random

# Core card database values setup
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand_list):
    """Computes total score values for a given hand registry."""
    return sum(hand_list)

def deal_card():
    """Returns a completely randomized element value from the cards matrix."""
    return random.choice(cards)

print("♣️ ♦️ Welcome to Casino Blackjack! ♥️ ♠️")

user_hand = [deal_card(), deal_card()]
computer_hand = [deal_card(), deal_card()]

game_over = False

# --- PLAYER OPERATION LOOP ---
while not game_over:
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)
    
    print(f"\nYour Cards: {user_hand} -> Current Score: {user_score}")
    print(f"Dealer's First Card: {computer_hand[0]}")
    
    # Check immediate baseline boundary rule conditions
    if user_score == 21 or computer_score == 21 or user_score > 21:
        game_over = True
    else:
        user_choice = input("Type 'hit' to draw another card, or 'stand' to pass: ").strip().lower()
        if user_choice == "hit":
            user_hand.append(deal_card())
        else:
            game_over = True

# --- DEALER AUTOMATION LOOP (Dealer AI hits until score is 17+) ---
while computer_score < 17 and user_score <= 21:
    computer_hand.append(deal_card())
    computer_score = calculate_score(computer_hand)

# --- SCORE EVALUATION GRID ---
print(f"\n=== FINAL SCORES ===")
print(f"Your final hand: {user_hand} -> Final score: {user_score}")
print(f"Dealer final hand: {computer_hand} -> Dealer score: {computer_score}")

if user_score > 21:
    print("❌ You went over 21. You Bust! Dealer wins.")
elif computer_score > 21:
    print("🎉 Dealer went over 21. Dealer Busts! You Win!")
elif user_score == computer_score:
    print("🤝 It's a Draw (Push)!")
elif user_score > computer_score:
    print("🎉 You score higher than the dealer! You Win!")
else:
    print("❌ Dealer scores higher. You Lose!")