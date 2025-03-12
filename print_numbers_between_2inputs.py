# Ask user to input 2 numbers
# Print numbers between the two inputted numbers

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
if num1 < num2:
    print(num1, list(range(num1 + 1, num2)), num2)
else:
    print(num2, list(range(num2 + 1, num1)), num1)