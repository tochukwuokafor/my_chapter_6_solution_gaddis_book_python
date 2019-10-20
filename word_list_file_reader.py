# use the words.txt file to practise this piece of code

def main():
    open_file = open('words.txt', 'r')
    counter = 0
    accumulator = 0
    longest = []
    length_list = {}
    word = open_file.readline()
    while word != '':
        word = word.rstrip('\n')
        word_length = len(word)
        accumulator += word_length
        length_list[word] = word_length
        counter += 1
        word = open_file.readline()
    for word, length in length_list.items():
        if length == max(list(length_list.values())):
            longest_word = word
            longest.append(longest_word) #if there are more than one word of the same longest length ...
    print('There are', counter, 'words in the file')
    print('The longest word(s) in the file is', longest)
    print('The average length of all of the words in the file is {:.2f}'.format(accumulator / counter))

main()