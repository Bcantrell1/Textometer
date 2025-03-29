import sys
from stats import get_book_text
from stats import get_word_count
from stats import count_chars
from stats import sort_char_count

def main():
    # book_title = "./books/frankenstein.txt"
    if len(sys.argv) == 2:
        book_text = get_book_text(sys.argv[1])
        word_counts = get_word_count(book_text)
        char_counter = count_chars(book_text)
        sorted_chars = sort_char_count(char_counter)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_counts} total words")
        print("--------- Character Count -------")
        for key, value in sorted_chars.items():
            print(f"{key}: {value}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()
