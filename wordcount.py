def word_count(file_name):
    the_file = open(file_name)
    word_counts = {}

    for line in the_file:

        line_split = line.strip().split()
        for word in line_split:
            word_counts[word] = word_counts.get(word, 0) + 1
        
    the_file.close()

    for word, number in word_counts.items():
        print word, number

word_count('twain.txt')
