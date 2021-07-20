import file_details as fd
import collections

file_list = []

with open("sample.txt",'r') as f:
    file_list = f.readlines()
print(file_list)

def test_count_lines():
    assert fd.count_lines(["hello\n", "123"]) == 2
    assert fd.count_lines(file_list) == 3

def test_count_characters():
    assert fd.count_characters(["1234567\n", "891234\n\n", "23567"]) == 18
    assert fd.count_characters(file_list) == 73

def test_count_spaces():
    assert fd.count_spaces("If I am student, I don't need to study") == 8
    assert fd.count_spaces(file_list) == 14

def test_count_words_in_line():
    assert fd.count_words_in_line("I am the universe.") == 4
    assert fd.count_words_in_line(file_list[0]) == 4

def test_count_words_in_each_line():
    assert fd.count_words_in_each_line(["Don't study engineering\n", "You will regret it"]) == [3, 4]
    assert fd.count_words_in_each_line(file_list) == [4, 8, 5]

def test_count_words():
    assert fd.count_words(["What will happen tomorrow?\n", "You never know"]) == 7      
    assert fd.count_words(file_list) == 17

def test_lines_to_characters():
    assert fd.lines_to_characters(["Good morning"]) == ['G','o','o','d',' ','m','o','r','n','i','n','g']

def test_count_alphabets():
    assert fd.count_alphabets(["Good evening\n"," 123 How are you?"]) == 20
    assert fd.count_alphabets(file_list) == 53

def test_count_each_alphabets():
    assert fd.count_each_alphabets(["ababcd"]) == {'a':2, 'b':2, 'c':1, 'd':1}

def test_count_total_numbers():
    assert fd.count_total_numbers(["12345\n", "6789"]) == 9
    assert fd.count_total_numbers(file_list) == 1

def test_count_each_number():
    assert fd.count_each_number(["12345\n", "HI"]) == {'1' : 1, '2' : 1, '3' : 1, '4' : 1, '5' : 1}
    assert fd.count_each_number(file_list) == {'6' : 1}

def test_count_total_special_chars():
    assert fd.count_total_special_chars([",.!@#$%^&"]) == 9
    assert fd.count_total_special_chars(file_list) == 5

def test_count_each_special_char():
    assert fd.count_each_special_char(["nikhil_123@gmail.com"]) == {'_' : 1, '@' : 1, '.' : 1}
    assert fd.count_each_special_char(file_list) == {',': 2, '?': 3}