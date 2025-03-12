# Ask the user to input 10 numbers.
# Sum the 10 numbers

# sum is set to 0
sum = 0
print("Input 10 numbers please.")

# Asks the user to input 10 numbers
for i in range(0, 10):
    num = float(input(f"number {i + 1}: "))
    sum += num # Num value input by the user will be added to sum
print(f"the sum is {sum}") # prints the answer

# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.