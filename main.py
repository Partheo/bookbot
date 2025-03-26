import sys
from stats import count_words
from stats import count_characters
from stats import sort_by_occurences

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    book_text = get_book_text("./" + path_to_book)

    num_words = count_words(book_text)
    num_characters = count_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
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