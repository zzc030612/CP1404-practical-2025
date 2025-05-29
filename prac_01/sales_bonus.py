"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

while sales >= 0:  # When the sales amount is non-negative, the loop continues
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15

    print(f"Your bonus is: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))  # Prompt the user to enter the sales amount again

print("Program finished.")  # When the user enters a negative number, the loop ends and the end information is printed