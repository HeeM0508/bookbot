def main(): 
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = words_count(text)
    print (f"Found {count} total words")  

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def words_count(text):
    num_words = len(text.split())
    return num_words

main()
