# Write a program that validates input values using just one function. Ask the user to enter hours and minutes and the program should use one function to validate if the hours are between 0 and 23 and the minutes are between 0 and 59. Program output should indicate the number of hours and minutes and the input validation function should keep asking the user to enter valid values.This one input validation function should be called from the main function. See sample output below. Submit python program and screenshot of output

# Input
# Process
# Output


# hours = int(input("How many hours? "))
# minutes = int(input("How many minutes? "))


def main():
    while True:
        hours = int(input("Enter a value between 0 and 23 "))
        minutes = int(input("Enter a value between 0 and 59 "))
        if time_window(hours, minutes):
            print(f"You entered {hours} hours and {minutes} minutes.")
            break
        else:
            print("Error, Try again!")


def time_window(hrs, mins):
    if 0 <= hrs <= 23 and 0 <= mins <= 59:
        return True
    return False


main()
