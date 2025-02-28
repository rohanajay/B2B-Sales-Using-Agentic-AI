from recommend_model import recommend_subscription

def test_recommend_model():
    """Test AI-based subscription recommendation with company name only."""
    company_name = input("Enter company name: ").strip()

    if not company_name:
        print("[ERROR] Company name cannot be empty.")
        return

    recommendation = recommend_subscription(company_name)
    
    print("\n[RESULT] Subscription Recommendation:")
    print(recommendation)

if __name__ == "__main__":
    test_recommend_model()