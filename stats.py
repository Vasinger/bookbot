def get_word_count(text):
    words = text.split()
    return len(words)

def get_characters_count(text):
    book = text.lower()
    char = {}
    for c in book:
        if c in char:
            char[c] += 1
        else:
            char[c] = 1
    return char

def get_sorted_list(dict):
    l = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    return l