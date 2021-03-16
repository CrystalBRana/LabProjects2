# Write a Python program to find sum of the first n positive integers.
# sum = (n*(n+1))/2
'''
num = int(input('Enter the number:'))
sum = (num*(num+1))/2
print('The sum of the first n positive integers is', sum)
'''
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(list)
print(f'the sum of given positive integer is {total}')