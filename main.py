from stats import count_words

BOOK_TO_READ = "./books/frankenstein.txt"

def main():
    num_words = count_words(get_book_text(BOOK_TO_READ))
    print(f"{num_words} words found in the document")

def get_book_text(path):
    text = ""
    with open(path) as f:
        text = f.read()
    
    return text

main()