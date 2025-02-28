from generate_products import generate_products

def test_generate_products():
    """Test AI-based product and service recommendations."""
    company_name = input("Enter company name: ").strip()

    if not company_name:
        print("[ERROR] Company name cannot be empty.")
        return

    recommendations = generate_products(company_name)
    
    print("\n[RESULT] Recommended Products & Services:")
    print(recommendations)

if __name__ == "__main__":
    test_generate_products()