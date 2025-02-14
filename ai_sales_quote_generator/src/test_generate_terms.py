from generate_terms import generate_terms

# Test Cases: Standard and Custom Terms
test_cases = [
    {
        "name": "Standard Terms",
        "custom_terms": ""
    },
    {
        "name": "Custom Terms for Early Payment",
        "custom_terms": "Include a 2% discount if paid within 10 days."
    }
]

print("\n[TEST] Generating Purchase Terms...\n")

for case in test_cases:
    print(f"Test Case: {case['name']}")
    terms = generate_terms(case['custom_terms'])
    print("[RESULT] Purchase Terms:")
    print(terms)
    print("-" * 60)