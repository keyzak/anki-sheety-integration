import pandas as pd

# Load the new words and the Sheety data
new_words_df = pd.read_csv('new_words.csv')
sheety_order_df = pd.read_csv('sheety_order.csv')

# Normalize the data: convert to lowercase for comparison
new_words_df['New_Word_normalized'] = new_words_df['polish'].fillna('').str.lower().str.strip()
sheety_order_df['polish_normalized'] = sheety_order_df['polish'].fillna('').str.lower().str.strip()

# Find matched words between the new words and Sheety data
matched_rows = []
for word in new_words_df['New_Word_normalized']:
    if word in sheety_order_df['polish_normalized'].values:
        matched_rows.append(word)

# Filter the Sheety data to keep only the matched words
filtered_df = sheety_order_df[sheety_order_df['polish_normalized'].isin(matched_rows)]

# Save the filtered data to a new CSV file
filtered_df.to_csv('final.csv', index=False)

print("Filtered new words saved to 'final.csv'.")
