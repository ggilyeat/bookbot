def get_book_text( filepath ):
    with open(filepath) as f:
        return f.read()

def count_words(filepath):
    return len(get_book_text(filepath).split())
