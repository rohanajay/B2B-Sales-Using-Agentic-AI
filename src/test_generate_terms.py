from generate_terms import generate_terms

def test_generate_terms():
    """Test AI-generated purchase terms."""
    custom_terms = input("Enter any custom terms (comma-separated) or press Enter for default terms: ").strip()

    if custom_terms:
        custom_terms = [term.strip() for term in custom_terms.split(",")]
    else:
        custom_terms = None

    terms = generate_terms(custom_terms)

    print("\n[RESULT] Generated Purchase Terms:")
    print(terms)

if __name__ == "__main__":
    test_generate_terms()