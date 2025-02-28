from load_leads import load_leads, search_lead

def test_load_and_search():
    """Test loading the dataset and searching for a lead."""
    df = load_leads()

    if df is None:
        print("[ERROR] Failed to load dataset. Exiting.")
        return

    print(f"[INFO] Loaded {len(df)} leads.")

    company_name = input("Enter company name to search: ").strip()
    lead_info = search_lead(company_name, df)

    if lead_info:
        print("[RESULT] Lead Details:")
        for key, value in lead_info.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    test_load_and_search()