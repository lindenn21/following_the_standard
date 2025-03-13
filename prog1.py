# While loop: Input numbers
# Display numbers with NO duplicate

number = []

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    number.append(num)

    if number.count(num) > 1:
        number.remove(num)

print(number)

# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.