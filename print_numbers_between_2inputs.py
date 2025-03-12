# Ask user to input 2 numbers
# Print numbers between the two inputted numbers

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

# Adds 1 point to the smaller number until it gets to the value of the bigger number.
if num1 < num2:
    print(num1, list(range(num1 + 1, num2)), num2)
else:
    print(num2, list(range(num2 + 1, num1)), num1)

# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.