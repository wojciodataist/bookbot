import sys

from stats import num_of_words, count_characters, char_occurence


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return str(file_contents)


# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


# Get the filepath from command line arguments
filepath = sys.argv[1]


text = get_book_text(filepath)
word_count = num_of_words(text)
print(f"Found {word_count} total words")

char_num = count_characters(text)

for char in char_occurence(char_num):
    if char["char"].isalpha() == True:
        print(f'{char["char"]}: {char["num"]}')
