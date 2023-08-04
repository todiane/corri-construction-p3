print("Welcome to the Corri Construction Company Contractors Page.")
print("Please input your first and last name to begin\n")

"""
instructions to add first and last name\n
"""
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
print("Hello: " + first_name + " " + last_name)

"""
instructions to confirm their profession

"""
print("What is your job role " + first_name + "?")


def get_profession_choice():
    # Dictionary to map profession codes to profession names
    professions = {
        "a": {"name": "Bricklayer", "rate": 25.85},
        "b": {"name": "Plumber", "rate": 36.52},
        "c": {"name": "Scaffolder", "rate": 22.95},
        "d": {"name": "Electrician", "rate": 36.52},
        "e": {"name": "Carpenter", "rate": 25.85},
        "f": {"name": "Construction Worker", "rate": 22.95}
    }

    while True:
        # Display available professions to the user
        print("Choose a profession:\n")
        for key, profession in professions.items():
            print(f"{key}: {profession['name']}")

        # Prompt the user to enter the letter corresponding to their choice
        choice = input("Enter valid letter for your profession: ").lower()

        """
        Validate the users input and confirm their choice
        """
        if choice in professions:
            confirm = input(f"You chose {professions[choice]['name']}. Is this correct? (y/n): ").lower()
            if confirm == "y":
                return professions[choice]
        else:
            print("Invalid choice. Please choose a valid option.")

"""
if yes print out the details including random user number and hourly pay
"""

if __name__ == "__main__":
    chosen_profession = get_profession_choice()
    import random
    print(first_name + " " + "your contractor number is " + str(random.randint(23203, 63944)))
    print(f"Your profession is: {chosen_profession['name']}")
    print(f"You earn £{chosen_profession['rate']} per hour.")
    print("You pay 20% tax and 13% National Insurance")
