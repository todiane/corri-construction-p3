# Main code for Corri Construction Company

# imports ----------
from datetime import datetime, timedelta
import time
import os
import sys
from flask import Flask
from colorama import Fore, Back, Style
# --------------

# Typing effect for letters taken from Python 101


def type_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')

# Corri Construction Company Introduction


text = Fore.WHITE + '\033[1m' + "CORRI CONSTRUCTION COMPANY CONTRACTORS PAGE" + '\033[0m'
new_text = text.center(90)
print(new_text)

# Instructions for contractors

type_print(Fore.YELLOW + '\033[1m' + "\n Use this portal to input your August(08) and September(09) 2023 hours.\n")
type_print(Fore.WHITE + " If your hours are for previous months please contact HR on 01305 483048")
time.sleep(1)
type_print("\n INSTRUCTIONS: (please read carefully)")
time.sleep(1)
type_print(Fore.RED + "\n Information once entered CANNOT be amended. " + Fore.WHITE + "If you make an error")
type_print(" and want to resubmit, press the " + Fore.GREEN + "'RUN CONTRACTOR PROGRAM'" + Fore.WHITE + " button.\n")
time.sleep(2)
type_print(" Failure to input your NAME correctly may result in your pay being delayed.\n")
type_print(" Our system uses your " + Fore.GREEN + "name and employee number" + Fore.WHITE + " to find you so it is important")
type_print(" that you enter the FULL NAME you provided for our records.")
type_print(" e.g. " + Fore.GREEN + "Mark Jenkins" + Fore.WHITE + ", although " + Fore.GREEN + "mark jenkins " + Fore.WHITE + "and " + Fore.GREEN + "MARK JENKINS " + Fore.WHITE + "are also ok.\n")
time.sleep(3)
type_print(" All Clear? Great. Let's get started - otherwise contact HR\n")
time.sleep(0.5)
type_print(Fore.GREEN + " Input your FULL (First + Last) name to begin:\n")
time.sleep(0.5)

"""
Instructions to add first and last name.
Used strip() to detect if section left blank
"""


while True:
    first_name = input(Fore.WHITE + " Enter your First Name: ")
    if first_name.strip() == "":     # code found at GeeksforGeeks
        type_print(Fore.RED + " First name is required. Please enter a valid first name.")
        continue
    elif not first_name.isalpha():   # code found at GeeksforGeeks
        type_print(Fore.RED + " First name should not contain numbers or symbols. Enter a valid first name.")
        continue
    last_name = input(" Enter your Last Name: ")
    if last_name.strip() == "":
        type_print(Fore.RED + " Last name is required. Please enter a valid First & Last name.")
        continue
    elif not last_name.isalpha():
        type_print(Fore.RED + " Your name should not contain numbers or symbols. Re-enter name.")
        continue
    break

type_print(Fore.YELLOW + " HELLO, " + first_name + " " + last_name + "\n")

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
        type_print(Fore.WHITE + " Select your profession:")
        time.sleep(1)
        print('')
        for key, profession in professions.items():
            print(f"{key}: {profession['name']}")

# Prompt the user to enter the letter corresponding to their choice
        choice = input("\n Select one of the above options " + Fore.GREEN + "a-f: ").lower()

        """
        Validate the users input and confirm their choice
        Or let them know their input is incorrect and provide the
        list of options again
        """
        if choice in professions:
            confirm = input(f" You chose {professions[choice]['name']}. Is this correct? Enter (y/n) only: ").lower()
            if confirm == "y":
                return professions[choice]
        else:
            print(Fore.RED + " Error: Invalid choice. Please choose a valid option.\n")

# If yes print out the details including random user number and hourly pay


if __name__ == "__main__":
    chosen_profession = get_profession_choice()
    import random
    type_print(Fore.WHITE + " Thank you.\n")
    time.sleep(1)
    print(" " + first_name + " your contractor number is " + str(random.randint(23203, 63944)))
    type_print(f" Your profession is: {chosen_profession['name']}")
    time.sleep(1)
    type_print(Fore.GREEN + f" You earn £{chosen_profession['rate']} per hour")
    time.sleep(1)
    type_print(Fore.WHITE + " You pay 20% tax and 13% National Insurance\n")

# Ask user for dates and hours
type_print(Fore.GREEN + "\n Next, we need to know the dates you worked (From - To)")
type_print(Fore.GREEN + " plus the number of days and number of hours worked.\n")
time.sleep(0.5)
type_print(Fore.WHITE + " This is for the months of August (08) and September(09) only.\n")
time.sleep(0.5)

