# use line_numbers.txt file to practice the function below

"""def main():
    filename = input('Enter the name of a file: ')
    open_filename = open(filename, 'r')
    counter = 1
    for line in open_filename:
        line = line[:-1]
        print(counter, ': ', line, sep = '')
        counter += 1
    open_filename.close()

main()"""

# here is another solution ...

def main():
    filename = input('Enter the name of a file: ')
    open_filename = open(filename, 'r')
    counter = 1
    line = open_filename.readline()
    while line != '':
        line = line.rstrip('\n')
        print(counter, ': ', line, sep = '')
        counter += 1
        line = open_filename.readline()
    open_filename.close()

main()