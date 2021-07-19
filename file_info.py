import collections

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
    chars = [char for line in lines for word in line.strip("\n") for char in word]
    return chars

def count_alphabets(lines):
    alphabets_count = lines_to_characters(lines)
    # print(len([c for c in alphabets_count if c.isalpha()]))
    return len([c for c in alphabets_count if c.isalpha()])

def count_each_alphabets(lines):
    each_alphabet_count = {}
    chars = lines_to_characters(lines)
    for char in chars:
        if char.isalpha():
            if char.lower() in each_alphabet_count.keys():
                each_alphabet_count[char.lower()] += 1
            else:
                each_alphabet_count[char.lower()] = 1
    # print(collections.OrderedDict(sorted(each_alphabet_count.items())))
    return collections.OrderedDict(sorted(each_alphabet_count.items()))

def count_total_numbers(lines):
    chars  = lines_to_characters(lines)
    total_numbers_count = len([char for char in chars if char.isnumeric()])
    # print(total_numbers_count)
    return total_numbers_count

def count_each_number(lines):
    chars = lines_to_characters(lines)
    each_number_count = {}
    for char in chars:
        if char.isnumeric():
            if char in each_number_count.keys():
                each_number_count[char] += 1
            else:
                each_number_count[char] = 1
    # print(collections.OrderedDict(sorted(each_number_count.items())))
    return collections.OrderedDict(sorted(each_number_count.items()))

def count_total_special_chars(lines):
    total_special_chars_count = 0
    chars = lines_to_characters(lines)
    total_special_chars_count = len([char for char in chars if not (char.isnumeric() or char.isalpha() or char == " ")])
    # print(total_special_chars_count)
    return total_special_chars_count

def count_each_special_char(lines):
    chars = lines_to_characters(lines)
    each_special_char_count = {}
    for char in chars:
        if not (char.isnumeric() or char.isalpha() or char == " "):
            if char in each_special_char_count.keys():
                each_special_char_count[char] += 1
            else:
                each_special_char_count[char] = 1
    # print(collections.OrderedDict(sorted(each_special_char_count.items())))
    return collections.OrderedDict(sorted(each_special_char_count.items()))

def write_to_screen(print_list):
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
        print("%c: %d" %(alpha,count),end="  ")

    print("\nThe total number of numbers: %d" %(print_list[7]))
    print("The frequency of numbers:")

    for num, count in print_list[8].items():
        print("%c: %d" %(num,count),end="  ")

    print("\nThe total number of special characters: %d" %(print_list[9]))
    print("The frequency of special characters:")

    for s_char, count in print_list[10].items():
        print("%c: %d" %(s_char,count),end="  ")
    print()

def write_to_file(print_list,file_name):
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
            f.write("%c: %d  " %(alpha,count))

        f.write("\nThe total number of numbers: %d\n" %(print_list[7]))
        f.write("The frequency of numbers:\n")

        for num, count in print_list[8].items():
            f.write("%c: %d  " %(num,count))

        f.write("\nThe total number of special characters: %d\n" %(print_list[9]))
        f.write("The frequency of special characters:\n")

        for s_char, count in print_list[10].items():
            f.write("%c: %d  " %(s_char,count))

try:
    f = open("sample.txt",'r')
    lines = f.readlines()
    f.close()

    print_list = []

    print_list.append(count_lines(lines))
    print_list.append(count_characters(lines))
    print_list.append(count_spaces(lines))
    print_list.append(count_words(lines))
    print_list.append(count_words_in_each_line(lines))
    print_list.append(count_alphabets(lines))
    print_list.append(count_each_alphabets(lines))
    print_list.append(count_total_numbers(lines))
    print_list.append(count_each_number(lines))
    print_list.append(count_total_special_chars(lines))
    print_list.append(count_each_special_char(lines))
    

    write_to_screen(print_list)
    write_to_file(print_list,"sample_info.txt")
    
except FileNotFoundError:
    print("File not found")
