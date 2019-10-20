# use the words.txt file to practise this piece of code

def main():
    number_of_words = int(input('How many words will you like to write to a file? '))
    filename = open('words.txt', 'w')
    for word in range(number_of_words):
        print('Enter word #' + str(word + 1), ': ', sep = '', end = '')
        enter_word = input() + '\n'
        filename.write(enter_word)
    print('The words have been written to words.txt!')
    filename.close()

main()