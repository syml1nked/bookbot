from stats import get_num_words, get_num_chars, get_sorted_list_of_chars

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")

    book_word_count = get_num_words(book_path)

    print("----------- Word Count ----------")
    print(f"Found {book_word_count} total words")

    print("--------- Character Count -------")

    book_char_count = get_num_chars(book_path)
    sorted_char_list = get_sorted_list_of_chars(book_char_count)
    for i in sorted_char_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
