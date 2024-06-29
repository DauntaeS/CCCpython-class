import math


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

    avg = math.ceil(total / len(months))

    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]

    print(f"Total rainfall: {total}")
    print(f"Average monthly rainfall: {avg}")
    print(f"Month with highest rainfall: {max_month} ({max_rainfall})")
    print(f"Month with lowest rainfall: {min_month} ({min_rainfall})")


main()
