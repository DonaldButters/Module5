"""

Program: basic_loop.py

Author: Donald Butters

Last date modified: 9/25/2020

The purpose of this program is write a for loop to print a list of floating point numbers.
The second part of the program prints the odd numbers decending from 99 to 33

"""
print("Declare a list of floating point number and write a for loop to print each")
print()
list_1 = ["3.14", "8.67", "9.13", "17.36", "45.67"]
floats_1 = []
for item in list_1:
    floats_1.append(float(item))
print(floats_1)
print()
print("Odd numbers decending from 99-33(including 33)")
print()
a = range(1,101)
for y in range(98,31,-2):
    print(a[y], end=" ")
