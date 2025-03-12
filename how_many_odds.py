# Ask the user to input 10 numbers.
# Count how many odds were inputted

# Set the initial amount of odds.
amt_of_odds = 0
print("Input 10 numbers please.")

# Asks the user to input 10 numbers, determines if it is odd or even, then adds 1 for every odd num.
for i in range(0, 10):
    num = float(input(f"Number {i + 1}: "))
    if num % 2 != 0:
        amt_of_odds += 1
print(f"there are {amt_of_odds} odds.")

# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.