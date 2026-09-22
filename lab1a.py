# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 9/18/2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: python3 lab1a.py

# TO DO 1: Creating and using varibales
# create a variable called message.
# Set the variable to equal to "Welcome to PRG101".
# Print the variable message using print() statement.
message = "Welcome to PRG101"
print(message)
# >>> Welcome to PRG101

# TO DO 2: Checking the type of a variable
# Use the builtin type() function and print the type of this variable.
type(message)
# >>> <class 'str'>

# TO DO 3: Dynamic Typing:
# Create a varibel called `x` and assign it the value 10, then print the type of this variable.
x = 10
type(x)
# >>> <class 'int'>

# TO DO 4: Dynamic Typing: 
# Now reassign a new value to the variable `x`, this value should be a string, e.g "hello", check the type of the variable `x` again.
# What did you observe?
x = "hello"
type(x)
# >>> <class 'str'>