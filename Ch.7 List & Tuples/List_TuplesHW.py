# Design a program that lets the user enter the total rainfall for each of 12 months into a list. The program should calculate and display the total rainfall for the year, the average monthly rainfall, the month NAMES with the highest and lowest amounts.

# Input
# ask user for 12 numbers
# empty list

# Process
# Take the numbers entered and add them all together
# total = rain for the year

# Output
# total divided by 12 = average
# return Max month with most rain
# return Min month with least rain


def main():
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "June",
        "July",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
    ]

    rainfall = []
    total = 0

    for i in range(len(months)):
        amount = float(input(f"How much did it rain in {months[i]}? "))
        rainfall.append(amount)
        total += amount

    avg = total / len(months)

    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]

    print(f"Total rainfall: {total}")
    print(f"Average monthly rainfall: {avg}")
    print(f"Month with highest rainfall: {max_month} ({max_rainfall})")
    print(f"Month with lowest rainfall: {min_month} ({min_rainfall})")


main()
