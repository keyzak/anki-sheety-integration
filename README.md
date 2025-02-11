Anki Vocabulary Integration
in that case my motherlanguage is polish
and google translator to english

This project helps you manage vocabulary. It gets words from Google Sheets, check what words you already have in Anki, and add only new ones.
Features

    Get words from Google Sheets (Sheety.co).
    Get words from Anki using AnkiConnect.
    Compare words and find new ones.
    Filter and prepare words before adding.
    Add new words to Anki automatically.

How It Works
1. Fetch Data

    fetch_sheet_data.py → Get words from Google Sheets.
        Creates: sheety_pl.csv

    fetch_anki_data.py → Get words from Anki.
        Creates: fromAnkiPl.csv

2. Compare & Filter

    compare_words.py → Check what words are missing in Anki.
        Creates: new_words.csv

    filter_new_words.py → Prepare words before adding them.
        Creates: new_words_filtered.csv

3. Add to Anki

    add_to_anki.py → Add words to Anki.

How to Use

    Set up Anki deck name and Google Sheets link in config.py:
## configuration file. 

Before running the scripts, update the config file (config.py) with your settings:
DECK_NAME = 'xxxy'  # Name of your Anki deck
SHEET_NAME = 'xxx'  # Name of your Google Sheet (used in Sheety API)

END_POINT = f'https://api.sheety.co/2e12e5e*******/your_file_name_in_sheety/{SHEET_NAME}'  # API endpoint for Sheety

-abova there are my config
How to Set Up:

    Update DECK_NAME with the exact name of your Anki deck.
    Set SHEET_NAME to match your Google Sheet's name in Sheety.
    Use the correct END_POINT from Sheety.co (replace with your own API link).



    Run scripts one by one:

python fetch_sheet_data.py  
python fetch_anki_data.py  
python compare_words.py  
python filter_new_words.py  
python add_to_anki.py  

That’s all! Now your Anki will have new words automatically.
     ```

## Notes
- Make sure Anki is running for AnkiConnect to work.
- Output files (filtered words) will be saved as CSV.


make sure
you have install
-pandas
-requests
-selenium
---
