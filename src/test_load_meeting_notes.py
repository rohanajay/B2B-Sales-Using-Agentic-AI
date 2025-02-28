from load_meeting_notes import load_meeting_notes, get_meeting_summary

def test_meeting_notes():
    """Test loading and retrieving meeting summaries."""
    df = load_meeting_notes()

    if df is None:
        print("[ERROR] Failed to load meeting notes. Exiting.")
        return

    company_name = input("Enter company name: ").strip()
    summary = get_meeting_summary(company_name, df)

    if summary:
        print(f"\n[RESULT] Summary for '{company_name}':\n{summary}")

if __name__ == "__main__":
    test_meeting_notes()