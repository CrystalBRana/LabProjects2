'''
A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students
in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 20 desks. The second group has
21  students , so they can get  by with no fewer than 11 desks. 11 desks are also enough for the third group of 22
students. So, we need 32 desks in total.
'''
a = int(input('Enter the number of students of sec A:'))
b = int(input('Enter the number of students of sec B:'))
c = int(input('Enter the number of students of sec C:'))
studentsPerdesks = 2
