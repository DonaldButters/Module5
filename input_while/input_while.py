"""

Program: input_while.py

Author: Donald Butters

Last date modified: 9/25/2020

The purpose of this program is prompt for inputs between 1-100 and save to list.
Then the program out puts the list

"""

#input_while.py

user_numbers = []
value = 1

while value != 404:
    try:
        x = int(input("Please Enter a number between 1 and 100. Type 404 to exit. : "))
    except ValueError:
        print('##Input Error - Yeah, gonna need to use the number keys for this.##' )
        print()
        continue
    if x in range(1,101):
        user_numbers.append(x)
        print('Thank you, your number has been added.')
        print()
        print()
    elif x == 404:
        break
    else:
        print('##Input Error##' )
        print()

print('Your numbers are: ')
print()
for i in user_numbers:
    print(i)
print()
print('Goodbye.')

'''comments
I found out after some testing of this code that if I enter the wrong number over and over
and then add the correct numbers it wont print correctly. otherwise the code outputs the correct data'''
