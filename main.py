from stats import get_num_words, get_char_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    wc = get_num_words(frankenstein)
    print(f"Found {wc} total words")

    char_counts = get_char_counts(frankenstein)
    print("Character counts:")
    print(char_counts)
    # for char, count in char_counts.items():
    #     print(f"'{char}': {count}")


main()