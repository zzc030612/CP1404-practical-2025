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

    # Display all guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

if __name__ == "__main__":
    main()