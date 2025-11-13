# --- [Stats] Define a function to get the length of the book ---
def get_word_count(book_contents):
    return len(book_contents.split())

# --- [Stats] Count Characters ---
def get_character_counts(book_contents):
    # Initialize the dictionary of character counts
    # i.e.,
    # character_counts = {
    # character: count,
    # 'a': 1
    # }
    character_counts = {}

    # Get the individual words of the book (make sure to lowercase the book contents)
    individual_words = book_contents.lower().split()

    # Iterate through each word in the contents of the book
    for word in individual_words:
        for character in word:
            if character not in character_counts:
                character_counts[character] = 1
            else:
                character_counts[character] += 1

    return character_counts

# --- [Stats] Generate a List of Dinctionaries
# First, define a helper function to sort the list of dictionaries
def sort_on(items):
    return items["num"]

def get_sorted_list_of_dicts(character_counts_dict):
    # Initialize a new list that we will add dinctionaries too
    list_of_dicts = []

    # Add the character_count dictionary contents to the new dictionary
    # character_count dictionary: {character: count}
    for character, count in character_counts_dict.items():
        list_of_dicts.append({"char": character, "num": count})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

