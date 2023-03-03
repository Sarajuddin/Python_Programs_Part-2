# 66. Write a Python program to calculate the sum of the digits in an integer.

num = int(input("Enter an integer : "))
num1 = num
sum = 0
while num != 0:
    rem = num%10
    num //= 10
    sum += rem

print("Sum of digits of %d is %d" %(num1, sum))