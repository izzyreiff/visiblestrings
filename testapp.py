from flask import Flask, request, jsonify, render_template
import os
import re
import pandas as pd

app = Flask(__name__)

# file_path refers to the csv file that holds all songs
file_path = 'clean.csv'
# Read the csv file into a DataFrame, try and catch reading errors
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: There was an issue parsing the CSV file '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

def find_matching_initial_letters(input_string):
    matching_entries = []
    cleaned_input = re.sub(r'[^\w]', '', input_string).lower()
    # Iterate through each row in the "Lyrics" column
    for index, row in df.iterrows():
        lyrics = row['Lyrics']
        title = row['Title']
        # Check if the user input exists within the Lyrics
        if cleaned_input in lyrics:
            matching_entries.append(title)
            print("match")
    return matching_entries

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('userInput', '')
    matching_entries = find_matching_initial_letters(user_input)
    result = f"Songs containing '{user_input}': " + ", ".join(matching_entries) if matching_entries else f"No songs were found containing '{user_input}'. Try removing a letter from the beginning or end, and enter it again!"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
