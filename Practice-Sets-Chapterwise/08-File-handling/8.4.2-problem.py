'''
4. Creating Command Line Utilities
    1.  Write a small script count_lines.py that takes a filename as input and prints
        how many lines are in the file.
        Example usage:
            python count_lines.py tasks.txt
            # Output: Number of lines: 4
            
    2.  Write a command-line utility search_word.py that takes two arguments:
        A filename
        A word to search and prints how many times the word appears in the file.

'''


'''
import argparse

parser = argparse.ArgumentParser(description="Search for a word to count its occurences in a file")
parser.add_argument('file_name', help="Path to the file to search in")
parser.add_argument('the_word', help="The word to search")

args = parser.parse_args()
file_name = args.file_name
searh_word = args.the_word.lower()

count = 0

try:
    with open("file_name", "r") as file:
        for line in file:
            words = line.lower.split()
            count += words.count("search_word")
        print(f'"search_word" appears {count} times in the file {file_name}')
except FileNotFoundError as Error:
    print(f"File does not exist!, {Error}")
    
    
'''


# using argparse

import argparse

parser = argparse.ArgumentParser(description="Search for a word in a file and count its occurrences.")

parser.add_argument("filename", help="Path to the file to search in")
parser.add_argument("word", help="Word to search for")

args = parser.parse_args()

filename = args.filename
search_word = args.word.lower()

count = 0

try:
    with open(filename, "r") as file:
        for line in file:
            words = line.lower().split()
            count += words.count(search_word)

    print(f'"{args.word}" appears {count} times in {filename}')

except FileNotFoundError:
    print("Error: File not found.")