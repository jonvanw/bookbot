from stats import get_num_words, get_char_counts, get_sorted_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_char_counts(sorted_counts):
    for cc in sorted_counts:
        if cc["char"].isalpha():
            print(f"{cc["char"]}: {cc["num"]}")
    
def main():
    file_path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    contents = get_book_text(file_path)

    wc = get_num_words(contents)
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")

    char_counts = get_char_counts(contents)
    sorted_counts = get_sorted_counts(char_counts)
    print("--------- Character Count -------")
    print_char_counts(sorted_counts)
    
    print("============= END ===============")
    
main()