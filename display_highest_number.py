# Ask user to input a num
# Display the highest inputted number

number = []
while True:
    try:
        num = int(input("Enter a number: "))
        number.append(num)
        biggest = max(number)
        print(f"The biggest number is: {biggest}")
    except ValueError:
        print("Invalid")
        break

# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number