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

def sort_on(items):
    return items["num"]

def get_sorted_counts(char_counts):
    unsorted = []
    for char, count in char_counts.items():
        unsorted.append({
            "char": char,
            "num": count,
        })
    unsorted.sort(reverse=True, key=sort_on)
    return unsorted