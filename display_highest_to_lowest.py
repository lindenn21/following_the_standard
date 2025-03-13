# Ask the user to input a number
# Display and sort them from highest to lowest

number = []
while True:
    try:
        num = int(input("Enter a number: "))
        number.append(num)
        number.sort(reverse=True)
        print(number)
    except ValueError:
        print("Invalid")
        break

# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function