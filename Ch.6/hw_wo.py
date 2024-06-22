def main():
    name = input("Whats your name? ")
    description = input("Tell me about yourself ")

    html_file = open("index.html", "w")

    make_html(html_file, name, description)

    html_file.close()


def make_html(html_file, name, description):
    html_file.write("<html>\n")
    make_head(html_file)
    make_body(html_file, name, description)
    html_file.write("</html>\n")


def make_head(html_file):
    html_file.write("<head>\n")
    html_file.write("<title> This is the title </title>\n")
    html_file.write("</head>\n")


def make_body(html_file, name, description):
    html_file.write("<body>\n")
    html_file.write("<h1>")
    html_file.write(name)
    html_file.write("</h1>\n")
    html_file.write("<hr />\n")
    html_file.write(description)
    html_file.write("\n<hr />\n")
    html_file.write("</body>\n")


main()
