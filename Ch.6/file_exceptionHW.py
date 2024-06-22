# Write a program that asks the user for his or her name, then asks the user to enter a sentence that describes himself or herself. Here is an example of the program’s screen: Submit a screenshot of output that should include a screenshot of the folder where your html file is created and a screenshot of the file opened in the browser.

# Once the user has entered the requested input, the program should create an HTML file, containing the input, for a simple Web page. Here is an example of the HTML content, using the sample input previously shown:

# input
# ask user for name
# ask user to describe themselves

# process
# create an html file

# output
# HTML file in following format:

# <html>
# <body>
# <h1>John Doe</h1>
# <hr />
# I am a computer science major
# <hr />
# </body>
# </html>


def main():
    # ask for user input
    name = input("What is your name? ")
    description = input("Briefly describe yourself: ")

    # create html file
    html_file = open("index.html", "w")

    # writes the html: must be fed name & description
    html_template(html_file, name, description)

    # close html file
    html_file.close()


def html_template(html_file, name, description):
    # creates the html tag
    html_file.write("<html> \n")
    # calls html_head function which takes in the html_file
    html_head(html_file)
    # calls the html_body function which takes name, and description
    html_body(html_file, name, description)
    # closes the html tag
    html_file.write("</html>\n")


def html_head(html_file):
    # creates the head tag
    html_file.write("<head>\n")
    # creates the title tag
    html_file.write("<title> This is the head </title>\n")
    # closes the head tag
    html_file.write("</head>\n")


def html_body(html_file, name, description):
    html_file.write("<body>\n")
    html_file.write("<h1>\n")
    html_file.write(name)
    html_file.write("</h1>\n")
    html_file.write("<hr />\n")
    html_file.write(description)
    html_file.write("\n<hr />\n")
    html_file.write("</body>\n")


# calls the main function
main()
