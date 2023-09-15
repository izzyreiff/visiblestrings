import os
import re

# Reads file from @file_path and returns cleaned content of file (removes punctuation, line breaks, and makes lowercase)
def read_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            # Remove punctuation, convert to lowercase, and remove line breaks
            cleaned_content = re.sub(r'[^\w\s]', '', content).lower().replace('\n', ' ')
            return cleaned_content
    except FileNotFoundError:
        return None

# Sends filename to read_file_content to be read and cleaned up, then sends to first_letters to be shortened only to first letters with no spaces
def magic_cleanup(filename):
    # Example usage:
    songs_folder = "songs"
    file_name = filename
    file_path = os.path.join(songs_folder, file_name)
    cleaned_content = read_file_content(file_path)
    if cleaned_content is not None:
        return first_letters(cleaned_content)
    else:
        print(f"File {file_name} not found or unable to read.")
        return None

# Helper function that takes input and returns only the first letter of each word with spaces removed
def first_letters(content):
    # Split the content into words using spaces as the separator
    words = content.split()
    # Extract the first letter of each word and join them
    first_letters = ''.join(word[0] for word in words)
    return first_letters

# Helper function that returns true if shorter_string appears in longer_string, or else returns false
def contains_substring(longer_string, shorter_string):
    return shorter_string in longer_string

def find_matching_initial_letters(input_string, dictionary):
    # Initialize an empty list to store matching entries
    matching_entries = []
    # Convert the input string to lowercase for case-insensitive matching
    cleaned_input = re.sub(r'[^\w]', '', input_string).lower()
    # Iterate through the dictionary entries
    for title, file_name in dictionary.items():
        lyrics = magic_cleanup(file_name)
        if lyrics is not None:
            if contains_substring(lyrics, cleaned_input):
                matching_entries.append(title)
    return matching_entries

if __name__ == "__main__":
    # Get user input
    input_string = input("Enter a string of initial letters: ")

    # Define the dictionary with word mappings to file names
    debut = {
        "Tim McGraw": "1_1.txt",
        "Picture To Burn": "1_2.txt",
        "Teardrops on My Guitar": "1_3.txt",
        "A Place In This World": "1_4.txt",
        "Cold As You": "1_5.txt"
    }

    # Find matching entries
    matching_entries = find_matching_initial_letters(input_string, debut)

    if matching_entries:
        print(f"Songs containing '{input_string}':")
        print(", ".join(matching_entries))
    else:
        print(f"No entries found containing '{input_string}'. Try removing a letter from the beginning or end, and try again!")
