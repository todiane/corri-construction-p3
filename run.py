
# imports ----------

# from colorama import Fore, Back, Style FIND OUT HOW TO ADD COLOUR TO TEXT****
from datetime import datetime

# --------------

"""
Main code for Corri Construction Company that appears in terminal
"""
print("This is the Corri Construction Company Contractors Page.\n")
print("Use this portal to input your hours for August and September 2023 only.")
print("If your hours are for previous months please contact HR on 01305 483048\n")
print("Please input your first and last name to begin\n")

"""
instructions to add first and last name
"""
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
print("Hello " + first_name + " " + last_name + ",\n")

"""
instructions to confirm their profession by
selecting one of the letters provided.

"""
def get_profession_choice():
    """
    Dictionary to map profession codes to profession names
    and rate of pay
    """
    professions = {
        "a": {"name": "Bricklayer", "rate": 28},
        "b": {"name": "Plumber", "rate": 36},
        "c": {"name": "Scaffolder", "rate": 25},
        "d": {"name": "Electrician", "rate": 36},
        "e": {"name": "Carpenter", "rate": 29},
        "f": {"name": "Construction Worker", "rate": 27}
    }

    while True:
        """
        Display available professions to the user
        """
        print("Select your profession:")
        for key, profession in professions.items():
            print(f"{key}: {profession['name']}")

        """
        Prompt the user to enter the letter corresponding to their choice
        """
        choice = input("\nSelect one of the above options a-f: ").lower()

        """
        Validate the users input and confirm their choice
        Or let them know their input is incorrect and provide the
        list of options again
        """
        if choice in professions:
            confirm = input(f"You chose {professions[choice]['name']}. Is this correct? (y/n): ").lower()
            if confirm == "y":
                return professions[choice]
        else:
            print("Invalid choice. Please choose a valid option.\n")

"""
if yes print out the details including random user number and hourly pay
"""

if __name__ == "__main__":
    chosen_profession = get_profession_choice()
    import random
    print("Thank you.\n")
    print(first_name + " " + "your contractor number is " + str(random.randint(23203, 63944)))
    print(f"Your profession is: {chosen_profession['name']}")
    print(f"You earn £{chosen_profession['rate']} per hour.")
    print("You pay 20% tax and 13% National Insurance\n")

"""
Get dates from the user for August or September 2023 only
Checks if the dates are within that range
NEED TO ADD MESSAGE IF DATES ARE IN WRONG ORDER *************
"""
def get_date_from_user(prompt):
    while True:
        try:
            date_str = input(prompt)
            date_obj = datetime.strptime(date_str, "%d-%m-%Y")
            if date_obj < datetime(2023, 8, 1) or date_obj > datetime(2023, 9, 30):
                print("Dates should be between 1st August 2023 and 30th September 2023.")
                print("If your hours are for previous months please contact HR on 01305 483048\n")
            else:
                return date_obj
        except ValueError:
            print("Invalid date format. Please enter a date in the format DD-MM-YYYY.")
           

if __name__ == "__main__":
    print("Enter your dates for August/September 2023 in the format DD-MM-YYYY.")

    from_date = get_date_from_user("Enter the 'from' date: ")
    to_date = get_date_from_user("Enter the 'to' date: ")


"""
Asks user to input their hours and works out pay
"""
hrs = input("Enter your hours: ")
print("\nThis information will be authorised by your manager:\n")
pay = float(hrs) * chosen_profession['rate'] 
print((f"From {from_date.strftime('%d-%m')}") + " " + (f"to {to_date.strftime('%d-%m')}") + " 2023, your pay before tax" + " " + first_name + " " + "is £" + str(pay) + " for" + " " + str(hrs) + " hours\n")

"""
Calculating payment after tax - 20% tax is 0.2 and 13% NI is 0.13
"""
def final_pay(pay, tax, national_insurance):
  pay_after = pay - (tax * pay) - (national_insurance * pay)
  return pay_after

tax = 0.2
national_insurance = 0.13

print(f"Your pay after deducting tax and national insurance is £{final_pay(pay, tax, national_insurance)}.")


"""
NEED TO ADD : IF EVERYTHING IS OK ASK IF THEY WANT TO EXIT
IF THEY SAY NO EVERYTHING ISN'T OK - PRINT CONTACT HR ON  01305 483048

DO YOU WANT A PRINT OUT - CAN i FIGURE OUT HOW TO PROVIDE A PRINT-OUT SO THEY CAN DOWNLOAD IT.
OR SHOULD I JUST GET PYTHON TO LET THEM SAVE THE INFORMATION FOR THEM?

do you want to include 40% tax and 13% option as well - it will have to be a random computer selection 
so when people enter their details the computer will randomly give them either 20% or 40% status
OR I can set it up so plumber and electrician selections are 40% and the others are 20%

"""
