# Ask user to input 10 numbers
# Program will check which number inputted are even
# Print the amount of even numbers

even = 0
for i in range(0, 10):
    num = float(input(f"number {i + 1}: "))
    if num % 2 == 0:
        even += 1
print(even)

# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.