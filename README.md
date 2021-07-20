# This simple python program prints the file info on console and also redirects to a file.

## Usage
```
python3 file_info.py
```
## Files
### file_info.py
This is the main logic file. It imports file_details and uses its functions. The output is printed on screen and also redirected to a file.

### file_details.py
This is the core logic file. It implements all the functions necessary to obatin file details.

### test_file_info.py
This is a program to test the functions of file_details

### sample.txt
This is input to the file_info program, this contains sample text to test the validity.

## Output
The output of sample.txt file is 
```
The File Details are:
The number of lines: 3
The total number of characters: 73
The total number of spaces: 14
The total number of words: 17
Number of words in line 1: 4
Number of words in line 2: 8
Number of words in line 3: 5
The total number of alphabets: 53
The frequency of alphabets:
a: 4  b: 1  d: 1  e: 6  f: 2  g: 1  h: 3  i: 5  l: 2  m: 3  n: 3  o: 7  r: 4  s: 1  t: 1  u: 3  v: 1  w: 2  y: 3  
The total number of numbers: 1
The frequency of numbers:
6: 1  
The total number of special characters: 5
The frequency of special characters:
,: 2?: 3
```