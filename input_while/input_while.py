"""

Program: input_while.py

Author: Donald Butters

Last date modified: 9/25/2020

The purpose of this program is prompt for 5 inputs between 1-100 and save to list.
Then the program out puts the list

"""

list_1 = []
values = range(1,100)
print("Enter 5 numbers between 1-100")
for i in range(5):
    numbers = int(input("Enter # :"))
    if numbers in values:
     list_1.append(numbers)
    else:
        input("Please use a number between 1 -100 :")
print (list_1)

'''comments
I found out after some testing of this code that if I enter the wrong number over and over
and then add the correct numbers it wont print correctly. otherwise the code outputs the correct data'''
