# Main code for Corri Construction Company that appears in terminal

# imports ----------
import datetime
import time,os,sys
from flask import Flask
from colorama import Fore, Back, Style
# --------------

# Typing effect for letters from Python 101

def type_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')

# Clears the screen at the very end

def clearScreen():
  os.system("clear")


# Corri Construction Company Introduction


text = Fore.WHITE + '\033[1m' + "CORRI CONSTRUCTION COMPANY CONTRACTORS PAGE" + '\033[0m'
new_text = text.center(90)
print(new_text)

# Instructions for contractors
type_print(Fore.YELLOW + '\033[1m' + "\nUse this portal to input your August(08) and September(09) 2023 hours.\n")
type_print(Fore.WHITE + "If your hours are for previous months please contact HR on 01305 483048")
time.sleep(1)
type_print("\nINSTRUCTIONS: (please read carefully)")
time.sleep(1)
type_print(Fore.RED + "\nInformation once entered CANNOT be amended. " + Fore.WHITE + "If you make an error")
type_print("and want to resubmit, press the " + Fore.GREEN + "'RUN CONTRACTOR PROGRAM'" + Fore.WHITE + " button.\n")
time.sleep(2)
type_print("Failure to input your NAME correctly may result in your pay being delayed.\n")
type_print("Our system uses your " + Fore.GREEN + "name and employee number" + Fore.WHITE + " to find you so it is important")
type_print("that you enter the FULL NAME you provided for our records.")
type_print("e.g. " + Fore.GREEN + "Mark Jenkins" + Fore.WHITE + ", although " + Fore.GREEN + "mark jenkins " + Fore.WHITE + "and " + Fore.GREEN + "MARK JENKINS " + Fore.WHITE + "are also ok.\n")
time.sleep(3)
type_print("All Clear? Great. Let's get started - otherwise contact HR\n")
print(Fore.GREEN + "Input your FULL (First + Last) name to begin:\n")

# Instructions to add first and last name. Used strip() to detect if section left blank
while True:
    first_name = input(Fore.WHITE + "Enter your First Name: ")
    if first_name.strip() == "":     # code found at GeeksforGeeks
        type_print(Fore.RED + "First name is required. Please enter a valid first name.")
        continue
    elif not first_name.isalpha():   # code found at GeeksforGeeks
        type_print(Fore.RED + "First name should not contain numbers or symbols. Enter a valid first name.")
        continue
    last_name = input("Enter your Last Name: ")
    if last_name.strip() == "":
        type_print(Fore.RED + "Last name is required. Please enter a valid First & Last name.")
        continue
    elif not last_name.isalpha():
        type_print(Fore.RED + "First name should not contain numbers or symbols. Enter a valid Last name.")
        continue
    break

type_print(Fore.YELLOW + "H E L L O, " + first_name + " " + last_name + "\n")

# Instructions to confirm their profession by selecting a letter.


def get_profession_choice():
    """
    Dictionary to map profession codes to profession names
    and rate of pay to each profession
    """
    professions = {
        "a": {"name": "Bricklayer", "rate": 28.87, },
        "b": {"name": "Plumber", "rate": 46.75, },
        "c": {"name": "Scaffolder", "rate": 25.75, },
        "d": {"name": "Electrician", "rate": 46.75, },
        "e": {"name": "Carpenter", "rate": 32.89, },
        "f": {"name": "Construction Worker", "rate": 27.57, }
    }

    while True:
        # Display available professions to the user
        type_print(Fore.WHITE + "Select your profession:")
        time.sleep(1)
        print('')
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
            print(Fore.RED + "Invalid choice. Please choose a valid option.\n")

# If yes print out the details including random user number and hourly pay


if __name__ == "__main__":
    chosen_profession = get_profession_choice()
    import random
    type_print(Fore.WHITE + "Thank you.\n")
    time.sleep(1)
    print(first_name + " your contractor number is " + str(random.randint(23203, 63944)))
    type_print(f"Your profession is: {chosen_profession['name']}")
    time.sleep(1)
    type_print(Fore.GREEN + f"You earn £{chosen_profession['rate']} per hour.")
    time.sleep(1)
    type_print(Fore.WHITE + "You pay 20% tax and 13% National Insurance\n")
    # print("Earnings this year are £" + str(random.randint(67500, 80000)) + " so you will pay " + {chosen_profession['tax']} + "% tax and 13% National Insurance\n")

