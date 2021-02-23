# N students take K apples and distribute them among each other evenly. The remaining (undivisible) part remains in
# the basket. How many apples will each single student get? How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for the question above.
N = int(input('Enter the number of students in class:'))
K = int(input('Enter the number of apples:'))
D = K//N
print('The number of apples that each students will get', D)
R = K%N
print('The remaining apples are ', R)