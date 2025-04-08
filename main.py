from stats import get_characters_count, get_word_count, get_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    count = get_word_count(get_book_text("./books/frankenstein.txt"))
    char = get_characters_count(get_book_text("./books/frankenstein.txt"))
    format = get_sorted_list(char)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in format:
        c = i[0]
        if c.isalpha():
            print(f"{i[0]}: {i[1]}")
    print("============= END ===============")

main()