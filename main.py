from stats import chars_dict_to_sorted_list, get_chars_dict, get_num_words
import sys

print("hello")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

#the above is setting up the agruments and the book path using an import "sys"



def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def print_report(get_num_words,chars_dict_to_sorted_list,get_chars_dict):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in chars_sorted_list:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")


print_report(get_num_words,chars_dict_to_sorted_list,get_chars_dict)