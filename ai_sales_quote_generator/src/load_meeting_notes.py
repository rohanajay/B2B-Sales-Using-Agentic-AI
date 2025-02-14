import pandas as pd

def load_meeting_notes(file_path='data/meeting_notes.csv'):
    """Load meeting notes CSV into a DataFrame with error handling."""
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        df.columns = df.columns.str.strip().str.lower()  # Normalize column names
        if 'company_name' not in df.columns or 'overall_summary' not in df.columns:
            raise ValueError("CSV must contain 'company_name' and 'overall_summary' columns.")
        return df
    except FileNotFoundError:
        print("[ERROR] File not found.")
        return None
    except pd.errors.EmptyDataError:
        print("[ERROR] CSV file is empty.")
        return None
    except pd.errors.ParserError:
        print("[ERROR] Error parsing CSV file.")
        return None
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        return None

def get_meeting_summary(company_name, df):
    """Return the overall summary for the specified company."""
    company_name_clean = company_name.strip().lower()

    # Normalize company names in DataFrame
    df['company_name'] = df['company_name'].str.strip().str.lower()

    result = df[df['company_name'] == company_name_clean]

    if result.empty:
        print(f"[DEBUG] '{company_name_clean}' not found in meeting notes.")
        return None

    overall_summary = result['overall_summary'].values[0].strip()
    print(f"[RESULT] Overall Summary for '{company_name}':\n{overall_summary}")
    return overall_summary