def count_words(text):
    return len(text.split())

def count_characters(text):
    character_occurences = {}
    for char in text.lower():
        if char not in character_occurences:
            character_occurences[char] = 1
            continue
        character_occurences[char] += 1

    return character_occurences

def sort_by_occurences(dict):
    character_counts = []
    for char in dict:
        pair = {"character": char, "count": dict[char]}
        character_counts.append(pair)

    character_counts.sort(reverse=True, key=sort_on)

    return character_counts

def sort_on(dict):
    return dict["count"]