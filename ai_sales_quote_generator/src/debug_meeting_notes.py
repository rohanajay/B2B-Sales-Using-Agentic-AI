import pandas as pd

# Load the meeting notes CSV
df = pd.read_csv('data/meeting_notes.csv')

# Normalize column names and values
df.columns = df.columns.str.strip().str.lower()
df['company_name'] = df['company_name'].str.strip().str.lower()

# Search for 'meditech'
if 'meditech' in df['company_name'].values:
    print("Found 'MediTech' in company_name!")
else:
    print("MediTech not found.")