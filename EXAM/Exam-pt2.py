def main():
    try:
        # Open the file for reading
        with open("EXAM/numbers.txt", "r") as infile:
            numbers = []
            total = 0

            # Read each line in the file & append to the list
            for line in infile:
                number = int(line.strip())
                numbers.append(number)
                total += number

            if not numbers:
                raise ValueError("The file is empty")

            # Calculate the statistics

            for value in numbers:
                highest_num = value
                if value > highest_num:
                    highest_num = value

            maximum = float(highest_num)
            average = float(total / len(numbers))
            unique_numbers = sorted(set(numbers))

            for num in numbers:
                if num > 200:
                    greater_than = num

            # Display the results
            print(f"Total of the numbers is: {float(total)}")
            print(f"The maximum number is: {maximum}")
            print(f"Numbers greater than 200: {float(greater_than)}")
            print(f"The average of the numbers is: {average:.2f}")
            print(f"The unique numbers in file are: \n {unique_numbers}")

    except FileNotFoundError:
        print("The file is not found.")


main()
