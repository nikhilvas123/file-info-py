
def count_lines(lines):
    return len(lines)

def count_characters(lines):
    ch_count = sum([len(line.strip("\n")) for line in lines])    
    return ch_count

def count_spaces(lines):
    space_count = 0
    for line in lines:
        space_count += line.count(" ")
    return space_count

def count_words_in_line(line):
    return len(line.strip("\n").split(" "))

def count_words_in_each_line(lines):
    word_count_in_each_line = []
    for line in lines:
        word_count_in_each_line.append(count_words_in_line(line))
    return word_count_in_each_line

def count_words(lines):
    words_count = 0
    for line in lines:
        words_count += count_words_in_line(line)
    return words_count

def lines_to_characters(lines):
    chars = [char for line in lines for word in line.strip("\n") for char in word if char.isalpha()]
    return chars

def count_alphabets(lines):
    alphabets_count = lines_to_characters(lines)
    return len(alphabets_count)

def count_each_alphabets(lines):
    each_alphabet_count = {}
    chars = lines_to_characters(lines)
    for char in chars:
        if char.isalpha():
            if char.lower() in each_alphabet_count.keys():
                each_alphabet_count[char.lower()] += 1
            else:
                each_alphabet_count[char.lower()] = 1
    return each_alphabet_count

try:
    f = open("file.txt",'r')
    lines = f.readlines()
    print_list = []

    print_list.append(count_lines(lines))
    print_list.append(count_characters(lines))
    print_list.append(count_spaces(lines))
    print_list.append(count_words(lines))
    print_list.append(count_words_in_each_line(lines))
    print_list.append(count_alphabets(lines))
    print_list.append(count_each_alphabets(lines))


    f.close()
    
except FileNotFoundError:
    print("File not found")
