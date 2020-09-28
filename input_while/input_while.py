"""

Program: input_while.py

Author: Donald Butters

Last date modified: 9/25/2020

The purpose of this program is prompt for inputs between 1-100 and save to list.
Then the program out puts the list

"""

#input_while.py

user_numbers = []
stopvalue = 404

x = int(input("Please Enter a number between 1 and 100. Type 404 to exit. : "))

while x != stopvalue:
    while x not in range(1,101):
        x = int(input("Incorrect. Please enter only numbers 1-100. :"))
    else:
        user_numbers.append(x)
        x = int(input("Please Enter a number between 1 and 100. Type 404 to exit. : "))

print('Your numbers are: ')
for i in user_numbers:
    print(i)
print('Goodbye.')



'''comments
I found out after some testing of this code that if I enter the wrong number over and over
and then add the correct numbers it wont print correctly. otherwise the code outputs the correct data'''
