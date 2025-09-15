#!/usr/sbin/python3

import sys
from stats import count_words, get_char_dict, sort_dict

def get_book_text( filepath ):
    with open(filepath, encoding='utf-8-sig') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    char_list = sort_dict(get_char_dict(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item["char"]}: {item["num"]}")
    print("---------------------------------")

if __name__ == "__main__":
    main()
