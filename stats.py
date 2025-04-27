def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return str(file_contents)


def num_of_words(text):
    num_words = len(text.split())
    return num_words


def count_characters(text):
    letter_count = {}
    for char in text:
        char = char.lower()
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count


def sort_on(dict):
    return dict["num"]


def char_occurence(char_dict):
    chars = []
    for char in char_dict.items():
        letter, count = char
        d = {"char": letter, "num": count}
        chars.append(d)
    chars.sort(reverse=True, key=sort_on)
    return chars
