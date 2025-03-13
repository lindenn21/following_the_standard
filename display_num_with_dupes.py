# While loop: Input numbers
# Display numbers with duplicates

# Store user inputs
number = []

# For loop - 10 times
# append - adds input to the list (number)
# Dupe_list - new list based on the existing (number) list
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    number.append(num)
    Dupe_list = [num for num in number if number.count(num) > 1]
    print(Dupe_list)

# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.