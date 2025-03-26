from stats import count_words
from stats import count_characters
from stats import sort_by_occurences

BOOK_TO_READ = "./books/frankenstein.txt"

def main():
    book_text = get_book_text(BOOK_TO_READ)

    num_words = count_words(book_text)
    num_characters = count_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for pair in sort_by_occurences(num_characters):
        if pair["character"].isalpha():
            print(f"{pair["character"]}: {pair["count"]}")

    print("============= END ===============")

def get_book_text(path):
    text = ""
    with open(path) as f:
        text = f.read()
    
    return text

main()