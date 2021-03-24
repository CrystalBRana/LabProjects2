# WAP which accepts marks of four subjects and display total marks, pecentage and grade.
# Hint: more than 70% -> distinction, more than 60% -> first, more than 40% -> pass, less than 40% -> fail
print("Enter the marks obtained by students in specific subjects. ")
Math = float(input("Enter the marks of maths:"))
Architecture = float(input("Enter the marks of architecture:"))
Programming = float(input("Enter the marks of programming:"))
Lab = float(input("Enter the marks of lab:"))
total_marks = Math + Architecture + Programming + Lab
total_percentage = total_marks/4
print(f"Your total percentage {total_percentage}%.")
if total_percentage>100:
    print('Please re-enter your markss!!')
elif total_percentage >=70:
    print("Congratulation!! Distinction!!")
elif total_percentage >= 60:
    print("Congratulation!! First Division!!")
elif total_percentage >= 40:
    print("Congratulation!! You are pass!!")
elif total_percentage <40 and total_percentage>=0:
    print("Sorry!! You are fail!!")
elif total_percentage <0:
    print("Sorry!! You are not eligible!!")
print("Program is over!!")