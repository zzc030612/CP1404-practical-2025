from programming_language import ProgrammingLanguage

def main():
    """Test the ProgrammingLanguage class."""
    # Create ProgrammingLanguage objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print details of a single language
    print(python)

    # Create a list of programming languages
    languages = [python, ruby, visual_basic]

    # Find and print dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    main()