"""

Program: input_while_exit.py

Author: Donald Butters

Last date modified: 9/25/2020

The purpose of this program is prompt for inputs between 1-100 and save to list.
Then the program out puts the list

"""

#input_while_exit.py

user_numbers = []
stopvalue = 404

x = int(input("Please Enter a number between 1 and 100. Type 404 to exit. : "))

while x != stopvalue:
    while x not in range(1,101):
        x = int(input("Incorrect. Please enter only numbers 1-100. Type 404 to exit. :"))
        if x == 404:
            print("Your are now exiting the program.")
            break
    else:
        user_numbers.append(x)
        x = int(input("Thank you. "
                      "Your number has been saved. \n"
                      "Enter another number between 1-100\n"
                      "or type 404 to exit. : "))
        if x == 404:
            print('Your numbers are: ')
for i in user_numbers:
    print(i)
print('Thank You. Goodbye')








'''comments
code seems to work as intended. if a user inputs a number between 1-100 they are taken to a promt
tells them their number has been saved. it then promts for another number. each promt will also have
an exit code to leave the program. The exit codes will promt the use goodbye and exit.
The outputs for each test are as expected'''
