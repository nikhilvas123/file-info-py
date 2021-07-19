'''
    OrderedDict is used from collections to sort the dictionary
'''
import collections

def count_lines(lines):
    ''' Returns the number of lines '''
    return len(lines)

def count_characters(lines):
    ''' Returns the total number of characters'''
    ch_count = sum([len(line.strip("\n")) for line in lines])
    return ch_count

def count_spaces(lines):
    ''' Returns the number of spaces '''
    space_count = 0
    for line in lines:
        space_count += line.count(" ")
    return space_count

def count_words_in_line(line):
    ''' Returns the number of words in a line '''
    return len(line.strip("\n").split(" "))

def count_words_in_each_line(lines):
    ''' Returns the number of words in each line '''
    word_count_in_each_line = []
    for line in lines:
        word_count_in_each_line.append(count_words_in_line(line))
    return word_count_in_each_line

def count_words(lines):
    ''' Returns the total number of words'''
    words_count = 0
    for line in lines:
        words_count += count_words_in_line(line)
    return words_count

def lines_to_characters(lines):
    ''' Flattens the list to have characters'''
    chars = [char for line in lines for word in line.strip("\n") for char in word]
    return chars

def count_alphabets(lines):
    ''' Returns the total number of alphabets '''
    alphabets_count = lines_to_characters(lines)
    return len([c for c in alphabets_count if c.isalpha()])

def count_each_alphabets(lines):
    ''' Returns the number of each alphabet '''
    each_alphabet_count = {}
    chars = lines_to_characters(lines)
    for char in chars:
        if char.isalpha():
            if char.lower() in each_alphabet_count.keys():
                each_alphabet_count[char.lower()] += 1
            else:
                each_alphabet_count[char.lower()] = 1
    return collections.OrderedDict(sorted(each_alphabet_count.items()))

def count_total_numbers(lines):
    ''' Returns the total count of numbers '''
    chars = lines_to_characters(lines)
    total_numbers_count = len([char for char in chars if char.isnumeric()])
    return total_numbers_count

def count_each_number(lines):
    ''' Returns the count of each number '''
    chars = lines_to_characters(lines)
    each_number_count = {}
    for char in chars:
        if char.isnumeric():
            if char in each_number_count.keys():
                each_number_count[char] += 1
            else:
                each_number_count[char] = 1
    return collections.OrderedDict(sorted(each_number_count.items()))

def count_total_special_chars(lines):
    ''' Returns the number of special characters '''
    total_special_chars_count = 0
    chars = lines_to_characters(lines)
    total_special_chars_count = len([char for char in chars \
    if not (char.isnumeric() or char.isalpha() or char == " ")])
    return total_special_chars_count

def count_each_special_char(lines):
    ''' Returns the number of each special character '''
    chars = lines_to_characters(lines)
    each_special_char_count = {}
    for char in chars:
        if not (char.isnumeric() or char.isalpha() or char == " "):
            if char in each_special_char_count.keys():
                each_special_char_count[char] += 1
            else:
                each_special_char_count[char] = 1
    return collections.OrderedDict(sorted(each_special_char_count.items()))

def write_to_screen(print_list):
    ''' Writes print_list to screen'''
    print("The File Details are:")
    print("The number of lines: %d" %(print_list[0]))
    print("The total number of characters: %d" %(print_list[1]))
    print("The total number of spaces: %d" %(print_list[2]))
    print("The total number of words: %d" %(print_list[3]))

    for line_no, count in enumerate(print_list[4]):
        print("Number of words in line %d: %d" %(line_no + 1, count))

    print("The total number of alphabets: %d" %(print_list[5]))
    print("The frequency of alphabets:")

    for alpha, count in print_list[6].items():
        print("%c: %d" %(alpha, count), end="  ")

    print("\nThe total number of numbers: %d" %(print_list[7]))
    print("The frequency of numbers:")

    for num, count in print_list[8].items():
        print("%c: %d" %(num, count), end="  ")

    print("\nThe total number of special characters: %d" %(print_list[9]))
    print("The frequency of special characters:")

    for s_char, count in print_list[10].items():
        print("%c: %d" %(s_char, count), end="  ")
    print()

def write_to_file(print_list, file_name):
    ''' Writes print_list to file '''
    with open(file_name, 'w') as f:
        f.write("The File Details are:\n")
        f.write("The number of lines: %d\n" %(print_list[0]))
        f.write("The total number of characters: %d\n" %(print_list[1]))
        f.write("The total number of spaces: %d\n" %(print_list[2]))
        f.write("The total number of words: %d\n" %(print_list[3]))

        for line_no, count in enumerate(print_list[4]):
            f.write("Number of words in line %d: %d\n" %(line_no + 1, count))

        f.write("The total number of alphabets: %d\n" %(print_list[5]))
        f.write("The frequency of alphabets:\n")

        for alpha, count in print_list[6].items():
            f.write("%c: %d  " %(alpha, count))

        f.write("\nThe total number of numbers: %d\n" %(print_list[7]))
        f.write("The frequency of numbers:\n")

        for num, count in print_list[8].items():
            f.write("%c: %d  " %(num, count))

        f.write("\nThe total number of special characters: %d\n" %(print_list[9]))
        f.write("The frequency of special characters:\n")

        for s_char, count in print_list[10].items():
            f.write("%c: %d" %(s_char, count))