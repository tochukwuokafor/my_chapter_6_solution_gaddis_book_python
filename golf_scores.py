# use the golf.txt file to practise this piece of code

def new_record():
    new_file = open('golf.txt', 'w')
    counter = int(input('How many new golf score records will you like to create? '))
    for record in range(counter):
        print('Enter name for record #' + str(record + 1) + ' : ', end = '')
        name = input() + '\n'
        new_file.write(name)
        print('Enter score for record #' + str(record + 1) + ' : ', end = '')
        score = input() + '\n'
        new_file.write(score)
    print('The new records have been written!')
    new_file.close()

def add_record():
    existing_file = open('golf.txt', 'a')
    append_recs = int(input('How many golf score records will you like to add to golf.txt? '))
    for record in range(append_recs):
        print('Enter name for record #' + str(record + 1) + ' : ', end = '')
        name = input() + '\n'
        existing_file.write(name)
        print('Enter score for record #' + str(record + 1) + ' : ', end = '')
        score = input() + '\n'
        existing_file.write(score)
    print('The new records have been appended to the existing record!')
    existing_file.close()

def read_record():
    read_file = open('golf.txt', 'r')
    name = read_file.readline()
    while name != '':
        name = name.rstrip('\n')
        print('Name: ', name)
        score = read_file.readline()
        score = score.rstrip('\n')
        print('Score: ', score)
        print()
        name = read_file.readline()
    read_file.close()

def main():
    print('What will you like to do?')
    print('-------------------------')
    print('1. Enter a new golf score record')
    print('2. Add new records to the existing record')
    print('3. Read records from the file and display them')
    print()
    QUIT = 0
    print('Enter 1, 2 or 3: ', end = '')
    selection = int(input())
    while selection != 0:
        if selection == 1:
            new_record()
        elif selection == 2:
            add_record()
        elif selection == 3:
            read_record()
        elif selection > 3:
            print('Enter a number between 1 and 3 to make a selection!!')
        selection = int(input('Enter new record/ add record/read record again? '))


main()