"""
Asks users to input their days worked, number of days and total number of hours
worked. Max number of hours allowed in one day is 13. Validates dates are in
the right order, and the number of days added fits in with the dates inputted.

Code added with help from Travis.Media
"""
# function to check that no more than 13 days are worked in one day

def worked_too_many_hours(days_worked, hours_entered):
    max_hours_per_day = 13
    max_total_hours = days_worked * max_hours_per_day
    if hours_entered > max_total_hours:
        return True
    return False


while True:
    try:
        start_date_str = input(Fore.WHITE + " Enter the start date (DD-MM-YYYY): ")
        end_date_str = input(Fore.WHITE + " Enter the end date (DD-MM-YYYY): ")
        days_worked = int(input(Fore.WHITE + " Enter the number of days worked: "))
        hrs = float(input(Fore.WHITE + " Enter your hours: "))

        start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
        end_date = datetime.strptime(end_date_str, "%d-%m-%Y")

        # Validates that dates are within the specified range
        valid_start_date = datetime(2023, 8, 1)
        valid_end_date = datetime(2023, 9, 30)

        if start_date < valid_start_date or end_date > valid_end_date:
            print(Fore.RED + " Error: The start and/or end date is outside the allowed range (01-08-2023 to 30-09-2023).")
            continue

        calculated_days_worked = (end_date - start_date).days + 1

        if days_worked != calculated_days_worked:
            print(Fore.RED + " Error: The dates entered and the number of days worked do not match.")
            continue

        if worked_too_many_hours(days_worked, hrs):
            print(Fore.RED + " Error: You cannot enter more than 13 hours per day for a total of " + str(days_worked) + " days.")
        else:
            print(" You have entered " + str(hrs) + " hours for " + str(days_worked) + " days.")
            break
    except ValueError:
        print(Fore.RED + " Error: Invalid info. Check your date. The year and days worked.")

# Ask user to confirm the information added is correct
info_confirm = input(Fore.GREEN + f"\n Check that the information added so far is correct & confirm. Enter (y/n) only: ").lower()
if info_confirm == "y":
    type_print(Fore.WHITE + "\n Thank you, " + first_name + ".")
    time.sleep(1)

else:
    type_print(Back.RED + Fore.WHITE + "\n Okay. You can't edit anything already entered " + first_name + ",")
    time.sleep(1)
    type_print(Fore.WHITE + " but you can hit the" + Fore.GREEN + "'RUN CONTRACTOR PROGRAM'" + Fore.WHITE + " button above to start again.")
    quit()

# Confirm information of profession rate, dates, hours plus tax amount
type_print("\n This information will be authorised by your manager:\n")
time.sleep(1)
pay = float(hrs) * chosen_profession['rate']
type_print((f" From {start_date.strftime('%d-%m')}") + " " + (f"to {end_date.strftime('%d-%m')}") + f" 2023, your pay before tax is £{pay:.2f} for {hrs} hours")
time.sleep(1)

# Calculates amount after tax and national insurance deductions


def final_pay(pay, tax, national_insurance):
    pay_after = pay - (tax * pay) - (national_insurance * pay)
    return pay_after


tax = 0.02
national_insurance = 0.013
pay_after = final_pay(pay, tax, national_insurance)
tax_amount = tax * pay
national_insurance_amount = national_insurance * pay


# Print out full result of pay minus tax and NI
pay_statement = Fore.YELLOW + (f"\n Your pay minus tax of (£{tax_amount:.2f}) and NI of (£{national_insurance_amount:.2f}) is £{pay_after:.2f}")
pay_summary = pay_statement.center(80)
type_print(pay_summary)
time.sleep(1)

type_print(Fore.WHITE + "\n The TAX and NATIONAL INSURANCE amounts shown are for your information only")
time.sleep(1)
print('')
type_print(" Final pay amounts are approximate and depend on your tax status.")
time.sleep(1)
type_print(" The actual amount you are paid may change.")
time.sleep(1)
print('')
type_print(" If you have any questions contact HR on 01305 483048.\n")

# Ask user if they want to exit
exit = input(Fore.GREEN + f" Information Complete. Select y to submit or n to continue (y/n): ").lower()
if exit == "y":
    type_print(Fore.WHITE + "\n Information successfully submitted to HR. Thank you " + first_name + ".")
    time.sleep(1)
    print('')
    type_print(" A copy has been sent to the email address we have on file for you.")
    print(" If you have any questions contact HR on 01305 483048.\n")
    time.sleep(1)
    type_print(Fore.GREEN + " You can now exit this window " + first_name + ".")
    quit()


else:
    type_print(Back.RED + Fore.WHITE + "\n Okay. You can't edit anything already entered " + first_name + ",")
    time.sleep(1)
    type_print(" but you can hit the Run Program button above to start again.\n")
    quit()
