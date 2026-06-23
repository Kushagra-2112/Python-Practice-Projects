# TITLE: Dynamic Tip Calculator
# DESCRIPTION: A financial utility script that computes individual bill splits including floating-point tax and custom tip tier distribution percentages.
# LIMITATIONS: String Formatting Fallback: Relying purely on string format blocks (`{:.2f}`) instead of rounding math functions can complicate nested variable arithmetic down the line. | Critical Input Value Crash: Entering text values or non-digit expressions when prompted for the dollar bill size triggers a system crash.
# CHALLENGE: Implement exception validation loops (`try-except`) around inputs to ensure a user typing a literal character string like 'ten dollars' doesn't break the application runtime.

print("Welcome to the Tip Calculator!")


total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? (e.g., 10, 12, 15, 20): "))
people_count = int(input("How many people are splitting the bill? "))

tip_amount = total_bill * (tip_percentage / 100)
final_bill = total_bill + tip_amount
amount_per_person = final_bill / people_count


final_amount = "{:.2f}".format(amount_per_person)

print(f"\nEach person should pay: ${final_amount}")