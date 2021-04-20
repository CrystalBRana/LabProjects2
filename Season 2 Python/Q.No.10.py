'''
Write a Python program  to sum of three given integers. However, if two values are equal sum will be zer0.
'''

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if (a==b) or (b==c) or (a==c):
    print("The two values are equal, so, sum will be zero.")
else:
    total = a + b + c
    print(f"The sum of three number are {total}")
