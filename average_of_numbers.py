# use the numbers.txt file to practise this piece of python code

def main():
    open_numbers = open('numbers.txt', 'r')
    accumulator = 0
    counter = 0
    for number in open_numbers:
        number = number[:-1]
        accumulator += int(number)
        counter += 1
    average = accumulator / counter
    print('The average of all the numbers stored in the numbers.txt file is', average)

main()