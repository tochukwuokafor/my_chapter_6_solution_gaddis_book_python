#use numbers.txt file to practice the function below

def main():
    my_file = open('numbers.txt', 'r')
    for line in my_file:
        line = line.rstrip('\n')
        print(line)
    my_file.close()

main()