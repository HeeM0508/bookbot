from stats import get_words_count, get_characters_number


def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_words_count(text)
    characters_count = get_characters_number(text)
    print (f"Found {count} total words")  
    print (f"{characters_count}")

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()
    
main()
