from stats import count_words
from stats import count_chars

def main():
    path = "books/frankenstein.txt"
    print( f"{count_words(path)} words found in the document" )
    print( f"{count_chars(path)} characters found in the document.")


if __name__ == "__main__":
    main()
