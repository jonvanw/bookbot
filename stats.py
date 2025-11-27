def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    dict = {}
    for c in text.lower():
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
    return dict