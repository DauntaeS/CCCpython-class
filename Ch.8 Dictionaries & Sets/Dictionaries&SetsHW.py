# Read the attached file which contains product, amount and price separated by commas in a text file.
# Summarize the data so that it looks as follows. The first part of the output is a dictionary and the second part is formatted output from the dictionary. Total sales is amount*price.


def main():
    line = " "
    counter = 0
    total = 0
    dict = {}

    infile = open("Ch.8 Dictionaries & Sets/sales_data.txt", "r")

    line = infile.readline()
    counter = 1

    while line != "":
        key, value = line.rstrip("\n").split(",")
        dict[key.strip()] = value.strip()
        line = infile.readline()
        counter += 1

        print(line)

        infile.close()


main()
