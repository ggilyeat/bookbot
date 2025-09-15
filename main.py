#!/usr/sbin/python3

from stats import count_words, get_char_dict, sort_dict

def get_book_text( filepath ):
    with open(filepath, encoding='utf-8-sig') as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    char_list = sort_dict(get_char_dict(text))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    for item in char_list:
        print(f"{item["char"]}: {item["num"]}")

if __name__ == "__main__":
    main()
