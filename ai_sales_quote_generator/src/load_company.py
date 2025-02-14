import pandas as pd

def load_company_database(file_path='data/company_db.csv'):
    """Load the company database CSV into a pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

def search_company(company_name, df):
    """Search for a company by name and return details."""
    result = df[df['Company Name'].str.lower() == company_name.lower()]
    if not result.empty:
        return result.to_dict(orient='records')[0]
    else:
        print(f"Company '{company_name}' not found.")
        return None