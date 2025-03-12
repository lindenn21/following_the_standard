# Ask user to input the first number
# Ask user to input the following numbers
# First number will be subtracted to the following numbers
# Print the result

first_num = float(input("Input number 1: "))
for i in range(0, 9):
    num = float(input(f"Input number {i + 2}: "))
    first_num -= num
print(first_num)

# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
