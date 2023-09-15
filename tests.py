from flask import Flask, request, jsonify, render_template
import os
import re

app = Flask(__name__)

# Define your dictionary and functions here
debut = {
    "Tim McGraw": "1_1.txt",
    "Picture To Burn": "1_2.txt",
    "Teardrops on My Guitar": "1_3.txt",
    "A Place In This World": "1_4.txt",
    "Cold As You": "1_5.txt"
}

def read_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            cleaned_content = re.sub(r'[^\w\s]', '', content).lower().replace('\n', ' ')
            return cleaned_content
    except FileNotFoundError:
        return None

def magic_cleanup(filename):
    songs_folder = "songs"
    file_name = filename
    file_path = os.path.join(songs_folder, file_name)
    cleaned_content = read_file_content(file_path)
    if cleaned_content is not None:
        return first_letters(cleaned_content)
    else:
        print(f"File {file_name} not found or unable to read.")
        return None

def first_letters(content):
    words = content.split()
    first_letters = ''.join(word[0] for word in words)
    return first_letters

def contains_substring(longer_string, shorter_string):
    return shorter_string in longer_string

def find_matching_initial_letters(input_string, dictionary):
    matching_entries = []
    cleaned_input = re.sub(r'[^\w]', '', input_string).lower()
    for title, file_name in dictionary.items():
        lyrics = magic_cleanup(file_name)
        if lyrics is not None:
            if contains_substring(lyrics, cleaned_input):
                matching_entries.append(title)
    return matching_entries

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('userInput', '')
    matching_entries = find_matching_initial_letters(user_input, debut)
    result = f"Songs containing '{user_input}': " + ", ".join(matching_entries) if matching_entries else f"No entries found containing '{user_input}'"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
