'''
    All the function definitions are placed in the following module
'''
import file_details as fd

try:
    f = open("sample.txt", 'r')
    lines = f.readlines()
    f.close()

    # List used to hold all the information
    print_list = []

    # Calling each function from file_details module and appending the print_list
    print_list.append(fd.count_lines(lines))
    print_list.append(fd.count_characters(lines))
    print_list.append(fd.count_spaces(lines))
    print_list.append(fd.count_words(lines))
    print_list.append(fd.count_words_in_each_line(lines))
    print_list.append(fd.count_alphabets(lines))
    print_list.append(fd.count_each_alphabets(lines))
    print_list.append(fd.count_total_numbers(lines))
    print_list.append(fd.count_each_number(lines))
    print_list.append(fd.count_total_special_chars(lines))
    print_list.append(fd.count_each_special_char(lines))

    # Writing the print_list to screen and file
    fd.write_to_screen(print_list)
    fd.write_to_file(print_list, "sample_info.txt")

# Catching file not found exception
except FileNotFoundError:
    print("File not found")
