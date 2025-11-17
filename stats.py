def get_words_count(text):
    words = text.split()
    return len(words)

def get_characters_number(text):
    characters_count = {}
    for character in text.lower(): 
        if character in characters_count:
            characters_count [character] += 1
        else:
            characters_count [character] = 1
    return characters_count

