# --- Import functions from stats.py
from stats import get_word_count, get_character_counts, get_sorted_list_of_dicts
import sys

# --- Define function to get the contents of a book from it's file path ---
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

# --- Define a function to print the report of the character counts ---
def print_sorted_dict_list(file_path, word_count, sorted_list_of_dicts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each key-value pair in the sorted list of dictionaries
    for dictionary in sorted_list_of_dicts:
        if not dictionary["char"].isalpha():
            continue
        print(f"{dictionary["char"]}: {dictionary["num"]}")

    print("============= END ===============")


# --- Define Main ---
def main():
    # Validation - Check if sys.argv has two entries
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file_path = sys.argv[1]
    # 1. Print the contents of the book
    book_contents = get_book_text(book_file_path)
    # print(book_contents)

    # 2. Print the word count of the book
    word_count = get_word_count(book_contents)
    print(f"Found {word_count} total words")

    # 3. Capture and print the dictionary of characters and their counts
    character_counts_dict = get_character_counts(book_contents)
    print(character_counts_dict)

    # 4. Print the report of the characters and their counts, sorted
    sorted_list_of_dicts = get_sorted_list_of_dicts(character_counts_dict)
    print_sorted_dict_list(book_file_path, word_count, sorted_list_of_dicts)

# --- Call Main ---
if __name__ == "__main__":
    main()
