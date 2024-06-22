# Write a program that reads the attached file numbers.txt and display the sum and average of numbers stored in the file.  It should handle any IOError exceptions that are raised when the file is opened and data is read from it. It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number.

# try
# open file
# the read each line
# add each num to the next
# print the number total
# print number total divided by amount of numbers
# except errors

# 15


def main():
    try:
        line = " "
        counter = 0
        avg = 0
        total = 0

        infile = open("Ch.6/numbers.txt", "r")

        line = infile.readline()
        counter = 1

        while line != "":
            line = line.rstrip("\n")
            total = total + int(line)
            line = infile.readline()
            counter += 1
            avg = total // counter + 1

        print(total)
        print(avg)

        infile.close()

    except ValueError as error:
        print("This is my error", error)


main()
