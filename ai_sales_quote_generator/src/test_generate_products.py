from generate_products import generate_products

# Sample overall summaries for testing
test_summaries = [
    {
        "company": "MediTech",
        "summary": "MediTech aims to use GenAI to: 1) Provide personalized medicine recommendations, "
                   "2) Assist doctors in diagnosing conditions faster, "
                   "3) Streamline patient record analysis."
    },
    {
        "company": "LogiTrack",
        "summary": "LogiTrack plans to use GenAI for: 1) Real-time logistics tracking, "
                   "2) Route optimization, "
                   "3) Warehouse inventory predictions."
    }
]

print("\n[TEST] Generating Products & Services...\n")

for case in test_summaries:
    print(f"Company: {case['company']}")
    products = generate_products(case['summary'])
    print("[RESULT] Recommended Products & Services:")
    print(products)
    print("-" * 60)