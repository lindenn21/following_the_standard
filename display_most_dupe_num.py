
def most_dupe_num():
    number = []
    while True:
        try:
            num = int(input("Enter a number: "))
            number.append(num)
            print(most_dupe_num())
        except ValueError:
            break

    return max(set(number), key=number.count)

most_dupe_num()




