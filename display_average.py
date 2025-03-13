# Ask to input a number
# If num is more than one, sum them then take the average
# Display the answer

number = []
while True:
    try:
        num = int(input("Input a number: "))
        number.append(num)
        SUM = sum(number) / len(number)
        print(SUM)
    except ValueError:
        print("Invalid")
        break

# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
