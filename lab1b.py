# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 9/18/2026
# Purpose: Use arithmetic in python.
# Usage: python3 lab1b.py

# TO-DO 1:
#	Create a variable called "num1", take its value from user.
num1 = input('Enter a number for num1:')
# >>> Enter a number for num1: 
#	Create another variable called "num2" and take its value from user. 
num2 = input('Enter a number for num2:')
# >>> Enter a number for num2:
print(type(num1))
# >>> class 'str'
print(type(num2))
# >>> class 'str'
# Convert the values to integers using int() function
num1 = int(num1)
num2 = int(num2)
print(type(num1))
# >>> class 'int'
print(type(num2))
# >>> class 'int'

# TO-DO 2:
# Perform all arithmetic oeprations as outlined in the description in README.md file, and print in the required format.
print(f"{num1} + {num2} = {num1 + num2}\n"
      f"{num1} - {num2} = {num1 - num2}\n"
      f"{num1} * {num2} = {num1 * num2}\n"
      f"{num1} ** {num2} = {num1 ** num2}\n"
      f"{num1} / {num2} = {num1 / num2}\n"
      f"{num1} // {num2} = {num1 // num2}\n"
      f"{num1} % {num2} = {num1 % num2}")
# >>> 5 + 10 = 15
# >>> 5 - 10 = -5
# >>> 5 * 10 = 50
# >>> 5 ** 10 = 9765625
# >>> 5 / 10 = 0.5
# >>> 5 // 10 = 0
# >>> 5 % 10 = 5