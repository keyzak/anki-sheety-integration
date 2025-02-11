import requests
import pandas as pd
import re  # Import the re module for regular expressions
import config

# Use the deck name from config
deck_name = config.DECK_NAME

# Send request to AnkiConnect to list all decks
#very importand make sure Anki app , anki for descktop is open ! anki.exe
payload = {"action": "deckNames",
           "version": 6}
response = requests.post("http://127.0.0.1:8765", json=payload).json()



#------------------- Get All Cards from the Deck -------------------
payload = {
    "action": "findCards",
    "version": 6,
    "params": {
        "query": f"deck:{deck_name}"
    }
}

response = requests.post("http://127.0.0.1:8765", json=payload).json()
card_ids = response.get("result", [])

#------------------- Retrieve Card Information -------------------
payload = {
    "action": "cardsInfo",
    "version": 6,
    "params": {
        "cards": card_ids
    }
}

response = requests.post("http://127.0.0.1:8765", json=payload).json()
cards_info = response.get("result", [])

# Extract front and back text from each card
data = []
for card in cards_info:
    front = card['fields']['Front']['value']
    back = card['fields']['Back']['value']
    data.append([front, back])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Front", "Back"])

# Save as CSV
df.to_csv("anki_export.csv", index=False, encoding="utf-8")

# Function to remove HTML tags
def clean_html(text):
    return re.sub(r"<.*?>", "", text)

# Clean the 'Front' column
df_front = pd.read_csv("anki_export.csv", usecols=['Front'])
df_front["Front"] = df_front["Front"].apply(clean_html)
df_front["Front"] = df_front["Front"].apply(lambda x: re.sub(r"\.\.\.", "", x).strip())
df_front["Front"] = df_front["Front"].apply(lambda x: re.sub(r"([a-zżźćńółęąś])([A-Z])", r"\1 \2", x))
df_front["Front"] = df_front["Front"].apply(lambda x: re.sub(r"(?<=[a-z])(?=[A-Z])", " ", x))

# Save cleaned Front column to CSV
df_front.to_csv("fromAnkiPl.csv", index=False)

# Check for successful processing
print("Anki data processed and saved.")
