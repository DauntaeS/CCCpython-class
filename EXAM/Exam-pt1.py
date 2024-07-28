def validate(num1, num2):
    if num1 >= 0 and num2 >= 0:
        return True
    else:
        return False


def add(num1, num2):
    return num1 + num2


def outputprint(total):
    print(f"The sum of the numbers you entered is {total}")


def main():
    while True:
        try:
            user_num1 = int(input("Enter a number: "))
            user_num2 = int(input("Enter next number: "))
        except ValueError:
            print("Enter a number greater than 0")
            continue

        if validate(user_num1, user_num2):
            total = add(user_num1, user_num2)
            outputprint(total)
        else:
            print("Enter numbers greater than or equal to 0")

        repeat = input("Do you want to add two more numbers? (y/n): ").strip().lower()
        if repeat != "y":
            break


main()
