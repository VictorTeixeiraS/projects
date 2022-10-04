book_path = "books/frankenstein.txt"


def main():
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(book_path) as f:
        return f.read()


main()
