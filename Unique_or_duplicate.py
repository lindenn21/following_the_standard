# While loop to endlessly ask until the input isn't a number
# Print the number input
# If it's the first input for the num, print unique. If not, it's duplicate
# End program if the input is invalid

def unique_or_duplicate():
    number = []

# Keep asking until the user inputs something other than numbers
    while True:
        try:
            num = int(input("Enter a number: "))
            number.append(num)

            if number.count(num) == 1:
                print("Unique")
            else:
                print("Duplicate")
        except ValueError:
            print("Invalid")
            break


unique_or_duplicate()

# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

