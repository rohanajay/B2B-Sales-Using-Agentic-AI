import json
import pandas as pd
from src.load_company import load_company_database, search_company
from src.load_meeting_notes import load_meeting_notes, get_meeting_summary
from src.recommend_model import recommend_subscription
from src.generate_products import generate_products
from src.generate_terms import generate_terms

# Load databases once
company_df = load_company_database()
meeting_df = load_meeting_notes()

def generate_full_quote(company_name):
    """Generate a complete sales quote with all components."""
    quote = {}

    # Step 1: Lookup Company Information
    company_info = search_company(company_name, company_df)
    if not company_info:
        return {"error": f"Company '{company_name}' not found in database."}
    quote["company_info"] = company_info

    # Step 2: Get Meeting Summary
    meeting_summary = get_meeting_summary(company_name, meeting_df)
    if not meeting_summary:
        return {"error": f"No meeting notes found for company '{company_name}'."}
    quote["meeting_summary"] = meeting_summary

    # Step 3: Get Subscription Recommendation
    subscription = recommend_subscription(meeting_summary)
    quote["subscription_recommendation"] = subscription

    # Step 4: Get Products & Services
    products = generate_products(meeting_summary)
    quote["products_and_services"] = products

    # Step 5: Get Purchase Terms
    terms = generate_terms()
    quote["purchase_terms"] = terms

    return quote

def main():
    """Main program to generate a full sales quote."""
    company_name = input("Enter company name for the quote: ").strip()
    result = generate_full_quote(company_name)

    if "error" in result:
        print(f"[ERROR] {result['error']}")
    else:
        output_file = f"output/{company_name.replace(' ', '_')}_quote.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=4)
        print(f"[SUCCESS] Quote generated: {output_file}")

if __name__ == "__main__":
    main()