#use the numbers.txt file to practise this piece of code

def main():
    try:
        open_numbers = open('numbers.txt', 'r')
    except IOError:
        print('Unable to open file and read data!')
    accumulator = 0
    counter = 0
    for number in open_numbers:
        number = number[:-1]
        try:
            accumulator += int(number)
        except ValueError:
            print('Unable to convert item to number!')
        counter += 1
    average = accumulator / counter
    print('The average of all the numbers stored in the numbers.txt file is', average)

main()