# use file_head_display.txt file for practice

def main():
    counter = 0
    file_name = input('Enter the name of the file: ')
    open_file = open(file_name, 'r')
    for _ in open_file:
        counter += 1
    open_file.close()
    open_file = open(file_name, 'r')
    if counter < 5:
        for idx in open_file:
            idx = idx[:-1]
            print(idx)
    else:
        first_five = (open_file.readlines())[:5]
        for j in first_five:
            j = j[:-1]
            print(j)
        open_file.close()

main()