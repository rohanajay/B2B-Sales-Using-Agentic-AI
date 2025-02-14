from recommend_model import recommend_subscription

# Sample overall summaries for testing
test_summaries = [
    {
        "company": "MediTech",
        "summary": "MediTech aims to use GenAI to: 1) Provide personalized medicine recommendations, "
                   "2) Assist doctors in diagnosing conditions faster, "
                   "3) Streamline patient record analysis."
    },
    {
        "company": "FinGrow",
        "summary": "FinGrow plans to implement GenAI for: 1) Automated financial forecasting, "
                   "2) Risk assessment, "
                   "3) Personalized financial advice for customers."
    }
]

print("\n[TEST] Running Subscription Recommendation Model...\n")

for case in test_summaries:
    print(f"Company: {case['company']}")
    recommendation = recommend_subscription(case['summary'])
    print("[RESULT] Recommendation:")
    print(recommendation)
    print("-" * 60)