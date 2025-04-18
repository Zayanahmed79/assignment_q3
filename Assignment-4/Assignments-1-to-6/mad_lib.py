def main():
    print("Welcome to the Enhanced Mad Libs!")
    print("Fill in the blanks to create a fun and personalized story.")
    print("-" * 50)

    name = input("Enter a name: ")
    city = input("Enter a city: ")
    occupation = input("Enter an occupation: ")
    hobby = input("Enter a hobby: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    place = input("Enter a place: ")

    story = f"""
    Once upon a time in {city}, there lived a {adjective1} person named {name}.
    {name} was a {occupation} who loved {hobby} every weekend.
    One day, while {verb_ing} in the {place}, {name} stumbled upon a {adjective2} discovery that changed everything!
    """

    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == '__main__':
    main()