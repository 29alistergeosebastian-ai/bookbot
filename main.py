from stats import chars_dict_to_sorted_list, get_chars_dict, get_num_words


def main() -> None:
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print(f"Found {num_words} total words")
    for item in chars_sorted_list:
        print(item)


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def print_report(get_num_words,chars_dict_to_sorted_list,get_chars_dict):
    book_path = "books/frankenstein.txt"
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
