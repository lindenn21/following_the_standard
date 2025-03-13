# While loop: Ask user to input numbers
# most_dupe will check the most inputted number

def most_dupe_num():
    number = []
    while True:
        try:
            num = int(input("Enter a number: "))
            number.append(num)
            most_dupe = max(set(number), key=number.count)
            print(f"The most duplicated number as of now: {most_dupe}")
        except ValueError:
            break

    return max(set(number), key=number.count)

most_dupe_num()

# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.




