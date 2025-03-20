from stats import get_num_words, get_char_dict, sort_dict

def get_book_text(filepath: str) -> str:
    try: 
        with open(filepath) as f:
            text = f.read()
    except:
        text = "Error reading file"
    return text


def main():
    print("============ BOOKBOT ============")
    book_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    chars = get_char_dict(text)
    sorted_chars = sort_dict(chars)
    print("--------- Character Count -------")
    for item in sorted_chars:
        key = list(item.keys())[0]
        if key.isalpha():
            print(f"{key}: {item[key]}")
    print("============= END ===============")


main()
