# Ask user to input 10 numbers
# Print first entries only

unique_num = []

for i in range(10):
    num = float(input("Add number"))
    if num not in unique_num:
        unique_num.append(num)
print(unique_num)

# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
