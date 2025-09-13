def get_book_contents(filepath) -> str:
    with open(filepath) as f:
        book_contents = f.read()

        return book_contents

def get_num_words(filepath) -> int:
    book_contents = get_book_contents(filepath)
    num_words = len(book_contents.split())

    return num_words

def get_num_chars(filepath) -> int:
    book_contents = get_book_contents(filepath)
    chars_count = {}
    for char in book_contents:
        char = char.lower()
        if char not in chars_count:
            chars_count[char] = 1
        else:
            chars_count[char] = chars_count[char] + 1

    return chars_count

def sort_on(items):
    return items["num"]

def get_sorted_list_of_chars(chars_count):
    char_list = []
    for k,v in chars_count.items():
        char_list.append({"char": k, "num": v})

    char_list.sort(reverse=True, key=sort_on)

    return char_list

