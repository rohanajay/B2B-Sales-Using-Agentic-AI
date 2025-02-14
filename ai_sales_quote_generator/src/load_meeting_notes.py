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
    """Print only the overall summary for a company."""
    try:
        result = df[df['company_name'] == company_name]

        if not result.empty:
            print("\n[RESULT] Overall Summary:")
            print(result.iloc[0]['overall_summary'])
        else:
            print(f"[INFO] No meeting notes found for company '{company_name}'.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")