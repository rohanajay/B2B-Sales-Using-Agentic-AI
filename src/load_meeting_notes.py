import pandas as pd

def load_meeting_notes(file_path='data/final_leads.csv'):
    """Load meeting notes from CSV."""
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()  # Ensure no trailing spaces
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load meeting notes: {e}")
        return None

def get_meeting_summary(company_name, df):
    """Return the meeting summary for the specified company."""
    company_name_clean = company_name.strip().lower()
    df['Company'] = df['Company'].str.strip().str.lower()

    result = df[df['Company'] == company_name_clean]

    if result.empty:
        print(f"[ERROR] No meeting notes found for '{company_name}'.")
        return None

    # Extract summary column
    summary = result['Summary'].values[0].strip()
    if not summary:
        print(f"[WARNING] No summary available for '{company_name}'.")
        return None

    print(f"[RESULT] Meeting Summary for '{company_name}':\n{summary}")
    return summary