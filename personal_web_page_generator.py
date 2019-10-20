# use the personal_web_page_generator.html for this piece of code

def main():
    name = input('Enter your name: ')
    description = input('Describe yourself: ')
    content = '<html>\n<head>\n</head>\n<body>\n\t<center>\n\t\t<h1>' + name + '</h1>\n\t</center>\n\t<hr  />\n' + description + '\n\t<hr  />\n</body>\n</html>'
    open_file = open('personal_web_page_generator.html', 'w')
    open_file.write(content)
    print('The web page has been generated!')
    open_file.close()
main()