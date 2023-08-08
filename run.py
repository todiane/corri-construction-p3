# Main code for Corri Construction Company that appears in terminal

# imports ----------
import datetime
from flask import Flask
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
# --------------

# Corri Construction Company Introduction
text = Fore.BLUE + '\033[1m' + "CORRI CONSTRUCTION COMPANY CONTRACTORS PAGE" + '\033[0m'
new_text = text.center(71)
print(new_text)

print(Fore.YELLOW + '\033[1m' + "\nUse this portal to input your August(08) and September(09) 2023 hours.\n")
print("INSTRUCTIONS:")
print("If your hours are for previous months please contact HR on 01305 483048")
print("Information once entered cannot be amended.")
print("If you make an error or want to restart, hit the Run Program button.\n")
print(Fore.YELLOW + "Input your first and last name to begin:\n")

# Instructions to add first and last name. Used strip() to detect if section left blank
while True:
    first_name = input("Enter your First Name: ")
    if first_name.strip() == "":    # code found at GeekforGeek
        print("First name is required. Please enter a valid first name.")
        continue
    last_name = input("Enter your Last Name: ")
    if last_name.strip() == "":
        print("Last name is required. Please enter a valid First & Last name.")
        continue
    break

print(Fore.YELLOW + "Hello " + first_name + " " + last_name + "\n")

# Instructions to confirm their profession by selecting a letter.


def get_profession_choice():
    """
    Dictionary to map profession codes to profession names
    and rate of pay to each profession
    """
    professions = {
        "a": {"name": "Bricklayer", "rate": 28, },
        "b": {"name": "Plumber", "rate": 46, },
        "c": {"name": "Scaffolder", "rate": 25, },
        "d": {"name": "Electrician", "rate": 46, },
        "e": {"name": "Carpenter", "rate": 32, },
        "f": {"name": "Construction Worker", "rate": 27, }
    }

    while True:
        # Display available professions to the user
        print(Fore.GREEN + "Select your profession:")
        for key, profession in professions.items():
            print(f"{key}: {profession['name']}")

# Prompt the user to enter the letter corresponding to their choice
        choice = input("\nSelect one of the above options " + Fore.GREEN + "a-f: ").lower()

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
            print(Back.RED + "Invalid choice. Please choose a valid option.\n")

# If yes print out the details including random user number and hourly pay


if __name__ == "__main__":
    chosen_profession = get_profession_choice()
    import random
    print(Fore.WHITE + "Thank you.\n")
    print(Fore.GREEN + first_name + " " + "your contractor number is " + str(random.randint(23203, 63944)))
    print(f"Your profession is: {chosen_profession['name']}")
    print(Fore.GREEN + f"You earn £{chosen_profession['rate']} per hour.")
    print("You pay 20% tax and 13% National Insurance\n")
    # print("Earnings this year are £" + str(random.randint(67500, 80000)) + " so you will pay " + {chosen_profession['tax']} + "% tax and 13% National Insurance\n")

# Ask user for dates and hours
print(Fore.WHITE + "\nNext, we need to know the dates you worked and number of hours\n")

"""
Get dates from the user for August or September 2023 only. Checks if the dates
are within that range and in sequential order if not error message given.
Code created with support from Travis.media.
"""

# Define the valid date range - this can change each month
start_date = datetime.date(2023, 8, 1)
end_date = datetime.date(2023, 9, 30)

# Function to validate the user input


def validate_date(date_str):
    try:
        date = datetime.datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        return False
    # Check if the date is within the valid range
    if start_date <= date <= end_date:
        return date
    else:
        return False

# Function to get the from and to dates from user


def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        date = validate_date(date_str)
        if date:
            return date
        else:
            print(Back.RED + "\nInvalid date. Enter a date between 1 August 2023 and 30 September 2023.")

# Function to get the from and to dates from the user


def get_from_to_dates():
    while True:
        from_date = get_date_input("Enter the from date (DD-MM-YYYY): ")
        to_date = get_date_input("Enter the to date (DD-MM-YYYY): ")
        if from_date <= to_date:
            return from_date, to_date
        else:
            print(Back.RED + "\nInvalid dates. The from date must be before or equal to the to date.")


from_date, to_date = get_from_to_dates()


print(Fore.GREEN + f"Thank you, you entered from {from_date.strftime('%d-%m-%Y')} to {to_date.strftime('%d-%m-%Y')} as your dates.\n")


# Asks user to input their hours and works out pay
hrs = input("Enter your hours: ")

# Ask user to confirm the information added is correct
info_confirm = input(Fore.GREEN + f"\nIs all the information added so far correct? Enter (y/n): ").lower()
if info_confirm == "y":
    print(Fore.WHITE + "\nThank you, " + first_name + ".")

else:
    print(Fore.WHITE + "\nOkay. You can't edit anything already entered " + first_name + ",")
    print("but you can hit the Run Program button above to start again.")
    quit()

# Confirm information of profession, dates and hours plus gives before tax amount
print("\nThis information will be authorised by your manager:\n")
pay = float(hrs) * chosen_profession['rate']
print((f"From {from_date.strftime('%d-%m')}") + " " + (f"to {to_date.strftime('%d-%m')}") + " 2023, your pay before tax is £" + str(pay) + " for" + " " + str(hrs) + " hours\n")

# Calculating payment after tax - 20% tax is 0.2 and 13% NI is 0.13


def final_pay(pay, tax, national_insurance):
    pay_after = pay - (tax * pay) - (national_insurance * pay)
    return pay_after


tax = 0.02
national_insurance = 0.013
pay_after = final_pay(pay, tax, national_insurance)
tax_amount = tax * pay
national_insurance_amount = national_insurance * pay


# Print out full result of pay minus tax and NI
pay_statement = Fore.YELLOW + '\033[1m' + (f" Your pay minus tax of (£{tax_amount:.2f}) and NI of (£{national_insurance_amount:.2f}) is £{pay_after:.2f}") + '\033[0m'
pay_summary = pay_statement.center(70)

print(pay_summary)
print(Fore.RED + "\nThe TAX and NATIONAL INSURANCE amounts shown are for your information only\n")
print("Final pay amounts are approximate and depend on your tax status.")
print("The actual amount you are paid may change.\n")
print("If you have any questions contact HR on 01305 483048.\n")

# Ask user if they want to exit
exit = input(Fore.GREEN + f"Information Complete. Select y to submit or n to continue (y/n): ").lower()
if exit == "y":
    print(Fore.WHITE + "\nInformation successfully submitted to HR. Thank you " + first_name + ".")
    print("A copy has been sent to the email address we have on file for you.")
    print("If you have any questions contact HR on 01305 483048.\n")
    quit()

else:
    print(Fore.WHITE + "\nOkay. You can't edit anything already entered " + first_name + ",")
    print("but you can hit the Run Program button above to start again.\n")
