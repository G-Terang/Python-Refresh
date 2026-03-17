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

import argparse

parser = argparse.ArgumentParser(description = "This is a simple command line")
parser.add_argument("file_name", help="The file to process.")

args = parser.parse_args()
try:
    with open(args.file_name, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")
except FileNotFoundError as file_not_found:
    print(f"Error occurred: {file_not_found}")