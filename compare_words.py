# import pandas as pd
#
# # Load necessary columns
# new_words_df = pd.read_csv('new_words_filtered.csv')
# sheety_order_df = pd.read_csv('sheety_order.csv')
#
# # Normalize data to ensure proper matching
# new_words_df['New_Word'] = new_words_df['New_Word'].str.strip().str.lower()
# sheety_order_df['TranslPL'] = sheety_order_df['TranslPL'].str.strip().str.lower()
#
# matched_rows = []
#
# # Simple iteration approach to find matches
# for word in new_words_df['New_Word']:
#     if word in sheety_order_df['TranslPL'].values:
#         matched_rows.append(word)
#
# # Filter matching rows from sheety_order_df
# filtered_df = sheety_order_df[sheety_order_df['TranslPL'].isin(matched_rows)]
# filtered_df.to_csv("new_words_filtered.csv", index=False)
# print("Matching words saved to 'new_words_filtered.csv'.")

#

#


import pandas as pd

# Load the CSV files
sheety_df = pd.read_csv("sheety_pl.csv")  # Contains 'polish' column (words)
anki_df = pd.read_csv("fromAnkiPl.csv")  # Contains 'Front' column (sentences)

# Normalize text (strip spaces and lowercase) and handle NaN values
sheety_df["polish"] = sheety_df["polish"].astype(str).str.strip().str.lower()
anki_df["Front"] = anki_df["Front"].astype(str).str.strip().str.lower()

# Function to check if a word appears in any sentence
def word_in_sentences(word, sentences):
    return any(word in sentence for sentence in sentences if isinstance(sentence, str))

# Filter words that are NOT found in any sentence from Anki
filtered_words = [word for word in sheety_df["polish"] if not word_in_sentences(word, anki_df["Front"].dropna())]

# Convert to DataFrame and save to CSV
filtered_df = pd.DataFrame(filtered_words, columns=["polish"])
filtered_df.to_csv("new_words.csv", index=False)

print("Filtered words saved to 'new_words.csv'.")


