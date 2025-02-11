import requests
import pandas as pd
import json
import config

# Use the deck name from config
deck_name = config.DECK_NAME

# Set the AnkiConnect URL
anki_url = 'http://localhost:8765'

# Load the final.csv file
df = pd.read_csv('final.csv')

# Normalize the columns
df['polish_normalized'] = df['polish'].str.lower().str.strip()
df['english_normalized'] = df['english'].str.lower().str.strip()

# Function to add a note to Anki
def add_to_anki(polish_word, english_word, deck_name=deck_name):
    note = {
        'deckName': deck_name,
        'modelName': 'Basic',  # Standard card type
        'fields': {
            'Front': polish_word,
            'Back': english_word
        },
        'tags': [],
        'options': {
            'allowDuplicate': False  # Prevent adding duplicates
        }
    }

    # Send the request to AnkiConnect
    response = requests.post(anki_url, json.dumps({
        'action': 'addNote',
        'version': 6,
        'params': {'note': note}
    }))

    return response.json()  # Return the response for debugging


# Loop through the dataframe and add words to Anki
for index, row in df.iterrows():
    polish_word = row['polish_normalized']
    english_word = row['english_normalized']
    result = add_to_anki(polish_word, english_word)
    print(f"Added: {polish_word} - {english_word}, Result: {result}")
