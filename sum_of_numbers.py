# use the numbers.txt file for this piece of python code

def main():
    open_numbers = open('numbers.txt', 'r')
    accumulator = 0
    for line in open_numbers:
        line = line[:-1]
        accumulator += int(line)
    print('The total of the numbers in numbers.txt is', accumulator)
    open_numbers.close()

main()