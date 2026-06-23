# TITLE: Procedural Stream Calculator
# DESCRIPTION: An operational tool featuring dedicated functional computing layers run inside an interactive continuous flow block.
# LIMITATIONS: Variable Evaluation Vulnerability: Entering character letter variables where digit data types are programmatically expected causes a termination error. | Static Input Setup: The platform forces the user to choose their operation option before asking for arguments every single execution turn, which prevents smooth string daisy-chaining operations (e.g., continuing to add numbers to the previous result).
# CHALLENGE: Restructure the system to track a continuous `current_total` state, allowing the user to perform new mathematical operations directly on the previous calculation's result without resetting.

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): 
    if b == 0:
        return "Zero Division Error"
    return a / b

while True:
    print("\n1-ADD, 2-Subtract, 3-Multiply, 4-Divide, 5-Exit")
    
    user_choice = int(input("Enter number from 1-5 for calculations: "))

    if user_choice == 5:
        print("Exiting calculator...")
        break 

    elif user_choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_choice == 1:
            print(f"Result: {add(num1, num2)}")

        elif user_choice == 2:
            print(f"Result: {subtract(num1, num2)}")

        elif user_choice == 3:
            print(f"Result: {multiply(num1, num2)}")

        elif user_choice == 4:
            print(f"Result: {divide(num1, num2)}")
            
    else:
        print("Invalid choice! Please select 1, 2, 3, 4, or 5.")