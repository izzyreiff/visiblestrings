# Go from initial songs.csv spreadsheet to cleaned Lyrics column with only first letters
import pandas as pd
import re

# Replace 'input_file.csv' with the path to your input CSV file
input_file = 'songs.csv'

# Replace 'output_file.csv' with the path where you want to save the modified CSV file
output_file = 'clean.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# Define a function to remove text within brackets
def remove_text_within_brackets(text):
    return re.sub(r'\[.*?\]', '', text)

def remove_text_within_brackets_and_parentheses(text):
    # Remove text within square brackets and parentheses
    cleaned_text = re.sub(r'[\[\(].*?[\]\)]', '', text)
    return cleaned_text

def clean_text(text):
    cleaned_content = re.sub(r'[^\w\s]', '', text).lower().replace('\n', ' ')
    return cleaned_content

def first_letters(text):
    words = text.split()
    first_letters = ''.join(word[0] for word in words)
    return first_letters

# Apply the function to the specified columns (e.g., 'column_name')
df['Lyrics'] = df['Lyrics'].apply(remove_text_within_brackets)
df['Lyrics'] = df['Lyrics'].apply(clean_text)
df['Lyrics'] = df['Lyrics'].apply(first_letters)

# Copy the content of the first column into a new fourth column
df['TitlesCleaned'] = df.iloc[:, 0]
df['TitlesCleaned'] = df['TitlesCleaned'].apply(remove_text_within_brackets_and_parentheses)
df['TitlesCleaned'] = df['TitlesCleaned'].apply(clean_text)
df['TitlesCleaned'] = df['TitlesCleaned'].apply(first_letters)

# Save the modified DataFrame to a new CSV file
df.to_csv(output_file, index=False)
