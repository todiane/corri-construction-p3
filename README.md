![CCCCP header](/assets/images/ccccp-rm-header.webp)
# Corri Construction Company - Contractor Page

The deployed project live link is [HERE](https://corri-construction-p3-e9d1aa627f6f.herokuapp.com/) - Press Ctrl (Cmd) and mouse click to open in a new window.

Corri Construction Company (not their real name!) hires anything from 2 - 300 contractors in a week. HR was inundated with calls from contractors asking different questions about their pay, so they asked for an app to be built that will help them manage these requests. 

This app asks contractors to input their name, profession, working dates and number of hours. They are then given a rough estimate of payments due to them after tax and NI (which is handled by an umbrella company). Future updates will include the ability to save this information so that contractors can get an overview of their inputted data. Currently, the data is forwarded to HR and a copy to the contractor.

## Project Aims

## Wireframes


## How It Works

Contractors are asked a series of questions after reading the instructions. Having worked with contractors for several years, many of them have a tendency to dislike technology and not follow instructions. This then results in phone calls to HR that could easily be avoided. For this reason it was decided to leave the instructions in full view each time, rather than hide them behind an instruction button.

### What the app checks


- A name is inputted and not left blank. Instructions are given to only use letters to avoid a delay in payment.
![CCCCP name](/assets/images/ccccp-rm-namecheck.webp)


- Profession is chosen from a list of options
![CCCCP name](/assets/images/ccccp-rm-profession.webp)

- The dates worked (must be within a two month period) and the number of hours

- As per Working Time Regulations 1998 a maximum of 13 hours are allowed in a day. App checks that no more than 18 hours can be inputted if the dates show only one day was worked.

- Based on information provided a calculation is made to determine pay before tax and then pay after tax and NI deductions.

## Future Updates

The next update of the app will include the option to choose whether it is their first visit (which will show the instructions) or whether they have used the service before - which will show the instructions behind a button.

The ability to edit information already added if it is incorrect without having to start again.

Contractor can input details of other payments that need to be removed from their pay e.g. student loan or pension.

The program generates an employee number. An update of this app would be to link to a Google sheet where the number is saved so that if they returned and entered their name they will be given the same employee number and their past submissions will be listed.

## Testing

## Credits

Free Code Camp Python for everyone course that helped me get my project started - [here](https://www.youtube.com/watch?v=wgkC8SxraAQ)

py4e autograder to help with checking maths - [here](https://www.py4e.com/tsugi/store/test/pythonauto )

Geek for Geek to help me use strip() to add required field for first/last name - [here](https://www.geeksforgeeks.org/python-program-to-check-if-string-is-empty-or-not/)


Help putting together the function that calculates income tax and national insurance I started with this video and adapated it - [here](https://www.youtube.com/watch?v=b4lok6-_GGg )

To change numerical value to end in two figures only - [here](https://tutorial.eyehunts.com/python/how-to-display-2-decimal-places-in-python-example-code/)

Using colorama import - [here](https://www.youtube.com/watch?v=u51Zjlnui4Y )

Header code - being able to bold and center - taken from w3Schools - [here](https://www.w3schools.com/python/ref_string_center.asp)


## Acknowledgements

Code Institute women-in-tech group for their support during huddles.

Travis.media community - To help with to and from dates function so it worked correctly

My mentor