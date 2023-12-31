
# Corri Construction Company - Contractor Page
![CCCCP header](/assets/images/cc-rm-instructions.png)

Corri Construction Company (not their real name!) hires anything from 2 - 300 contractors in a week. HR was inundated with daily calls from contractors asking different questions about their pay. Many contractors would store up three to four months of work before submitting their invoices, which caused payroll issues. A consultation took place with the company and contractors to discuss the best way to get regular pay invoices from contractors and to reduce the HR call volume. The end result of the consultation was the request for a portal to be built that will help them manage contractors pay. 

The deployed project live link is [HERE](https://corri-construction-8c4725a33281.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Contents

- [Introduction](#introduction)
- [Project](#project)
  - [User goals:](#user-goals)
  - [Site owner goals](#site-owner-goals)
- [Pre development](#pre-development)
- [Development](#development)
- [Features](#features)
  - [Slow Typing Instructions](#slow-typing-instructions)
  - [Name and profession input](#name-and-profession-input)
  - [Hourly pay and employee number](#hourly-pay-and-employee-number)
  - [Working dates, days and hours](#working-dates-days-and-hours)
  - [Confirm information so far](#confirm-information-so-far)
  - [Tax and National Insurance](#tax-and-national-insurance)
  - [Confirmation of information](#confirmation-of-information)
  - [What the portal checks](#what-the-portal-checks)
  - [Error Page](#error-page)
- [Google Sheets](#google-sheets)
  - [Payments](#payments)
  - [Tax](#tax)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
  - [Libraries](#libraries)
- [Testing](#testing)
- [Future Updates](#future-updates)  
- [Validation](#validation)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Branching the GitHub Repository using GitHub Desktop and Visual Studio Code](#branching-the-github-repository-using-github-desktop-and-visual-studio-code)
- [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Introduction

This portal asks contractors to input their name, profession, working dates, number of days worked and number of hours. They are then given a rough estimate of their pay due after tax and NI (which is handled by an umbrella company). The data is forwarded to HR (who extract information for the umbrella company) with a copy also sent to the contractor's email address.

## Project 

The aim of this project is to:

- Reduce the number of calls from contractors to HR asking about their pay.
- Encourage contractors to enter their working dates regularly and within a couple of months.
- Provide a system that will send the information added by the contractor to HR as well as the user.
- Provide clear, visible instructions with each visit.*

![storyboard](assets/images/ccccp-storyboard-small.png)


*Contractors felt that it was important for the instructions to be shown EACH TIME a contractor visits. In a questionnaire sent out many of them cited their dislike of technology and the fact that they tend to ignore instructions unless they are in front of them. This then results in phone calls to HR that could easily be avoided. For this reason it was decided to leave the instructions in full view each time, rather than hide them behind an instruction button.

### User goals:

Get clear instructions on how to use the system in front of them that they can refer to if needed.
The ability to input their details including dates of work, days, and hours.
Retrieve their employee number.
Get an estimate of tax and national insurance due to be paid.
Receive a copy of the information inputted via email.


### Site owner goals

Provide a program that is easy to use and maintain.
Present a program that gives clear instructions each time a contractor visits.
Get access to the information inputted by users via email.
Develop a program that can have additional features added at a later date.
Add the submitted information to Google Sheets with one sheet for information before tax and the other sheet containing tax and national insurance information.


### Pre development
I wrote out notes and created a flow chart. All I had to do then is follow my notes and code one area at a time before moving on to the next. I set up projects in GitHub to write out work that needed to be done. The aim is to provide early and continuous delivery of the project.

![ccccp flow chart](/assets/images/ccccp-flow-chart.png)

My actual notes that created the flow chart

![CCCCP notes](/assets/images/corri-constructionx500.webp)

![CCCCP notes](/assets/images/corri-rm-construction.webp)

### Development

Code was written for each part of the program starting with the header and input for contractors to add their name. Once each section was working the development of the following section took place. Once all sections had been created testing took place which highlighted the need for additional features.

i.e.
In the "input name" section the user could hit enter and a blank space would be inputted so the first and last names were made required fields. Instructions were written to ensure each user understood the importance of entering their name only. After testing with required fields, the inability to add symbols and numbers was also added.

![CCCCP name error](/assets/images/cc-rm-name-error.png)

In the "input dates and hours" section testing highlighted the fact that a customer can enter that they worked for just one day but worked 36 hours. Additional coding was added to ensure the maximum number of hours worked in a day was 13 and that applied whether a user worked one day or 10.


## Features

### Slow Typing Instructions
A staggered typing effect was used to display the instructions at the beginning and at different stages of the program at close to reading speed. The sleep effect was used to allow for delays in displaying the next line of information.
This provided time for the customer to process the information given before starting to input their details, the hope is that this will result in a reduction in input errors.

### Name and profession input
This feature gives the program the information it needs to find the contractor and connect to their employee number. 

![CCCCP name](/assets/images/cc-rm-name.png)


Next. The contractor is asked to select their profession. An error message is displayed if an invalid letter is added:

![CCCCP profession](/assets/images/cc-rm-profession-invalid.png)

An opportunity to pick again if the wrong profession was selected has also been given.

![CCCCP profession](/assets/images/cc-rm-profession-incorrect.png)

### Hourly pay and employee number
Once a contractor has selected their name and profession and confirms the information is correct, the computer brings up confirmation of their hourly pay and contractor number.

![CCCCP pay](/assets/images/cc-rm-pay-number-confirmation.png)

### Working dates, days and hours
The contractor is then prompted to add the dates they worked, the number of days and the number of hours. The number of days worked was not originally included in the program but after testing it was added to avoid any confusion about the days a contractor has worked. 

![CCCCP dates](/assets/images/cc-rm-incorrect-dates.png)

The dates and number of days must match exactly otherwise the user cannot continue to add any further details. This avoids a contractor adding that they worked for 1-08-2023 to 7-08-2023 but they only worked 3 out of those 7 days. The contractor will then have to complete the exact number of days to continue moving forward.

### Confirm information so far

The contractor will be asked to confirm all the information they have submitted so far before being able to move on. 

![CCCCP check](/assets/images/cc-rm-check-information.png)

If anything needs to change e.g. name, professions, hours, dates etc. the contractor selects n for no.

![CCCCP no selection](/assets/images/cc-rm-check-information-invalid.png)

### Tax and National Insurance
Once all information has been added the program will give a contractor a rough estimate of the tax and national insurance due, which is taken by an umbrella company they joined. The majority of self-employed contractors pay 20% tax or less so it wasn't felt necessary to include a 40% tax option for those earning more than £67,500 in a tax year. This could be added in the future if necessary.

![CCCCP confirm](/assets/images/cc-rm-check-information-ok.png)

### Confirmation of information

Once the amount before and after tax has been shown the contractor can confirm that they would like this information submitted to HR. HR keep detailed information on the contractors they use and the hours they work. The information submitted is checked by a manager who confirms the working hours and days. Information on tax and NI payments is sent to the umbrella company.


### What the portal checks


A name is inputted and not left blank. Instructions are given to only use letters to avoid a delay in payment.

![CCCCP name](/assets/images/cc-rm-name-error.png)


Profession is chosen from a list of options

![CCCCP professions](/assets/images/cc-rm-profession.png)

The dates (must be within a two month period), the total number of days and hours worked.

![incorrect dates](/assets/images/cc-rm-incorrect-dates.png)


As per Working Time Regulations 1998 a maximum of 13 hours are allowed in a day. App checks that less than 13 hours is inputted per day.

![CCCCP hours](/assets/images/cc-rm-13.png)

Hours can not exceed the dates.


Based on information provided a calculation is made to determine pay before tax and then pay after tax and NI deductions.


![CCCCP confirm](/assets/images/cc-rm-check-information-ok.png)

The program checks that the contractor is ready to submit this information. 

If they select yes, they receive confirmation of submission

![CCCCP submission](/assets/images/cc-rm-information-submitted.png)

If they select no, they are invited to re-submit, as shown above.

### Error Page

A 404 error page has been included. The html was run through the W3C html validator and errors removed. A css style file was created to support the display of the text on the page.


## Google Sheets

Using Google sheets wasn't part of the original project spec and was added after all the code was created, tested and working. The sheet contains two sections

### Payments
In this area the following contractor information is included:

- First name
- Last name
- Profession
- Start date
- End date
- Pay before tax

![gsheet](assets/images/gsheet-rm-ccccp.png)

### Tax
In this area the following contractor information is included:

- First name
- Last name
- Profession
- Pay before tax
- Tax to pay
- National Insurance to pay

![gsheet](assets/images/gsheet2-rm-ccccp.png)

This information is sent to the umbrella company.

## Technologies Used

The main technology used to create this program is Python
HTML and CSS to change the background and add social media links.
Google API
Google Sheets

### Resources

- Codeanywhere 
- Visual Studio Code (VSC)
- GitHub 
- Heroku
- Font Awesome
- Canva for help with images
- miro.com to create flow chart

### Libraries
[colorama Fore & Back](https://pypi.org/project/colorama/)
[random](https://docs.python.org/3/library/random.html) - to generate contractor number
[typing](https://www.101computing.net/python-typing-text-effect/))
[datetime](https://www.programiz.com/python-programming/datetime)
[sleep](https://www.programiz.com/python-programming/time/sleep) - function for delays in typing out lines

## Testing

The portal has been well tested and the results can be viewed [here - TESTING](https://github.com/todiane/corri-construction-p3/blob/main/TESTING.md)


## Future Updates

The next update of the app will include the option to choose whether it is their first visit (which will show the instructions) or whether they have used the service before - which will show the instructions behind a button.

The ability for a manager to log into the system and confirm working dates and days for each contractor all in one place rather than via separate emails.

Relevant information is accessible by the umbrella company so that HR doesn't have to collate and forward this information.

Other future updates are included in the TESTING.md file.

## Validation

PEP8 - Python style guide checker imported - https://pypi.org/project/pep8/
All code validated and where lines were showing as too long they were adjusted. Some line adjustments caused bugs in the code and it stopped working so they were left as longer lines to avoid this issue. pycodestyle . - was used in Codeanywhere terminal to list any issues.

## Deployment

### Heroku

The Application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name ( for example corri-construction-p3) and then choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars add the private API key information using key 'CRED' and into the value area copy the API key information added to the .json file.  Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, set it up so Python will be on top and Node.js on bottom
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To connect Heroku app to your Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below.
9.  Choose the branch you want to build your app from
10. If preferred, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Branching the GitHub Repository using GitHub Desktop and Visual Studio Code
1. Go to the GitHub repository.
2. Click on the branch button in the left hand side under the repository name.
3. Give your branch a name.
4. Go to the CODE area on the right and select "Open with GitHub Desktop".
5. You will be asked if you want to clone the repository - say yes.
6. GitHub desktop will suggest what to do next - select Open code using Visual Studio Code.
   
The deployed project live link is [HERE](https://corri-construction-8c4725a33281.herokuapp.com/) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

## Bugs

After importing the type element so that text can be typed out a line at a time the codes for Fore.WHITE or bold kept showing up e.g. '\033[1m' for bold was typed out. To fix this I had to remove - colorama.init(autoreset=True) - which  meant I had to go through each line of code to ensure if one line was red, all subsequent lines didn't turn red. 

## Credits

Free Code Camp Python for everyone course that helped me get my project started - [here](https://www.youtube.com/watch?v=wgkC8SxraAQ)

py4e autograder to help with checking maths - [here](https://www.py4e.com/tsugi/store/test/pythonauto )

Geek for Geek to help me use strip() to add required field for first/last name - [here](https://www.geeksforgeeks.org/python-program-to-check-if-string-is-empty-or-not/)


Help putting together the function that calculates income tax and national insurance I started with this video and adapted it - [here](https://www.youtube.com/watch?v=b4lok6-_GGg )

To change numerical value to end in two figures only - [here](https://tutorial.eyehunts.com/python/how-to-display-2-decimal-places-in-python-example-code/)

Using colorama import - [here](https://www.youtube.com/watch?v=u51Zjlnui4Y )


Being able to bold and center font - taken from w3Schools - [here](https://www.w3schools.com/python/ref_string_center.asp)


## Acknowledgements

Code Institute women-in-tech group for their support during huddles and when reviewing my code.

Peer-review slack channel for help trying to find any issues/break the code.

Tutor support for help with figuring out how to round numbers in Google sheet.

Travis.media community - To help with date/hours/time function so it worked correctly.

My mentor Andre Aquilina for teaching me about the proper structure for code - e.g. imports, functions, main code and for encouraging me to create the Google sheets addition and for helping with explaining coding.