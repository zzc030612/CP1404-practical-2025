"""
Program to manage a collection of guitars.

Estimated time: 25 minutes
Actual time: 20 minutes
"""

from guitar import Guitar

def main():
    """Manage a collection of guitars."""
    guitars = []

    print("My guitars!")
    while True:
        name = input("Name: ")
        if not name:  # Exit when name is blank
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")