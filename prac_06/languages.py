from programming_language import ProgrammingLanguage

def main():
    """Test the ProgrammingLanguage class."""
    # Create ProgrammingLanguage objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print details of a single language
    print(python)


if __name__ == "__main__":
    main()