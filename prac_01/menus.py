# menus.py

def main():
    # Get the user's name
    name = input("Enter name: ")

    # Display menu
    display_menu()

    # Get user choices
    choice = input(">>> ").upper()

    # The menu loops until the user chooses to exit
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")

        # Display the menu again and get the choice
        display_menu()
        choice = input(">>> ").upper()

    # Exit message
    print("Finished.")


def display_menu():
    """显示菜单选项"""
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


# Call the main function
if __name__ == "__main__":
    main()