# Ask user for dates and hours
type_print(Fore.GREEN + "\nNext, we need to know the dates you worked (From - To) and number of hours.\n")
time.sleep(0.5)
type_print(Fore.WHITE + "This is for the months of August (08) and September(09) only.")
time.sleep(0.5)
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
            print(Fore.RED + "\nInvalid date. Enter a date between 1 August 2023 and 30 September 2023.")

# Function to get the from and to dates from the user


def get_from_to_dates():
    while True:
        from_date = get_date_input(Fore.WHITE + "Enter the from date (DD-MM-YYYY): ")
        to_date = get_date_input(Fore.WHITE +"Enter the to date (DD-MM-YYYY): ")
        if from_date <= to_date:
            return from_date, to_date
        else:
            print(Fore.RED + "\nInvalid dates. The from date must be before or equal to the to date.")


from_date, to_date = get_from_to_dates()


type_print(Fore.GREEN + f"Thank you, you entered from {from_date.strftime('%d-%m-%Y')} to {to_date.strftime('%d-%m-%Y')} as your dates.\n")
time.sleep(1)

# Asks user to input their hours and works out pay
hrs = input(Fore.WHITE + "Enter your hours: ")

# Ask user to confirm the information added is correct
info_confirm = input(Fore.GREEN + f"\nCheck that the information added so far is correct & confirm. Enter (y/n): ").lower()
if info_confirm == "y":
    type_print(Fore.WHITE + "\nThank you, " + first_name + ".")
    time.sleep(1)

else:
    type_print(Back.RED + Fore.WHITE + "\nOkay. You can't edit anything already entered " + first_name + ",")
    time.sleep(1)
    type_print(Fore.WHITE + "but you can hit the" + Fore.GREEN + "'RUN CONTRACTOR PROGRAM'" + Fore.WHITE + " button above to start again.")
    quit()

# Confirm information of profession, dates and hours plus gives before tax amount
type_print("\nThis information will be authorised by your manager:\n")
time.sleep(1)
pay = float(hrs) * chosen_profession['rate']
type_print((f"From {from_date.strftime('%d-%m')}") + " " + (f"to {to_date.strftime('%d-%m')}") + " 2023, your pay before tax is £" + str(pay) + " for" + " " + str(hrs) + " hours\n")
time.sleep(1)
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
pay_summary = pay_statement.center(90)
type_print(pay_summary)
time.sleep(1)

type_print(Fore.WHITE + "\nThe TAX and NATIONAL INSURANCE amounts shown are for your information only")
time.sleep(1)
print('')
type_print("Final pay amounts are approximate and depend on your tax status.")
time.sleep(1)
type_print("The actual amount you are paid may change.")
time.sleep(1)  
print('')
type_print("If you have any questions contact HR on 01305 483048.\n")

# Ask user if they want to exit
exit = input(Fore.GREEN + f"Information Complete. Select y to submit or n to continue (y/n): ").lower()
if exit == "y":
    type_print(Fore.WHITE + "\nInformation successfully submitted to HR. Thank you " + first_name + ".")
    time.sleep(1)
    print('')
    type_print("A copy has been sent to the email address we have on file for you.")
    print("If you have any questions contact HR on 01305 483048.\n")
    time.sleep(1)


else:
    type_print(Back.RED + Fore.WHITE + "\nOkay. You can't edit anything already entered " + first_name + ",")
    time.sleep(1)
    type_print("but you can hit the Run Program button above to start again.\n")
    quit()

# Clear screen message once everything is complete - taken from Python 101

type_print("Your session is now complete.\n")
time.sleep(3)
type_print("This screen will clear itself in 3..")
time.sleep(1)
type_print("2..")
time.sleep(1)
type_print("1..")
time.sleep(1)
clearScreen()