"""
CP1404/CP5632 Practical
Taxi simulator program
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator program."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100, 1.23),  # Provide the price_per_km parameter
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    while True:
        print("\nq)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")


def display_taxis(taxis):
    """Display the list of available taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Allow the user to choose a taxi."""
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input; please enter a number")
    return None


def drive_taxi(taxi):
    """Drive the chosen taxi and return the trip cost."""
    try:
        distance = float(input("Drive how far? "))
        taxi.start_fare()
        taxi.drive(distance)
        trip_cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
        return trip_cost
    except ValueError:
        print("Invalid input; please enter a number")
        return 0.0


if __name__ == "__main__":
    main()