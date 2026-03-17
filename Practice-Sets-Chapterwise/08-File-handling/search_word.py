import sys

if len(sys.argv) != 3:
    print("Usage: python search_word.py <filename> <word>")
    sys.exit(1)

filename = sys.argv[1]
search_word = sys.argv[2].lower()

count = 0

try:
    with open(filename, "r") as file:
        for line in file:
            words = line.lower().split()
            count += words.count(search_word)

    print(f'"{search_word}" appears {count} times in {filename}')

except FileNotFoundError:
    print("Error: File not found.")