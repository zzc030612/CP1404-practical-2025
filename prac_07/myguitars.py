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

    # Save all guitars back to the file
    save_guitars("guitars.csv", guitars)
    print("\nGuitars have been saved to the file.")


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list.")
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")