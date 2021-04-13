# Given three integers, print the smallest one. (Three integers should be user input)
num = int(input("Enter your first number:"))
num1 = int(input("Enter your second number:"))
num2 = int(input("Enter your third number:"))

if num < num1 and num < num2:
    print(f"{num} is the smallest number.")

elif num1 < num and num1 < num2:
    print(f"{num1}is the smallest number.")
else:
    print(f"{num2} is the smallest number.")
print("Your program is over.")