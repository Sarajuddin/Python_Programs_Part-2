# 58. Write a Python program to calculate the hypotenuse of a right angled triangle.

import math

height = float(input("Enter height of Right angle triangle : "))
base = float(input("Enter base of Right angle triangle : "))

hypo = math.sqrt(height**2 + base**2)

print(f"Hypotenuse is : {hypo}")