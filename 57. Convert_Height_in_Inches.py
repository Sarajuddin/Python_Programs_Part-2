# 57. Write a Python program to convert height (in feet and inches) to centimeters.

cm = float(input("Enter height in Centimeter : "))

inches = cm*0.3937
feet = cm*0.0328

print(f"Height in Feet : {feet}")
print(f"Height in Inches : {inches}")