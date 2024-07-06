from tabulate import tabulate

# Read the attached file which contains product, amount and price separated by commas in a text file.
# Summarize the data so that it looks as follows. The first part of the output is a dictionary and the second part is formatted output from the dictionary. Total sales is amount*price.

# Input
# file meant to be read
# empty dictionary

# Process
# open/close sales_data.txt file
# Iterate through each line of of the file
# Seperate input data by commas
# Remove blank spacing
# add items to dictionary

# Output
# Table containing data from dictionary


def main():
    # opens the file for reading
    with open("Ch.8 Dictionaries & Sets/sales_data.txt", "r") as infile:
        dict = {}
        # reads initial line and assigns to line variable
        # line = infile.readline()

        for text in infile:
            line = text.split(",")
            name = line[0].strip()
            amount = int(line[1].strip())
            price = float(line[2].strip())

            total_sales = amount * price

            if name in dict:
                dict[name] += total_sales
            else:
                dict[name] = total_sales

    print("\nProduct\t\tTotal Sales")
    print("-" * 30)
    for key, value in dict.items():
        print(f"{key:<10}$ \t {value:.2f}")


main()
