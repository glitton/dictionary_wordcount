the_file = open('test.txt')
word_counts = {}

for line in the_file:

    line_split = line.strip().split(' ')
    for word in line_split:
        word_counts[word] = word_counts.get(word, 0) + 1

the_file.close()

print word_counts
