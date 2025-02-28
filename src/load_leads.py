import pandas as pd

def load_leads(file_path='data/final_leads.csv'):
    """Load lead data from CSV file."""
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()  # Ensure no leading/trailing spaces in column names
        return df
    except Exception as e:
        print(f"[ERROR] Failed to load leads dataset: {e}")
        return None

def search_lead(company_name, df):
    """Search for a lead by company name and return lead details."""
    company_name_clean = company_name.strip().lower()
    df['Company'] = df['Company'].str.strip().str.lower()

    result = df[df['Company'] == company_name_clean]

    if result.empty:
        print(f"[ERROR] No lead found for company '{company_name}'.")
        return None

    return result.iloc[0].to_dict()  # Return lead details as a dictionary