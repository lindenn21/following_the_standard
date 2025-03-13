# While loop: Input numbers
# Display numbers with NO duplicate

# Store user inputs
number = []

# For loop - 10 times
# append - adds input to the list (number)
# Unique - new list based on the existing (number) list
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    number.append(num)
    unique = [num for num in number if number.count(num) == 1]
    print(unique)

# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.