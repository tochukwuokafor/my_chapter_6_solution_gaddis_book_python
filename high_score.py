# use scores.txt file for this file

def main():
    open_file = open('scores.txt', 'r')
    counter = 1
    score_dict = {}
    line_one = open_file.readline()
    while line_one != '':
        line_one = line_one.rstrip('\n')
        line_two = open_file.readline()
        line_two = line_two.rstrip('\n')
        score_dict[line_one] = int(line_two)
        print('Record #', counter, ': ', sep = '')
        print('Name:', line_one)
        print('Score:', line_two)
        counter += 1
        line_one = open_file.readline()
    print()
    list_of_scores = list(score_dict.values())
    maximum = max(list_of_scores)
    for name, value in score_dict.items():
        if value == maximum:
            print('The highest score is', maximum, 'by', name)
    open_file.close()

main()