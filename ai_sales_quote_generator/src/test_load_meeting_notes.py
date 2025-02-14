from load_meeting_notes import load_meeting_notes, get_meeting_summary

def test_meeting_notes():
    """Test loading and retrieving overall summaries."""
    df = load_meeting_notes()

    if df is None:
        print("[ERROR] Failed to load meeting notes. Exiting.")
        return

    try:
        company_name = input("Enter company name: ").strip()
        if not company_name:
            print("[ERROR] Company name cannot be empty.")
            return

        get_meeting_summary(company_name, df)

    except KeyboardInterrupt:
        print("\n[INFO] Test interrupted by user.")
    except Exception as e:
        print(f"[ERROR] Unexpected error during test: {e}")

if __name__ == "__main__":
    test_meeting_notes()