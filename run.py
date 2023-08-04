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
print ("What is your job role " + first_name + "?")

def get_profession_choice():
    # Dictionary to map profession codes to profession names
    professions = {
        "a": "bricklayer",
        "b": "plumber",
        "c": "scaffolder",
        "d": "electrician",
        "e": "carpenter",
        "f": "construction worker"
    }

    while True:
        # Display available professions to the user
        print("Choose a profession:\n")
        for key, profession in professions.items():
            print(f"{key}: {profession}")

        # Prompt the user to enter the letter corresponding to their choice
        choice = input("Enter the letter corresponding to your choice: ").lower()

        # Validate the user's input
        if choice in professions:
            # Confirm the user's choice
            confirm = input(f"You chose {professions[choice]}. Is this correct? (y/n): ").lower()
            if confirm == "y":
                return professions[choice]  # Return the chosen profession if confirmed
        else:
            print("Invalid choice. Please choose a valid option.")

#if yes print out the details including employee number and hourly rate of pay
if __name__ == "__main__":
    chosen_profession = get_profession_choice()
    print(first_name + " " + "your employee number is 3432" ) #NEED TO CREATE RANDOM NUMBER
    print(f"Your profession is: {chosen_profession}")
    print("You earn £34 per hour") #NEED TO CREATE CODE FOR PAY
    print("You pay 20% tax and 13% National Insurance")