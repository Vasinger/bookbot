from stats import get_characters_count, get_word_count, get_sorted_list
import sys

#sys.exit("Usage: python3 main.py <path_to_book>")


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    count = get_word_count(get_book_text(path))
    char = get_characters_count(get_book_text(path))
    format = get_sorted_list(char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in format:
        c = i[0]
        if c.isalpha():
            print(f"{i[0]}: {i[1]}")
    print("============= END ===============")

main()