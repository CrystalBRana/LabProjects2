'''
 Check whether the given year is leap year or not. If year is leap print "LEAP YEAR" else print "COMMON YEAR"
Hint: -  a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible 100
    - a year is always a leap year if its number is exactly divisible by 400
'''

year = int(input("Enter the year:"))
if (year % 4) == 0:
    print("It is Leap Year!!")
elif (year % 100) == 0:
    print("It is Leap Year!! ")
elif (year % 400) == 0:
    print("It is Leap Year!! ")
else:
    print("It is common year!!")
print("Your program is finished!!")