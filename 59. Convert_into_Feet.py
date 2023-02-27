# 59. Write a Python program to convert the distance (in feet) to inches, yards, and miles.

inches = float(input("Enter distance into Inches : "))
yards = float(input("Enter distance into Yards : "))
miles = float(input("Enter distance into Miles : "))

inch_2_feet = inches*0.083
yard_2_feet = yards*2.999
mile_2_feet = miles*5279.755

print(f"Distance in Feet to Inches : {inch_2_feet}")
print(f"Distance in Feet to Yards : {yard_2_feet}")
print(f"Distance in Feet to Miles : {mile_2_feet}")