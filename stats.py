def get_book_text(filepath):
    try:
        with open(filepath) as file:
            return file.read()
    except:
        print("failed in get_book_text")

def get_word_count(book_text):
    num_words = book_text.split()
    return len(num_words)

def count_chars(book_text):
    char_count = {}
    lower_text = book_text.lower()
    for char in lower_text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_char_count(char_count):
    get_sorted = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    get_dict = dict(get_sorted)
    return get_dict
