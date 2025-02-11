import requests
import pandas as pd
import config

# Get data from Sheety API
END_POINT = config.END_POINT
SHEET_NAME = config.SHEET_NAME
response = requests.get(END_POINT)
data = response.json()

# Extract the saved translations from the response


sheet_data = data[SHEET_NAME]

# Create DataFrame
df = pd.DataFrame(sheet_data)

# Ensure lowercase for all columns (convert them to lowercase)
df.columns = ["English", "Polish", "OriginalEN", "TranslPL", "ID"]

#df.columns = [col.lower() for col in df.columns]

df_english = df[["English", "ID"]]
#----------Swap values in Columns if need -----------
# Swap values in columns 'A' and 'B' for row 1
#df.loc[1, 'A'], df.loc[1, 'B'] = df.loc[1, 'B'], df.loc[1, 'A']

lista_ID =[]
index=0
for value  in df_english['English']:
    if value == 'Polish':

        lista_ID.append(index)
        df.loc[index, "OriginalEN"], df.loc[index,"TranslPL" ] = df.loc[index,"TranslPL" ], df.loc[index, "OriginalEN"]
        df.loc[index, "English" ], df.loc[index, "Polish" ] = df.loc[index, "Polish" ], df.loc[index, "English" ]
        #(df["OriginalEN"][index])
    index += 1
#---------end swaping-----------




df['english'] = df.iloc[:, 2].str.lower()  # Use the third column for English
df['polish'] = df.iloc[:, 3].str.lower()  # Use the forth column for Polish or other language

# Select relevant columns and drop others
df = df[['english', 'polish', 'ID']]

# Save the processed DataFrame into CSV
df.to_csv('sheety_order.csv', index=False)

# For the Polish-only column (TranslPL), save that as a separate file
df_polish = df[['polish']]
df_polish.to_csv('sheety_pl.csv', index=False)

# Check for successful transformation
print("Sheet data processed and saved.")
