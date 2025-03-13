# While loop, ask user to input until invalid
# Display the lowest number

def small():
    number = []

    while True:
        try:
            num = int(input("Enter number: "))
            number.append(num)

            smallest = min(number)
            print(smallest)
        except ValueError:
            print("Invalid")
            break
small()

# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

