# Call 0-100 numbers
# Find numbers that are not divisible by 10
# Print it

# A for loop calling numbers 0-100, then checking if it ends in zero, printing numbers that doesn't end with zero.
for num in range(0, 101):
    if num % 10 != 0:
        print(num)

# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.