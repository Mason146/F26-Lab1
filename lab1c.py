
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Mason Chan
# Date: 9/18/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py

#TO-DO 1:
# import math module.
import math
# Create a variable called 'radius' and take its value form user.
radius = int(input("Please enter radius: "))
# >>> Please enter radius:
# Convert the variable to integer using int()
# use the constant pi form math module and compute the area of the circle using the variable 'radius'
area = math.pi*radius**2
print("Area=", area)
# >>> Area= 123