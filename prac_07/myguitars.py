"""
Program to manage a list of guitars using the Guitar class.
"""

from guitar import Guitar


def main():
    """Main function to manage guitars."""
    guitars = load_guitars("guitars.csv")
    print("These are the guitars currently in the file:")
    display_guitars(guitars)

    # Sort guitars by year and display them
    guitars.sort()
    print("\nThese are the guitars sorted by year:")
    display_guitars(guitars)

    # Add new guitars
    print("\nAdd new guitars (leave name blank to stop):")
    while True:
        name = input("Name: ")
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Please enter valid data.")