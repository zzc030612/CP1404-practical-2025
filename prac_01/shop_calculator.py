"""
Program to calculate the total price for a number of items, applying a discount if the total is over $100.
"""


def main():
    # Input validation: Ensure that the quantity of goods is a non-negative integer
    num_items = int(input("Number of items: "))
    while num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))

    # Initialize the total price
    total_price = 0

    # Input the price of each commodity in a loop
    for i in range(num_items):
        price = float(input("Price of item: "))
        total_price += price

    # If the total price exceeds 100 US dollars, apply a 10% discount
    if total_price > 100:
        total_price *= 0.9

    # Output the total price and format it to two decimal places
    print(f"Total price for {num_items} items is ${total_price:.2f}")


# Call the main function
if __name__ == "__main__":
    main()