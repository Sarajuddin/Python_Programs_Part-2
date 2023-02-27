# 60. Write a Python program to convert all units of time into seconds

hours = int(input("Enter Hours : "))
min = int(input("Enter Minutes : "))
sec = int(input("Enter Seconds : "))

total_sec = sec + min*60 + hours*3600

print(f"Total Seconds are : {total_sec}")