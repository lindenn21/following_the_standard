# While loop asking to input num
# Display inputted numbers from lowest to highest

def smallest_highest():
    number = []

    while True:
        num = float(input("Enter a number: "))
        number.append(num)

        number.sort()
        print(number)

smallest_highest()

# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function